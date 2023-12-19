import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .calculations import (
    custom_product_total_price, custom_multi_lat_total_price, custom_kafshoor_profile_total_price,
    plain_user_custom_kafshoor_profile_total_price, steel_price_per_mm2,
    steel_total_area, laser_gas_total_length,
)

from account.decorators import superuser_required

from .forms import (
    CustomProductPrice, CustomMultiLatPrice, CustomKafshoorProfilePrice,
    SteelUnitPrice, SteelArea, PipePrice, DomePrice, BenderPrice,
    LaserGasLength, PointGrillPrice, LineGrillPrice, FullSteelArea, ComponentCategoryCreateForm,
    ComponentCategoryUpdateForm, ProductCreateForm, ProductUpdateForm,
    ComponentCreateForm, ComponentUpdateForm, ComponentConstantCreateForm,
    ComponentConstantUpdateForm, CurrentExpenseCreateForm, CurrentExpenseUpdateForm,

    PlainUserCustomProductPrice, PlainUserCustomMultiLatPrice, PlainUserCustomProfilePrice,
)
from .models import (
    ComponentCategory, Product, Component, ComponentConstant, CurrentExpense,
    TutorialVideo,
)
from .query import create_everything


@superuser_required
def home(request):
    all_products = Product.objects.all()

    seramic_khor = Product.objects.filter(
        name__icontains='سرامیک خور',
    )
    sang_khor = Product.objects.filter(
        name__icontains='سنگ خور'
    )
    grill_khati = Product.objects.filter(
        name__icontains='گریل خطی'
    )
    grill_noghtei = Product.objects.filter(
        name__icontains='گریل نقطه ای'
    )
    full_steel = Product.objects.filter(
        name__icontains='فول استیل'
    )
    dastgire = Product.objects.filter(
        name__icontains='دستگیره'
    )
    sefareshi = Product.objects.filter(
        name__icontains='سفارشی'
    )
    others = Product.objects.exclude(
        Q(name__contains="سرامیک خور") | Q(name__contains="سنگ خور") |
        Q(name__contains="گریل خطی") | Q(name__contains="گریل نقطه ای") |
        Q(name__contains="فول استیل") | Q(name__contains="دستگیره") |
        Q(name__contains="سفارشی")
    )

    context = {
        'all_products': all_products,
        'seramic_khor': seramic_khor,
        'sang_khor': sang_khor,
        'grill_khati': grill_khati,
        'grill_noghtei': grill_noghtei,
        'full_steel': full_steel,
        'dastgire': dastgire,
        'sefareshi': sefareshi,
        'others': others,
    }
    return render(request, 'super_user/home.html', context)


@superuser_required
def product_detail(request, pk):
    product = Product.objects.select_related().filter(pk=pk)[0]
    context = {
        'product': product,
    }
    return render(request, 'super_user/cost/product_detail.html', context)


@superuser_required
def custom_product_price(request):
    form = CustomProductPrice(request.POST or None)

    if request.method == 'POST':
        try:
            product = Product.objects.get(name='کفشور سفارشی')
        except Product.DoesNotExist:
            messages.error(request, 'لطفا ابتدا یک محصول با نام'
                                    '"کفشور سفارشی" ایجاد نمایید.')
            return redirect(reverse('cost:custom_product_price'))

        if form.is_valid():
            upside_piece = form.cleaned_data.get('upside_piece')
            downside_piece = form.cleaned_data.get('downside_piece')
            kind = form.cleaned_data.get('kind')
            steel_kind = form.cleaned_data.get('steel_kind')
            steel_thickness = form.cleaned_data.get('steel_thickness')
            length = form.cleaned_data.get('length')
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            pipe_height = form.cleaned_data.get('pipe_height')
            up_down_length_difference = form.cleaned_data.get('up_down_length_difference')
            up_down_height_difference = form.cleaned_data.get('up_down_height_difference')
            circle_diameter = form.cleaned_data.get('circle_diameter')
            screw_count = form.cleaned_data.get('screw_count')
            dome_count = form.cleaned_data.get('dome_count')
            glue_groove_count = form.cleaned_data.get('glue_groove_count')
            glue_groove_len = form.cleaned_data.get('glue_groove_len')
            additional_length = form.cleaned_data.get('additional_length')
            profit_percent = form.cleaned_data.get('profit_percent')
            factor = form.cleaned_data.get('factor')

            product.profit_percent = profit_percent
            product.save()

            result = custom_product_total_price(
                request, kind, steel_kind, steel_thickness,
                upside_piece, downside_piece, length, width, height, pipe_height,
                up_down_length_difference, up_down_height_difference,
                circle_diameter, screw_count, glue_groove_count, glue_groove_len,
                additional_length, dome_count)

            product = Product.objects.get(name='کفشور سفارشی')
            price_with_factor = int(product.final_price * factor)

            if result == 0:
                messages.error(request, 'شما باید حداقل یکی از تیک های '
                                        'قسمت رویی یا قسمت زیرین را بزنید!')

    else:
        product = None
        price_with_factor = None

    context = {
        'form': form,
        'product': product,
        'price_with_factor': price_with_factor,
    }
    return render(request, 'super_user/cost/custom_product_price.html', context)


@superuser_required
def custom_multi_lat_price(request):
    form = CustomMultiLatPrice(request.POST or None)

    if request.method == 'POST':
        try:
            product = Product.objects.get(name='کفشور چند لتی سفارشی')
        except Product.DoesNotExist:
            messages.error(request, 'لطفا ابتدا یک محصول با نام'
                                    '"کفشور چند لتی سفارشی" ایجاد نمایید.')
            return redirect(reverse('cost:custom_multi_lat_price'))

        if form.is_valid():
            kafshoor_count = form.cleaned_data.get('kafshoor_count')
            length = form.cleaned_data.get('length')
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            glue_groove_count = form.cleaned_data.get('glue_groove_count')
            glue_groove_len = form.cleaned_data.get('glue_groove_len')
            screw_count = form.cleaned_data.get('screw_count')
            divider_count = form.cleaned_data.get('divider_count')
            divider_width = form.cleaned_data.get('divider_width')
            z_branch_length = form.cleaned_data.get('z_branch_length')
            z_branch_width = form.cleaned_data.get('z_branch_width')
            l_pin_count = form.cleaned_data.get('l_pin_count')
            u_divider_count = form.cleaned_data.get('u_divider_count')
            u_divider_length = form.cleaned_data.get('u_divider_length')
            u_divider_width = form.cleaned_data.get('u_divider_width')
            u_divider_height = form.cleaned_data.get('u_divider_height')
            profit_percent = form.cleaned_data.get('profit_percent')
            factor = form.cleaned_data.get('factor')

            product.profit_percent = profit_percent
            product.save()

            result = custom_multi_lat_total_price(
                request, kafshoor_count, length, width, height, glue_groove_count, glue_groove_len,
                screw_count, divider_count, divider_width, z_branch_length, z_branch_width, l_pin_count,
                u_divider_count, u_divider_length, u_divider_width, u_divider_height, factor)

            product = Product.objects.get(name='کفشور چند لتی سفارشی')
            price_with_factor = int(product.final_price * factor)

    else:
        product = None
        price_with_factor = None

    context = {
        'form': form,
        'product': product,
        'price_with_factor': price_with_factor,
    }
    return render(request, 'super_user/cost/custom_multi_lat_price.html', context)


@superuser_required
def custom_kafshoor_profile_price(request):
    form = CustomKafshoorProfilePrice(request.POST or None)

    if request.method == 'POST':
        try:
            product = Product.objects.get(name='کفشور پروفیلی سفارشی')
        except Product.DoesNotExist:
            messages.error(request, 'لطفا ابتدا یک محصول با نام'
                                    '"کفشور پروفیلی سفارشی" ایجاد نمایید.')
            return redirect(reverse('cost:custom_kafshoor_profile_price'))

        if form.is_valid():
            profile_count = form.cleaned_data.get('profile_count')
            profile_length = form.cleaned_data.get('profile_length')
            profile_width = form.cleaned_data.get('profile_width')
            profile_height = form.cleaned_data.get('profile_height')
            adjust_jack_count = form.cleaned_data.get('adjust_jack_count')
            divider_count = form.cleaned_data.get('divider_count')
            divider_width = form.cleaned_data.get('divider_width')
            screw_count = form.cleaned_data.get('screw_count')
            profit_percent = form.cleaned_data.get('profit_percent')
            factor = form.cleaned_data.get('factor')

            product.profit_percent = profit_percent
            product.save()

            result = custom_kafshoor_profile_total_price(
                request, profile_count, profile_length, profile_width, profile_height,
                adjust_jack_count, divider_count, divider_width, screw_count)

            product = Product.objects.get(name='کفشور پروفیلی سفارشی')
            price_with_factor = int(product.final_price * factor)

    else:
        product = None
        price_with_factor = None

    context = {
        'form': form,
        'product': product,
        'price_with_factor': price_with_factor,
    }
    return render(request, 'super_user/cost/custom_kafshoor_profile_price.html', context)


@superuser_required
def steel_area(request):
    form = SteelArea(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            upside_piece = form.cleaned_data.get('upside_piece')
            downside_piece = form.cleaned_data.get('downside_piece')
            width = form.cleaned_data.get('width')
            length = form.cleaned_data.get('length')
            height = form.cleaned_data.get('height')
            up_down_length_difference = form.cleaned_data.get('up_down_length_difference')
            up_down_height_difference = form.cleaned_data.get('up_down_height_difference')

            result = steel_total_area(
                upside_piece, downside_piece, width, length, height,
                up_down_length_difference, up_down_height_difference)
            request.session['area'] = result
        else:
            messages.error(request, 'Please fill out the form correctly.')
    else:
        if request.session.get('area'):
            del request.session['area']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/steel_area.html', context)


@superuser_required
def steel_unit_price(request):
    form = SteelUnitPrice(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            width = form.cleaned_data.get('width')
            length = form.cleaned_data.get('length')
            weight = form.cleaned_data.get('weight')
            price_per_kilogram = form.cleaned_data.get('price_per_kilogram')

            result = steel_price_per_mm2(length, width, weight, price_per_kilogram)
            request.session['cost'] = result
        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('cost'):
            del request.session['cost']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/steel_unit_price.html', context)


@superuser_required
def pipe_unit_price(request):
    form = PipePrice(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            length = form.cleaned_data.get('length')
            price = form.cleaned_data.get('price')

            result = price / length
            request.session['pipe_cost'] = result
        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('pipe_cost'):
            del request.session['pipe_cost']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/pipe_unit_price.html', context)


@superuser_required
def dome_price(request):
    form = DomePrice(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            count = form.cleaned_data.get('count')
            price = form.cleaned_data.get('price')

            result = price / count
            request.session['dome_cost'] = result
        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('dome_cost'):
            del request.session['dome_cost']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/dome_price.html', context)


@superuser_required
def bender_price(request):
    form = BenderPrice(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            count = form.cleaned_data.get('count')
            price = form.cleaned_data.get('price')

            result = price / count
            request.session['bender_cost'] = result
        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('bender_cost'):
            del request.session['bender_cost']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/bender_price.html', context)


@superuser_required
def laser_gas_length(request):
    form = LaserGasLength(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            upside_piece = form.cleaned_data.get('upside_piece')
            downside_piece = form.cleaned_data.get('downside_piece')
            length = form.cleaned_data.get('length')
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            circle_diameter = form.cleaned_data.get('circle_diameter')
            up_down_length_difference = form.cleaned_data.get('up_down_length_difference')
            up_down_height_difference = form.cleaned_data.get('up_down_height_difference')
            screw_count = form.cleaned_data.get('screw_count')
            glue_groove_count = form.cleaned_data.get('glue_groove_count')
            glue_groove_len = form.cleaned_data.get('glue_groove_len')
            additional_length = form.cleaned_data.get('additional_length')

            total_length = laser_gas_total_length(
                upside_piece, downside_piece, length, width, height,
                circle_diameter, up_down_length_difference,
                up_down_height_difference, screw_count, glue_groove_count, glue_groove_len,
                additional_length)

            request.session['laser_gas_len'] = total_length

        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('laser_gas_len'):
            del request.session['laser_gas_len']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/laser_gas_length.html', context)


@superuser_required
def point_grill_price(request):
    form = PointGrillPrice(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            length = form.cleaned_data.get('length')
            try:
                obj = ComponentCategory.objects.get(name='لیزر و گاز').price
            except ComponentCategory.DoesNotExist:
                messages.error(request, 'لطفا ابتدا یک دسته بندی اجزا با نام'
                                        '"لیزر و گاز" ایجاد نمایید.')
                return redirect(reverse('cost:point_grill_price'))

            result = obj * length * 4

            request.session['point_grill_cost'] = result
        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('point_grill_cost'):
            del request.session['point_grill_cost']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/point_grill_price.html', context)


@superuser_required
def line_grill_price(request):
    form = LineGrillPrice(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            length = form.cleaned_data.get('length')
            width = form.cleaned_data.get('width')
            try:
                obj = ComponentCategory.objects.get(name='لیزر و گاز').price
            except ComponentCategory.DoesNotExist:
                messages.error(request, 'لطفا ابتدا یک دسته بندی اجزا با نام'
                                        '"لیزر و گاز" ایجاد نمایید.')
                return redirect(reverse('cost:line_grill_price'))

            result = obj * (length + width) * 2

            request.session['line_grill_cost'] = result
        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')
    else:
        if request.session.get('line_grill_cost'):
            del request.session['line_grill_cost']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/line_grill_price.html', context)


@superuser_required
def full_steel_area(request):
    form = FullSteelArea(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            upside_piece = form.cleaned_data.get('upside_piece')
            downside_piece = form.cleaned_data.get('downside_piece')
            width = form.cleaned_data.get('width')
            length = form.cleaned_data.get('length')
            height = form.cleaned_data.get('height')
            up_down_length_difference = form.cleaned_data.get('up_down_length_difference')
            up_down_height_difference = form.cleaned_data.get('up_down_height_difference')

            result = steel_total_area(
                upside_piece, downside_piece, width, length, height,
                up_down_length_difference, up_down_height_difference)
            request.session['area'] = result
        else:
            messages.error(request, 'Please fill out the form correctly.')
    else:
        if request.session.get('area'):
            del request.session['area']

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/full_steel_area.html', context)


@superuser_required
def component_category_list(request):
    component_categories = ComponentCategory.objects.all()

    context = {
        'component_categories': component_categories,
    }
    return render(request, 'super_user/cost/component_category_list.html', context)


@superuser_required
def component_category_create(request):
    form = ComponentCategoryCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            ComponentCategory.objects.create(name=name, price=price, description=description)
            messages.success(request, f'{name} با قیمت {price} تومان با موفقیت افزوده شد! ')
            return redirect(reverse('cost:component_category_list'))

        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/component_category_create.html', context)


@superuser_required
def component_category_update(request, pk):
    obj = get_object_or_404(ComponentCategory, pk=pk)
    # pass the object as instance in form
    form = ComponentCategoryUpdateForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, 'با موفقیت به روزرسانی شد!')
        return redirect(reverse('cost:component_category_list'))

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'super_user/cost/component_category_update.html', context)


@superuser_required
def component_category_delete(request, pk):
    component_category = get_object_or_404(ComponentCategory, pk=pk)

    # if request.method == "POST" and request.user.is_authenticated:
    if request.method == "POST":
        component_category.delete()
        messages.success(request, f"{component_category.name}"
                                  f" با قیمت "
                                  f"{component_category.price}"
                                  f" تومان با موفقیت حذف شد! ")
        return redirect(reverse('cost:component_category_list'))

    context = {
        'component_category': component_category,
        'pk': pk,
    }
    return render(request, 'super_user/cost/component_category_delete.html', context)


@superuser_required
def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'super_user/cost/product_list.html', context)


@superuser_required
def product_create(request):
    form = ProductCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            product_image = form.cleaned_data.get('product_image')
            no_prod_per_year = form.cleaned_data.get('no_prod_per_year')
            components_cost = form.cleaned_data.get('components_cost')
            current_expense = form.cleaned_data.get('current_expense')
            profit_percent = form.cleaned_data.get('profit_percent')
            final_price = form.cleaned_data.get('final_price')
            product = Product.objects.create(
                name=name, description=description, product_image=product_image,
                no_prod_per_year=no_prod_per_year, components_cost=components_cost,
                current_expense=current_expense, profit_percent=profit_percent,
                final_price=final_price
            )
            messages.success(request, f'{name} با موفقیت افزوده شد! ')
            return redirect(reverse('cost:product_detail',
                                    kwargs={'pk': product.pk}))

        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/product_create.html', context)


@superuser_required
def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    # pass the object as instance in form
    form = ProductUpdateForm(request.POST or None, request.FILES or None,
                             instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, 'با موفقیت به روزرسانی شد!')
        return redirect(reverse('cost:product_detail',
                                kwargs={'pk': pk}))

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'super_user/cost/product_update.html', context)


@superuser_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print('pk : ', pk)

    # if request.method == "POST" and request.user.is_authenticated:
    if request.method == "POST":
        product.delete()
        messages.success(request, f"{product.name}"
                                  f" با موفقیت حذف شد! ")
        return redirect(reverse('cost:product_list'))

    context = {
        'product': product,
        'pk': pk,
    }
    return render(request, 'super_user/cost/product_delete.html', context)


@superuser_required
def component_list(request):
    components = Component.objects.all()

    context = {
        'components': components,
    }
    return render(request, 'super_user/cost/component_list.html', context)


@superuser_required
def component_create(request):
    form = ComponentCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            category = form.cleaned_data.get('category')
            product = form.cleaned_data.get('product')
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            component_image = form.cleaned_data.get('component_image')
            used_count = form.cleaned_data.get('used_count')
            per_product = form.cleaned_data.get('per_product')
            Component.objects.create(
                category=category, product=product, name=name,
                description=description, component_image=component_image,
                used_count=used_count, per_product=per_product
            )
            messages.success(request, f'{name} با موفقیت افزوده شد! ')
            return redirect(reverse('cost:product_detail',
                                    kwargs={'pk': product.pk}))

        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/component_create.html', context)


@superuser_required
def component_update(request, pk):
    obj = get_object_or_404(Component, pk=pk)
    # pass the object as instance in form
    form = ComponentUpdateForm(request.POST or None, request.FILES or None,
                               instance=obj)

    if form.is_valid():
        form.save()
        product = form.cleaned_data.get('product')
        messages.success(request, 'با موفقیت به روزرسانی شد!')
        return redirect(reverse('cost:product_detail',
                                kwargs={'pk': product.pk}))

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'super_user/cost/component_update.html', context)


@superuser_required
def component_delete(request, pk):
    component = get_object_or_404(Component, pk=pk)

    # if request.method == "POST" and request.user.is_authenticated:
    if request.method == "POST":
        component.delete()
        messages.success(request, f"{component.name}"
                                  f" برای محصول "
                                  f"{component.product}"
                                  f" با موفقیت حذف شد! ")
        return redirect(reverse('cost:component_list'))

    context = {
        'component': component,
        'pk': pk,
    }
    return render(request, 'super_user/cost/component_delete.html', context)


@superuser_required
def component_constant_list(request):
    component_constants = ComponentConstant.objects.all()

    context = {
        'component_constants': component_constants,
    }
    return render(request, 'super_user/cost/component_constant_list.html', context)


@superuser_required
def component_constant_create(request):
    form = ComponentConstantCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            component_constant_image = form.cleaned_data.get('component_constant_image')
            product = form.cleaned_data.get('product')
            price = form.cleaned_data.get('price')
            per_product = form.cleaned_data.get('per_product')
            ComponentConstant.objects.create(
                name=name, description=description, component_constant_image=component_constant_image,
                product=product, price=price, per_product=per_product,
            )
            messages.success(request, f'{name} با موفقیت افزوده شد! ')
            return redirect(reverse('cost:product_detail',
                                    kwargs={'pk': product.pk}))

        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/component_constant_create.html', context)


@superuser_required
def component_constant_update(request, pk):
    obj = get_object_or_404(ComponentConstant, pk=pk)
    # pass the object as instance in form
    form = ComponentConstantUpdateForm(request.POST or None, request.FILES or None,
                                       instance=obj)

    if form.is_valid():
        form.save()
        product = form.cleaned_data.get('product')
        messages.success(request, 'با موفقیت به روزرسانی شد!')
        return redirect(reverse('cost:product_detail',
                                kwargs={'pk': product.pk}))

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'super_user/cost/component_constant_update.html', context)


@superuser_required
def component_constant_delete(request, pk):
    component_constant = get_object_or_404(ComponentConstant, pk=pk)

    # if request.method == "POST" and request.user.is_authenticated:
    if request.method == "POST":
        component_constant.delete()
        messages.success(request, f"{component_constant.name}"
                                  f" برای محصول "
                                  f"{component_constant.product}"
                                  f" با موفقیت حذف شد! ")
        return redirect(reverse('cost:component_constant_list'))

    context = {
        'component_constant': component_constant,
        'pk': pk,
    }
    return render(request, 'super_user/cost/component_constant_delete.html', context)


@superuser_required
def current_expense_list(request):
    current_expenses = CurrentExpense.objects.all()

    context = {
        'current_expenses': current_expenses,
    }
    return render(request, 'super_user/cost/current_expense_list.html', context)


@superuser_required
def current_expense_create(request):
    form = CurrentExpenseCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            cost_in_a_year = form.cleaned_data.get('cost_in_a_year')
            CurrentExpense.objects.create(
                name=name, cost_in_a_year=cost_in_a_year,
            )
            messages.success(request, f'{name} با موفقیت افزوده شد! ')
            return redirect(reverse('cost:current_expense_list'))

        else:
            messages.error(request, 'لطفا فرم را به درستی پر نمایید!')

    context = {
        'form': form,
    }
    return render(request, 'super_user/cost/current_expense_create.html', context)


@superuser_required
def current_expense_update(request, pk):
    obj = get_object_or_404(CurrentExpense, pk=pk)
    # pass the object as instance in form
    form = CurrentExpenseUpdateForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, 'با موفقیت به روزرسانی شد!')
        return redirect(reverse('cost:current_expense_list'))

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'super_user/cost/current_expense_update.html', context)


@superuser_required
def current_expense_delete(request, pk):
    current_expense = get_object_or_404(CurrentExpense, pk=pk)

    # if request.method == "POST" and request.user.is_authenticated:
    if request.method == "POST":
        current_expense.delete()
        messages.success(request, f"{current_expense.name}"
                                  f" برای محصول "
                                  f"{current_expense.cost_in_a_year}"
                                  f" با موفقیت حذف شد! ")
        return redirect(reverse('cost:current_expense_list'))

    context = {
        'current_expense': current_expense,
        'pk': pk,
    }
    return render(request, 'super_user/cost/current_expense_delete.html', context)


@superuser_required
def help_page(request):
    videos = TutorialVideo.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'super_user/help.html', context)


@login_required
def plain_user_home(request):
    all_products = Product.objects.all()

    seramic_khor = Product.objects.filter(
        name__icontains='سرامیک خور',
    )
    sang_khor = Product.objects.filter(
        name__icontains='سنگ خور'
    )
    grill_khati = Product.objects.filter(
        name__icontains='گریل خطی'
    )
    grill_noghtei = Product.objects.filter(
        name__icontains='گریل نقطه ای'
    )
    full_steel = Product.objects.filter(
        name__icontains='فول استیل'
    )
    dastgire = Product.objects.filter(
        name__icontains='دستگیره'
    )
    sefareshi = Product.objects.filter(
        name__icontains='سفارشی'
    )
    others = Product.objects.exclude(
        Q(name__contains="سرامیک خور") | Q(name__contains="سنگ خور") |
        Q(name__contains="گریل خطی") | Q(name__contains="گریل نقطه ای") |
        Q(name__contains="فول استیل") | Q(name__contains="دستگیره") |
        Q(name__contains="سفارشی")
    )

    context = {
        'all_products': all_products,
        'seramic_khor': seramic_khor,
        'sang_khor': sang_khor,
        'grill_khati': grill_khati,
        'grill_noghtei': grill_noghtei,
        'full_steel': full_steel,
        'dastgire': dastgire,
        'sefareshi': sefareshi,
        'others': others,
    }
    return render(request, 'plain_user/home.html', context)


@login_required
def plain_user_custom_product_price(request):
    form = PlainUserCustomProductPrice(request.POST or None)

    if request.method == 'POST':
        try:
            product = Product.objects.get(name='کفشور سفارشی')
        except Product.DoesNotExist:
            messages.error(request, 'لطفا ابتدا از ادمین بخواهید یک محصول با نام'
                                    '"کفشور سفارشی" ایجاد نماید.')
            return redirect(reverse('cost:plain_user_custom_product_price'))

        if form.is_valid():
            upside_piece = form.cleaned_data.get('upside_piece')
            downside_piece = form.cleaned_data.get('downside_piece')
            kind = form.cleaned_data.get('kind')
            length = form.cleaned_data.get('length')
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            pipe_height = form.cleaned_data.get('pipe_height')
            up_down_length_difference = form.cleaned_data.get('up_down_length_difference')
            up_down_height_difference = form.cleaned_data.get('up_down_height_difference')
            circle_diameter = form.cleaned_data.get('circle_diameter')
            screw_count = form.cleaned_data.get('screw_count')
            dome_count = form.cleaned_data.get('dome_count')
            glue_groove_count = form.cleaned_data.get('glue_groove_count')
            glue_groove_len = form.cleaned_data.get('glue_groove_len')
            additional_length = form.cleaned_data.get('additional_length')
            factor = form.cleaned_data.get('factor')

            result = custom_product_total_price(
                request, kind,
                upside_piece, downside_piece, length, width, height, pipe_height,
                up_down_length_difference, up_down_height_difference,
                circle_diameter, screw_count, glue_groove_count, glue_groove_len,
                additional_length, dome_count)

            product = Product.objects.get(name='کفشور سفارشی')
            price_with_factor = int(product.final_price * factor)

            if result == 0:
                messages.error(request, 'شما باید حداقل یکی از تیک های '
                                        'قسمت رویی یا قسمت زیرین را بزنید!')

    else:
        product = None
        price_with_factor = None

    context = {
        'form': form,
        'product': product,
        'price_with_factor': price_with_factor,
    }
    return render(request, 'plain_user/cost/custom_product_price.html', context)


@login_required
def plain_user_custom_multi_lat_price(request):
    form = PlainUserCustomMultiLatPrice(request.POST or None)

    if request.method == 'POST':
        try:
            product = Product.objects.get(name='کفشور چند لتی سفارشی')
        except Product.DoesNotExist:
            messages.error(request, 'لطفا ابتدا از ادمین بخواهید یک محصول با نام'
                                    '"کفشور چند لتی سفارشی" ایجاد نمایید.')
            return redirect(reverse('cost:plain_user_custom_multi_lat_price'))

        if form.is_valid():
            kafshoor_count = form.cleaned_data.get('kafshoor_count')
            length = form.cleaned_data.get('length')
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
            glue_groove_count = form.cleaned_data.get('glue_groove_count')
            glue_groove_len = form.cleaned_data.get('glue_groove_len')
            screw_count = form.cleaned_data.get('screw_count')
            divider_count = form.cleaned_data.get('divider_count')
            divider_width = form.cleaned_data.get('divider_width')
            z_branch_length = form.cleaned_data.get('z_branch_length')
            z_branch_width = form.cleaned_data.get('z_branch_width')
            l_pin_count = form.cleaned_data.get('l_pin_count')
            u_divider_count = form.cleaned_data.get('u_divider_count')
            u_divider_length = form.cleaned_data.get('u_divider_length')
            u_divider_width = form.cleaned_data.get('u_divider_width')
            u_divider_height = form.cleaned_data.get('u_divider_height')
            factor = form.cleaned_data.get('factor')

            result = custom_multi_lat_total_price(
                request, kafshoor_count, length, width, height, glue_groove_count, glue_groove_len,
                screw_count, divider_count, divider_width, z_branch_length, z_branch_width, l_pin_count,
                u_divider_count, u_divider_length, u_divider_width, u_divider_height, factor)

            product = Product.objects.get(name='کفشور چند لتی سفارشی')
            price_with_factor = int(product.final_price * factor)

    else:
        product = None
        price_with_factor = None

    context = {
        'form': form,
        'product': product,
        'price_with_factor': price_with_factor,
    }
    return render(request, 'plain_user/cost/custom_multi_lat_price.html', context)


@login_required
def plain_user_custom_kafshoor_profile_price(request):
    form = PlainUserCustomProfilePrice(request.POST or None)

    if request.method == 'POST':
        try:
            product = Product.objects.get(name='کفشور پروفیلی سفارشی')
        except Product.DoesNotExist:
            messages.error(request, 'لطفا ابتدا از ادمین بخواهید یک محصول با نام'
                                    '"کفشور پروفیلی سفارشی" ایجاد نمایید.')
            return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

        if form.is_valid():
            profile_count = form.cleaned_data.get('profile_count')
            profile_length = form.cleaned_data.get('profile_length')
            profile_width = form.cleaned_data.get('profile_width')
            profile_height = form.cleaned_data.get('profile_height')
            adjust_jack_count = form.cleaned_data.get('adjust_jack_count')
            divider_count = form.cleaned_data.get('divider_count')
            divider_width = form.cleaned_data.get('divider_width')
            screw_count = form.cleaned_data.get('screw_count')
            factor = form.cleaned_data.get('factor')

            result = plain_user_custom_kafshoor_profile_total_price(
                request, profile_count, profile_length, profile_width, profile_height,
                adjust_jack_count, divider_count, divider_width, screw_count)

            product = Product.objects.get(name='کفشور پروفیلی سفارشی')
            price_with_factor = int(product.final_price * factor)

    else:
        product = None
        price_with_factor = None

    context = {
        'form': form,
        'product': product,
        'price_with_factor': price_with_factor,
    }
    return render(request, 'plain_user/cost/custom_kafshoor_profile_price.html', context)


@superuser_required
def run_the_query(request):
    create_everything()
    return render(request, 'super_user/query.html')
