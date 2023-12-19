import math

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from cost.models import Product, Component


def custom_product_total_price(
        request, kind, steel_kind, steel_thickness,
        upside_piece, downside_piece, length, width, height, pipe_height,
        up_down_length_difference, up_down_height_difference,
        circle_diameter, screw_count, glue_groove_count, glue_groove_len,
        additional_length, dome_count):
    custom_product = Product.objects.filter(name='کفشور سفارشی')[0]

    if not upside_piece and not downside_piece:
        return 0

    try:
        pipe_component = custom_product.component_set.get(
            name='لوله کفشور سفارشی',
            category__name='لوله 51 میلی متری')
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لوله کفشور سفارشی" برای این محصول ایجاد نمایید.')
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لوله کفشور سفارشی" و با نام دسته بندی '
                                '"لوله 51 میلی متری" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_product_price'))

    if downside_piece:
        pipe_component.used_count = pipe_height
        pipe_component.save()
    else:
        pipe_component.used_count = 0
        pipe_component.save()

    steel_area = steel_total_area(
        upside_piece, downside_piece, length, width, height,
        up_down_length_difference, up_down_height_difference)

    try:
        steel_component = custom_product.component_set.get(category__name='ورق استیل 1.5 میلی متری 304')
        steel_component.used_count = 0
        steel_component.save()
        steel_component = custom_product.component_set.get(category__name='ورق استیل 3 میلی متری 304')
        steel_component.used_count = 0
        steel_component.save()
        steel_component = custom_product.component_set.get(category__name='ورق استیل 1.5 میلی متری 316')
        steel_component.used_count = 0
        steel_component.save()
        steel_component = custom_product.component_set.get(category__name='ورق استیل 3 میلی متری 316')
        steel_component.used_count = 0
        steel_component.save()

        if int(steel_kind) == 304 and int(steel_thickness) == 15:
            steel_component = custom_product.component_set.get(category__name='ورق استیل 1.5 میلی متری 304')
            steel_component.used_count = steel_area
            steel_component.save()
        elif int(steel_kind) == 304 and int(steel_thickness) == 30:
            steel_component = custom_product.component_set.get(category__name='ورق استیل 3 میلی متری 304')
            steel_component.used_count = steel_area
            steel_component.save()
        elif int(steel_kind) == 316 and int(steel_thickness) == 15:
            steel_component = custom_product.component_set.get(category__name='ورق استیل 1.5 میلی متری 316')
            steel_component.used_count = steel_area
            steel_component.save()
        elif int(steel_kind) == 316 and int(steel_thickness) == 30:
            steel_component = custom_product.component_set.get(category__name='ورق استیل 3 میلی متری 316')
            steel_component.used_count = steel_area
            steel_component.save()

    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 1.5 میلی متری 304 کفشور سفارشی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_product_price'))

    laser_gas_len = laser_gas_total_length(
        upside_piece, downside_piece, length, width, height,
        circle_diameter, up_down_length_difference,
        up_down_height_difference, screw_count, glue_groove_count, glue_groove_len,
        additional_length)

    try:
        laser_gas_component = custom_product.component_set.get(
            name='لیزر و گاز کفشور سفارشی', category__name='لیزر و گاز')
        laser_gas_component.used_count = laser_gas_len
        laser_gas_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز کفشور سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_product_price'))

    try:
        screw_component = custom_product.component_set.get(
            name='پیچ 1.5 سانتی کفشور سفارشی',
            category__name='پیچ 1.5 سانتی')
        screw_component.used_count = screw_count
        screw_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"پیچ 1.5 سانتی کفشور سفارشی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_product_price'))

    try:
        dome_component = custom_product.component_set.get(category__name='نکی')
        dome_component.used_count = dome_count
        dome_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"نکی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_product_price'))

    try:
        grill_component = custom_product.component_set.get(
            name='گریل کفشور سفارشی', category__name='لیزر و گاز')
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"گریل کفشور سفارشی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_product_price'))

    if upside_piece and kind == 'line_grill' or kind == 'point_grill':
        grill_len = grill_length(kind, length, width, up_down_length_difference)
        grill_component.used_count = grill_len
        grill_component.save()
    else:
        grill_component.used_count = 0
        grill_component.save()

    return custom_product


def custom_multi_lat_total_price(
        request, kafshoor_count, length, width, height, glue_groove_count, glue_groove_len,
        screw_count, divider_count, divider_width, z_branch_length, z_branch_width, l_pin_count,
        u_divider_count, u_divider_length, u_divider_width, u_divider_height, factor):
    custom_product = Product.objects.filter(name='کفشور چند لتی سفارشی')[0]

    try:
        steel_area = steel_total_area(False, True, length, width, height, 0, 0)
        steel_15_component = custom_product.component_set.get(
            name='ورق استیل 1.5 میلی متری 304 کفشور چند لتی سفارشی',
            category__name='ورق استیل 1.5 میلی متری 304')
        steel_15_component.used_count = kafshoor_count * steel_area
        steel_15_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 1.5 میلی متری 304 کفشور چند لتی سفارشی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        laser_gas_len = laser_gas_total_length_v2(length, width, height, screw_count,
                                                  glue_groove_count, glue_groove_len)
        laser_gas_component = custom_product.component_set.get(
            name='لیزر و گاز کفشور چند لتی سفارشی', category__name='لیزر و گاز')
        laser_gas_component.used_count = laser_gas_len
        laser_gas_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        screw_component = custom_product.component_set.get(
            name='پیچ 1.5 سانتی کفشور چند لتی سفارشی',
            category__name='پیچ 1.5 سانتی')
        screw_component.used_count = screw_count
        screw_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"پیچ 1.5 سانتی کفشور چند لتی سفارشی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        bend_component = custom_product.component_set.get(
            name='خم کفشور چند لتی سفارشی', category__name='خم')
        bend_component.used_count = kafshoor_count * 4
        bend_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"خم کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"خم" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        weld_component = custom_product.component_set.get(
            name='جوش کفشور چند لتی سفارشی', category__name='جوش')
        weld_component.used_count = kafshoor_count
        weld_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"جوش کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"جوش" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        reamer_component = custom_product.component_set.get(
            name='قلاویز کفشور چند لتی سفارشی', category__name='قلاویز')
        reamer_component.used_count = kafshoor_count * screw_count
        reamer_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"قلاویز کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"قلاویز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        divider_steel_3_component = custom_product.component_set.get(
            name='ورق استیل 3 میلی متری 304 (برای دیوایدر) کفشور چند لتی سفارشی',
            category__name='ورق استیل 3 میلی متری 304')
        # used_count = عرض * طول * تعداد دیوایدر
        divider_length = (kafshoor_count * width) + ((kafshoor_count + 1) * 10)
        divider_steel_3_component.used_count = divider_count * divider_length * divider_width
        divider_steel_3_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 3 میلی متری 304 (برای دیوایدر) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"ورق استیل 3 میلی متری 304" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        divider_laser_gas_component = custom_product.component_set.get(
            name='لیزر و گاز (برای دیوایدر) کفشور چند لتی سفارشی',
            category__name='لیزر و گاز')
        divider_length = (kafshoor_count * width) + ((kafshoor_count + 1) * 10)
        environment = (divider_length * 2) + divider_width * 2
        divider_laser_gas_component.used_count = divider_count * (environment + (divider_length / 1.6) * 3)
        divider_laser_gas_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز (برای دیوایدر) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        z_branch_steel_component = custom_product.component_set.get(
            name='ورق استیل 1.5 میلی متری 304 (برای شاخه Z) کفشور چند لتی سفارشی',
            category__name='ورق استیل 1.5 میلی متری 304')
        z_branch_steel_component.used_count = z_branch_length * z_branch_width
        z_branch_steel_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 1.5 میلی متری 304 (برای شاخه Z) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"ورق استیل 1.5 میلی متری 304" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        z_branch_l_pin_component = custom_product.component_set.get(
            name='ال پین (برای شاخه Z) کفشور چند لتی سفارشی',
            category__name='ال پین')
        z_branch_l_pin_component.used_count = l_pin_count
        z_branch_l_pin_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ال پین (برای شاخه Z) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"ال پین" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        z_branch_bend_component = custom_product.component_set.get(
            name='خم (برای شاخه Z) کفشور چند لتی سفارشی',
            category__name='خم')
        z_branch_bend_component.used_count = 8
        z_branch_bend_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"خم (برای شاخه Z) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"خم" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        z_branch_laser_gas_component = custom_product.component_set.get(
            name='لیزر و گاز (برای شاخه Z) کفشور چند لتی سفارشی',
            category__name='لیزر و گاز')
        extra_length = 100
        z_branch_laser_gas_component.used_count = \
            (z_branch_length + z_branch_width) * 2 + extra_length
        z_branch_laser_gas_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز (برای شاخه Z) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        u_divider_steel_30_component = custom_product.component_set.get(
            name='ورق استیل 3 میلی متری 304 (برای دیوایدر U) کفشور چند لتی سفارشی',
            category__name='ورق استیل 3 میلی متری 304')
        u_divider_steel_30_component.used_count = \
            u_divider_count * u_divider_length * (u_divider_height * 2 + u_divider_width)
        u_divider_steel_30_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 3 میلی متری 304 (برای دیوایدر U) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"ورق استیل 3 میلی متری 304" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    try:
        u_divider_steel_30_component = custom_product.component_set.get(
            name='لیزر و گاز (برای دیوایدر U) کفشور چند لتی سفارشی',
            category__name='لیزر و گاز')
        width = (u_divider_height * 2 + u_divider_width)
        environment = (u_divider_length * 2) + (width * 2)
        extra_length = 100
        u_divider_steel_30_component.used_count = u_divider_count * (environment + extra_length)
        u_divider_steel_30_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز (برای دیوایدر U) کفشور چند لتی سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_multi_lat_price'))

    return custom_product.final_price


def custom_kafshoor_profile_total_price(
        request, profile_count, profile_length, profile_width, profile_height,
        adjust_jack_count, divider_count, divider_width, screw_count):
    custom_product = Product.objects.filter(name='کفشور پروفیلی سفارشی')[0]

    try:
        rod_component = custom_product.component_set.get(
            name='ورق استیل پروفیل کفشور پروفیلی سفارشی',
            category__name='ورق استیل پروفیل')
        rod_component.used_count = profile_count * (profile_height + profile_width) * 2 * profile_length
        rod_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل پروفیل کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"ورق استیل پروفیل" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_kafshoor_profile_price'))

    try:
        rod_cut_component = custom_product.component_set.get(
            name='برش پروفیل کفشور پروفیلی سفارشی',
            category__name='برش پروفیل')
        rod_cut_component.used_count = profile_count * 2
        rod_cut_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"برش پروفیل کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"برش پروفیل" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_kafshoor_profile_price'))

    try:
        adjust_jack_component = custom_product.component_set.get(
            name='جک تنظیم کفشور پروفیلی سفارشی',
            category__name='جک تنظیم')
        adjust_jack_component.used_count = adjust_jack_count
        adjust_jack_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"جک تنظیم کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"جک تنظیم" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_kafshoor_profile_price'))

    try:
        divider_steel_3_component = custom_product.component_set.get(
            name='ورق استیل 3 میلی متری 304 (برای دیوایدر) کفشور پروفیلی سفارشی',
            category__name='ورق استیل 3 میلی متری 304')
        # used_count = عرض * طول * تعداد دیوایدر
        divider_length = (profile_count * profile_width * 2)
        divider_steel_3_component.used_count = divider_count * divider_length * divider_width
        divider_steel_3_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 3 میلی متری 304 (برای دیوایدر) کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"ورق استیل 3 میلی متری 304" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_kafshoor_profile_price'))

    try:
        divider_laser_gas_profile_component = custom_product.component_set.get(
            name='لیزر و گاز (برای دیوایدر) کفشور پروفیلی سفارشی',
            category__name='لیزر و گاز')
        divider_length = (profile_count * profile_width * 2)
        environment = (divider_length * 2) + (divider_width * 2)
        divider_laser_gas_profile_component.used_count = divider_count * (environment + profile_width * 3)
        divider_laser_gas_profile_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز (برای دیوایدر) کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_kafshoor_profile_price'))

    try:
        screw_30_profile_component = custom_product.component_set.get(
            name='پیچ 3 سانتی کفشور پروفیلی سفارشی',
            category__name='پیچ 3 سانتی')
        screw_30_profile_component.used_count = screw_count
        screw_30_profile_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"پیچ 3 سانتی کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"پیچ 3 سانتی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:custom_kafshoor_profile_price'))

    return custom_product.final_price


def plain_user_custom_kafshoor_profile_total_price(
        request, profile_count, profile_length, profile_width, profile_height,
        adjust_jack_count, divider_count, divider_width, screw_count):
    custom_product = Product.objects.filter(name='کفشور پروفیلی سفارشی')[0]

    try:
        rod_component = custom_product.component_set.get(
            name='ورق استیل پروفیل کفشور پروفیلی سفارشی',
            category__name='ورق استیل پروفیل')
        rod_component.used_count = profile_count * (profile_height + profile_width) * 2 * profile_length
        rod_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل پروفیل کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"ورق استیل پروفیل" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

    try:
        rod_cut_component = custom_product.component_set.get(
            name='برش پروفیل کفشور پروفیلی سفارشی',
            category__name='برش پروفیل')
        rod_cut_component.used_count = profile_count * 2
        rod_cut_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"برش پروفیل کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"برش پروفیل" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

    try:
        adjust_jack_component = custom_product.component_set.get(
            name='جک تنظیم کفشور پروفیلی سفارشی',
            category__name='جک تنظیم')
        adjust_jack_component.used_count = adjust_jack_count
        adjust_jack_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"جک تنظیم کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"جک تنظیم" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

    try:
        divider_steel_3_component = custom_product.component_set.get(
            name='ورق استیل 3 میلی متری (برای دیوایدر) کفشور پروفیلی سفارشی',
            category__name='ورق استیل 3 میلی متری')
        # used_count = عرض * طول * تعداد دیوایدر
        divider_length = (profile_count * profile_width * 2)
        divider_steel_3_component.used_count = divider_count * divider_length * divider_width
        divider_steel_3_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"ورق استیل 3 میلی متری (برای دیوایدر) کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"ورق استیل 3 میلی متری" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

    try:
        divider_laser_gas_profile_component = custom_product.component_set.get(
            name='لیزر و گاز (برای دیوایدر) کفشور پروفیلی سفارشی',
            category__name='لیزر و گاز')
        divider_length = (profile_count * profile_width * 2)
        environment = (divider_length * 2) + (divider_width * 2)
        divider_laser_gas_profile_component.used_count = divider_count * (environment + profile_width * 3)
        divider_laser_gas_profile_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"لیزر و گاز (برای دیوایدر) کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"لیزر و گاز" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

    try:
        screw_30_profile_component = custom_product.component_set.get(
            name='پیچ 3 سانتی کفشور پروفیلی سفارشی',
            category__name='پیچ 3 سانتی')
        screw_30_profile_component.used_count = screw_count
        screw_30_profile_component.save()
    except Component.DoesNotExist:
        messages.error(request, 'لطفا ابتدا یک جزء با نام'
                                '"پیچ 3 سانتی کفشور پروفیلی سفارشی" و با نام دسته بندی '
                                '"پیچ 3 سانتی" برای این محصول ایجاد نمایید.')
        return redirect(reverse('cost:plain_user_custom_kafshoor_profile_price'))

    return custom_product.final_price


def steel_price_per_mm2(length, width, weight, price_per_kilogram):
    total_price = weight * price_per_kilogram
    area_mm2 = width * length
    result = float(total_price / area_mm2)
    return result


def steel_total_area(upside_piece, downside_piece, length, width, height,
                     up_down_length_difference, up_down_height_difference):
    total_area = 0
    if not upside_piece and not downside_piece:
        return 0
    if downside_piece:
        area_of_square = (length + (2 * height)) * (width + (2 * height))
        total_area += area_of_square
    if upside_piece:
        length_up = length - up_down_length_difference
        width_up = width - up_down_length_difference
        height_up = height - up_down_height_difference

        total_area += (length_up + (2 * height_up)) * (width_up + (2 * height_up))

    return total_area


def laser_gas_total_length(
        upside_piece, downside_piece, length, width, height,
        circle_diameter, up_down_length_difference, up_down_height_difference,
        screw_count, glue_groove_count, glue_groove_len, additional_length):
    total_length = 0
    if not upside_piece and not downside_piece:
        return 0
    if downside_piece:
        total_length += 2 * (length + width + (4 * height))
        total_length += circle_diameter * 3.1415926
    if upside_piece:
        length_up = length - up_down_length_difference
        width_up = width - up_down_length_difference
        height_up = height - up_down_height_difference
        total_length += 2 * (length_up + width_up + (4 * height_up))

        total_length += screw_count * (6 * 3.1415926)

        total_length += glue_groove_count * ((2 * glue_groove_len) + 6 + (2 * 3.1415926))

    if additional_length:
        total_length += additional_length

    return total_length


def laser_gas_total_length_v2(length, width, height, screw_count,
                              glue_groove_count, glue_groove_len):
    total_length = 0
    total_length += 2 * (length + width + (4 * height))
    total_length += screw_count * (6 * 3.1415926)
    total_length += glue_groove_count * ((2 * glue_groove_len) + 6 + (2 * 3.1415926))
    return total_length


def grill_length(kind, length, width, up_down_length_difference):
    length = length - up_down_length_difference
    width = width - up_down_length_difference
    grill_len = 0

    if kind == 'point_grill':
        x = int((length - 16) / 7)
        x = x - 1 if x % 2 == 0 else x
        x = int(x / 2) + 1
        y = int((width - 16) / 7)
        y = y - 1 if y % 2 == 0 else y
        y = int(y / 2) + 1
        count = x * y
        grill_len = count * 28

    elif kind == 'line_grill':
        x = math.ceil(length / 10) / 2
        x = math.ceil(x)
        y = int((width - 20) / 50)
        count = x * y
        grill_len = count * 110

    return grill_len
