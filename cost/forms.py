from django import forms

from .models import (
    ComponentCategory, Product, Component, ComponentConstant, CurrentExpense
)


class CustomProductPrice(forms.Form):
    CHOICES_KAFSHOOR = [
        ('ceramic', 'سرامیک خور'),
        ('stone', 'سنگ خور'),
        ('full_steel', 'فول استیل'),
        ('line_grill', 'گریل خطی'),
        ('point_grill', 'گریل نقطه ای'),
    ]
    CHOICES_STEEL_KIND = [
        ('304', 'ورق استیل 304'),
        ('316', 'ورق استیل 316'),
    ]
    CHOICES_STEEL_THICKNESS = [
        ('15', '1.5 میلی متر'),
        ('30', '3 میلی متر'),
    ]

    upside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت رویی دارد؟')
    downside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت زیرین دارد؟')
    kind = forms.ChoiceField(choices=CHOICES_KAFSHOOR, label='نوع کفشور ')
    steel_kind = forms.ChoiceField(initial='304', choices=CHOICES_STEEL_KIND, label='نوع ورق استیل ')
    steel_thickness = forms.ChoiceField(initial='15', choices=CHOICES_STEEL_THICKNESS, label='ضخامت ورق استیل ')
    length = forms.IntegerField(label='طول (به میلی متر) ')
    width = forms.IntegerField(label='عرض (به میلی متر) ')
    height = forms.IntegerField(label='عمق (به میلی متر) ')
    pipe_height = forms.IntegerField(
        initial=30,
        label='طول لوله (به میلی متر) ')
    up_down_length_difference = forms.IntegerField(
        initial=12,
        label='اختلاف طول قسمت رویی و زیرین (به میلی متر) ')
    up_down_height_difference = forms.IntegerField(
        initial=8,
        label='اختلاف عمق قسمت رویی و زیرین (به میلی متر) ')

    circle_diameter = forms.IntegerField(
        initial=23,
        label='قطر دایره وسط قسمت زیرین (به میلی متر) ')
    screw_count = forms.IntegerField(
        initial=4,
        label='تعداد پیچ استفاده شده ')
    dome_count = forms.IntegerField(
        initial=8,
        label='تعداد نکی ')
    glue_groove_count = forms.IntegerField(
        initial=1,
        label='تعداد شیار چسب قسمت رویی ')
    glue_groove_len = forms.IntegerField(
        initial=31,
        label='طول شیار چسب قسمت رویی (به میلی متر) ')
    additional_length = forms.IntegerField(
        initial=0,
        required=False,
        label='طول اضافه لیزر و گاز (برای لوگو و نوشته ها) (به میلی متر) ')
    profit_percent = forms.IntegerField(
        initial=0,
        label='سود این محصول (به درصد) ')
    factor = forms.FloatField(
        initial=1,
        label='ضریب (برای کفشور های Curve) ')


class CustomMultiLatPrice(forms.Form):
    kafshoor_count = forms.IntegerField(label='تعداد کفشور ')
    length = forms.IntegerField(label='طول هرکدام از کفشورها (به میلی متر) ')
    width = forms.IntegerField(label='عرض هرکدام از کفشورها (به میلی متر) ')
    height = forms.IntegerField(label='عمق هرکدام از کفشورها (به میلی متر) ')
    glue_groove_count = forms.IntegerField(label='تعداد شیار هر کفشور ')
    glue_groove_len = forms.IntegerField(
        initial=31,
        label='طول هر شیار (به میلی متر) ')
    screw_count = forms.IntegerField(label='تعداد پیچ هر کفشور ')
    divider_count = forms.IntegerField(label='تعداد دیوایدر ')
    divider_width = forms.IntegerField(label='عرض دیوایدر (به میلی متر) ')
    z_branch_length = forms.IntegerField(label='طول شاخه Z (به میلی متر) ')
    z_branch_width = forms.IntegerField(label='عرض شاخه Z (به میلی متر) ')
    l_pin_count = forms.IntegerField(label='تعداد کل L Pin ها ')
    u_divider_count = forms.IntegerField(
        initial=0,
        label='تعداد دیوایدر U ')
    u_divider_length = forms.IntegerField(
        initial=0,
        label='طول دیوایدر U (به میلی متر) ')
    u_divider_width = forms.IntegerField(
        initial=0,
        label='عرض دیوایدر U (به میلی متر) ')
    u_divider_height = forms.IntegerField(
        initial=0,
        label='عمق دیوایدر U (به میلی متر) ')
    profit_percent = forms.IntegerField(
        initial=0,
        label='سود این محصول (به درصد) ')
    factor = forms.FloatField(
        initial=1,
        label='ضریب (برای کفشور های Curve) ')


class CustomKafshoorProfilePrice(forms.Form):
    profile_count = forms.IntegerField(label='تعداد پروفیل ')
    profile_length = forms.IntegerField(label='طول هرکدام از پروفیل ها (به میلی متر) ')
    profile_width = forms.IntegerField(
        initial=10,
        label='عرض هرکدام از پروفیل ها (به میلی متر) ')
    profile_height = forms.IntegerField(
        initial=10,
        label='عمق هرکدام از پروفیل ها (به میلی متر) ')
    adjust_jack_count = forms.IntegerField(label='تعداد جک تنظیم ')
    divider_count = forms.IntegerField(label='تعداد دیوایدر ')
    divider_width = forms.IntegerField(label='عرض دیوایدر (به میلی متر) ')
    screw_count = forms.IntegerField(label='تعداد پیچ ')
    profit_percent = forms.IntegerField(
        initial=0,
        label='سود این محصول (به درصد) ')
    factor = forms.FloatField(
        initial=1,
        label='ضریب (برای کفشورهای پروفیلی Curve) ')


class SteelUnitPrice(forms.Form):
    length = forms.IntegerField(label='طول (به میلی متر) ')
    width = forms.IntegerField(label='عرض (به میلی متر) ')
    weight = forms.IntegerField(label='وزن (به کیلوگرم) ')
    price_per_kilogram = forms.IntegerField(
        label='قیمت (به ازای هر کیلوگرم) (به تومان) ')


class SteelArea(forms.Form):
    upside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت رویی دارد؟')
    downside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت زیرین دارد؟')
    length = forms.IntegerField(label='طول (به میلی متر) ')
    width = forms.IntegerField(label='عرض (به میلی متر) ')
    height = forms.IntegerField(label='عمق (به میلی متر) ')
    up_down_length_difference = forms.IntegerField(
        initial=12,
        label='اختلاف طول قسمت رویی و زیرین (به میلی متر) ')
    up_down_height_difference = forms.IntegerField(
        initial=8,
        label='اختلاف عمق قسمت رویی و زیرین (به میلی متر) ')


class PipePrice(forms.Form):
    length = forms.IntegerField(label='طول (به میلی متر) ')
    price = forms.IntegerField(label='قیمت (به تومان) ')


class DomePrice(forms.Form):
    count = forms.IntegerField(label='تعداد نکی در ساعت ')
    price = forms.IntegerField(label='قیمت هر ساعت دستگاه نکی (به تومان) ')


class BenderPrice(forms.Form):
    count = forms.IntegerField(label='تعداد خم در ساعت ')
    price = forms.IntegerField(label='قیمت هر ساعت دستگاه خم کننده (به تومان) ')


class LaserGasLength(forms.Form):
    upside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت رویی دارد؟')
    downside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت زیرین دارد؟')
    length = forms.IntegerField(label='طول کفشور (به میلی متر) ')
    width = forms.IntegerField(label='عرض کفشور (به میلی متر) ')
    height = forms.IntegerField(label='عمق کفشور (به میلی متر) ')
    circle_diameter = forms.IntegerField(
        initial=23,
        label='قطر دایره وسط قسمت زیرین (به میلی متر) ')
    up_down_length_difference = forms.IntegerField(
        initial=12,
        label='اختلاف طول قسمت رویی و زیرین (به میلی متر) ')
    up_down_height_difference = forms.IntegerField(
        initial=8,
        label='اختلاف عمق قسمت رویی و زیرین (به میلی متر) ')
    screw_count = forms.IntegerField(
        initial=4,
        label='تعداد پیچ استفاده شده ')
    glue_groove_count = forms.IntegerField(
        initial=1,
        label='تعداد شیار چسب قسمت رویی ')
    glue_groove_len = forms.IntegerField(
        initial=31,
        label='طول شیار چسب قسمت رویی (به میلی متر) ')
    additional_length = forms.IntegerField(
        initial=0,
        required=False,
        label='طول اضافه لیزر و گاز (برای لوگو و نوشته ها) (به میلی متر) ')


class PointGrillPrice(forms.Form):
    length = forms.IntegerField(label='طول نقطه گریل (به میلی متر) ')


class LineGrillPrice(forms.Form):
    length = forms.IntegerField(label='طول خط گریل (به میلی متر) ')
    width = forms.IntegerField(label='عرض خط گریل (به میلی متر) ')


class FullSteelArea(forms.Form):
    upside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت رویی دارد؟')
    downside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت زیرین دارد؟')
    length = forms.IntegerField(label='طول (به میلی متر) ')
    width = forms.IntegerField(label='عرض (به میلی متر) ')
    height = forms.IntegerField(label='عمق (به میلی متر) ')
    up_down_length_difference = forms.IntegerField(
        initial=5,
        label='اختلاف طول قسمت رویی و زیرین (به میلی متر) ')
    up_down_height_difference = forms.IntegerField(
        initial=2,
        label='اختلاف عمق قسمت رویی و زیرین (به میلی متر) ')


class ComponentCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ComponentCategory
        fields = ['name', 'price', 'description']

    def clean(self):
        name = self.cleaned_data.get('name')
        name_exists = ComponentCategory.objects.filter(name=name).exists()
        if name_exists:
            raise forms.ValidationError('این نام در بین اجزا موجود می باشد!')


class ComponentCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ComponentCategory
        fields = ['id', 'name', 'price', 'description']


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'product_image', 'no_prod_per_year',
            'components_cost', 'current_expense', 'profit_percent',
            'final_price',
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        name_exists = Product.objects.filter(name=name).exists()
        if name_exists:
            raise forms.ValidationError('این نام در بین محصولات موجود می باشد!')


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'product_image', 'no_prod_per_year',
            'components_cost', 'current_expense', 'profit_percent',
            'final_price',
        ]


class ComponentCreateForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'category', 'product', 'name', 'description',
            'component_image', 'used_count', 'per_product'
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        name_exists = Product.objects.filter(name=name).exists()
        if name_exists:
            raise forms.ValidationError('این نام در بین اجزا موجود می باشد!')


class ComponentUpdateForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'category', 'product', 'name', 'description',
            'component_image', 'used_count', 'per_product'
        ]


class ComponentConstantCreateForm(forms.ModelForm):
    class Meta:
        model = ComponentConstant
        fields = [
            'name', 'description', 'component_constant_image',
            'product', 'price', 'per_product',
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        name_exists = Product.objects.filter(name=name).exists()
        if name_exists:
            raise forms.ValidationError('این نام در بین اجزای ثابت موجود می باشد!')


class ComponentConstantUpdateForm(forms.ModelForm):
    class Meta:
        model = ComponentConstant
        fields = [
            'name', 'description', 'component_constant_image',
            'product', 'price', 'per_product',
        ]


class CurrentExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = CurrentExpense
        fields = [
            'name', 'cost_in_a_year',
        ]

    def clean(self):
        name = self.cleaned_data.get('name')
        name_exists = Product.objects.filter(name=name).exists()
        if name_exists:
            raise forms.ValidationError('این نام در بین هزینه های جاری موجود می باشد!')


class CurrentExpenseUpdateForm(forms.ModelForm):
    class Meta:
        model = CurrentExpense
        fields = [
            'name', 'cost_in_a_year',
        ]


class PlainUserCustomProductPrice(forms.Form):
    CHOICES = [('ceramic', 'سرامیک خور'),
               ('stone', 'سنگ خور'),
               ('full_steel', 'فول استیل'),
               ('line_grill', 'گریل خطی'),
               ('point_grill', 'گریل نقطه ای'),
               ]

    upside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت رویی دارد؟')
    downside_piece = forms.BooleanField(
        initial=True,
        required=False, label='قسمت زیرین دارد؟')
    kind = forms.ChoiceField(choices=CHOICES, label='نوع کفشور ')
    length = forms.IntegerField(label='طول (به میلی متر) ')
    width = forms.IntegerField(label='عرض (به میلی متر) ')
    height = forms.IntegerField(label='عمق (به میلی متر) ')
    pipe_height = forms.IntegerField(
        initial=30,
        label='طول لوله (به میلی متر) ')
    up_down_length_difference = forms.IntegerField(
        initial=12,
        label='اختلاف طول قسمت رویی و زیرین (به میلی متر) ')
    up_down_height_difference = forms.IntegerField(
        initial=8,
        label='اختلاف عمق قسمت رویی و زیرین (به میلی متر) ')

    circle_diameter = forms.IntegerField(
        initial=23,
        label='قطر دایره وسط قسمت زیرین (به میلی متر) ')
    screw_count = forms.IntegerField(
        initial=4,
        label='تعداد پیچ استفاده شده ')
    dome_count = forms.IntegerField(
        initial=12,
        label='تعداد نکی ')
    glue_groove_count = forms.IntegerField(
        initial=1,
        label='تعداد شیار چسب قسمت رویی ')
    glue_groove_len = forms.IntegerField(
        initial=31,
        label='طول شیار چسب قسمت رویی (به میلی متر) ')
    additional_length = forms.IntegerField(
        initial=0,
        required=False,
        label='طول اضافه لیزر و گاز (برای لوگو و نوشته ها) (به میلی متر) ')
    factor = forms.FloatField(
        initial=1,
        label='ضریب (برای کفشور های Curve) ')


class PlainUserCustomMultiLatPrice(forms.Form):
    kafshoor_count = forms.IntegerField(label='تعداد کفشور ')
    length = forms.IntegerField(label='طول هرکدام از کفشورها (به میلی متر) ')
    width = forms.IntegerField(label='عرض هرکدام از کفشورها (به میلی متر) ')
    height = forms.IntegerField(label='عمق هرکدام از کفشورها (به میلی متر) ')
    glue_groove_count = forms.IntegerField(label='تعداد شیار هر کفشور ')
    glue_groove_len = forms.IntegerField(
        initial=31,
        label='طول هر شیار (به میلی متر) ')
    screw_count = forms.IntegerField(label='تعداد پیچ هر کفشور ')
    divider_count = forms.IntegerField(label='تعداد دیوایدر ')
    divider_width = forms.IntegerField(label='عرض دیوایدر (به میلی متر) ')
    z_branch_length = forms.IntegerField(label='طول شاخه Z (به میلی متر) ')
    z_branch_width = forms.IntegerField(label='عرض شاخه Z (به میلی متر) ')
    l_pin_count = forms.IntegerField(label='تعداد کل L Pin ها ')
    u_divider_count = forms.IntegerField(
        initial=0,
        label='تعداد دیوایدر U ')
    u_divider_length = forms.IntegerField(
        initial=0,
        label='طول دیوایدر U (به میلی متر) ')
    u_divider_width = forms.IntegerField(
        initial=0,
        label='عرض دیوایدر U (به میلی متر) ')
    u_divider_height = forms.IntegerField(
        initial=0,
        label='عمق دیوایدر U (به میلی متر) ')
    factor = forms.FloatField(
        initial=1,
        label='ضریب (برای کفشور های Curve) ')


class PlainUserCustomProfilePrice(forms.Form):
    profile_count = forms.IntegerField(label='تعداد پروفیل ')
    profile_length = forms.IntegerField(label='طول هرکدام از پروفیل ها (به میلی متر) ')
    profile_width = forms.IntegerField(
        initial=10,
        label='عرض هرکدام از پروفیل ها (به میلی متر) ')
    profile_height = forms.IntegerField(
        initial=10,
        label='عمق هرکدام از پروفیل ها (به میلی متر) ')
    adjust_jack_count = forms.IntegerField(label='تعداد جک تنظیم ')
    divider_count = forms.IntegerField(label='تعداد دیوایدر ')
    divider_width = forms.IntegerField(label='عرض دیوایدر ')
    screw_count = forms.IntegerField(label='تعداد پیچ ')
    factor = forms.FloatField(
        initial=1,
        label='ضریب (برای کفشورهای پروفیلی Curve) ')
