from django.db import connection
from django.shortcuts import get_object_or_404

from cost.models import (
    ComponentCategory, Product, Component, ComponentConstant, CurrentExpense
)


def create_everything():
    print('Started ... ')

    # Create ComponentCategory
    component_category_steel_304_15 = ComponentCategory.objects.get_or_create(
        id=1, name="ورق استیل 1.5 میلی متری 304", price=1.62, description=''
    )
    component_category_steel_304_30 = ComponentCategory.objects.get_or_create(
        id=2, name="ورق استیل 3 میلی متری 304", price=3.24, description=''
    )
    component_category_steel_316_15 = ComponentCategory.objects.get_or_create(
        id=3, name="ورق استیل 1.5 میلی متری 316", price=2, description=''
    )
    component_category_steel_316_30 = ComponentCategory.objects.get_or_create(
        id=4, name="ورق استیل 3 میلی متری 316", price=4, description=''
    )
    component_category_flappy = ComponentCategory.objects.get_or_create(
        id=5, name="فلاپی", price=25000, description=''
    )
    component_category_pipe_100_mil = ComponentCategory.objects.get_or_create(
        id=6, name="لوله 10 سانتی متری", price=217, description=''
    )
    component_category_pipe_75_mil = ComponentCategory.objects.get_or_create(
        id=7, name="لوله 7/5 سانتی متری", price=217, description=''
    )
    component_category_pipe_51_mil = ComponentCategory.objects.get_or_create(
        id=8, name="لوله 51 میلی متری", price=217, description=''
    )
    component_category_pipe_42_mil = ComponentCategory.objects.get_or_create(
        id=9, name="لوله 42 میلی متری", price=217, description=''
    )
    component_category_pipe_32_mil = ComponentCategory.objects.get_or_create(
        id=10, name="لوله 32 میلی متری", price=217, description=''
    )
    component_category_pipe_25_mil = ComponentCategory.objects.get_or_create(
        id=11, name="لوله 25 میلی متری", price=116, description=''
    )
    component_category_pipe_cutting = ComponentCategory.objects.get_or_create(
        id=12, name="برش لوله", price=2000, description=''
    )
    component_category_laser_gas = ComponentCategory.objects.get_or_create(
        id=13, name="لیزر و گاز", price=4.5, description=''
    )
    component_category_dome = ComponentCategory.objects.get_or_create(
        id=14, name="نکی", price=524, description=''
    )
    component_category_screw_15 = ComponentCategory.objects.get_or_create(
        id=15, name="پیچ 1.5 سانتی", price=130, description=''
    )
    component_category_screw_30 = ComponentCategory.objects.get_or_create(
        id=16, name="پیچ 3 سانتی", price=300, description=''
    )
    component_category_fasten = ComponentCategory.objects.get_or_create(
        id=17, name="بست", price=3284, description=''
    )
    component_category_bend = ComponentCategory.objects.get_or_create(
        id=18, name="خم", price=765, description=''
    )
    component_category_spring = ComponentCategory.objects.get_or_create(
        id=19, name="فنر", price=2000, description=''
    )
    component_category_key = ComponentCategory.objects.get_or_create(
        id=20, name="کلید", price=2000, description=''
    )
    component_category_weld = ComponentCategory.objects.get_or_create(
        id=21, name="جوش", price=12000, description=''
    )
    component_category_reamer = ComponentCategory.objects.get_or_create(
        id=22, name="قلاویز", price=200, description=''
    )
    component_category_electropolish = ComponentCategory.objects.get_or_create(
        id=23, name="الکتروپلیش", price=1000, description=''
    )
    component_category_press = ComponentCategory.objects.get_or_create(
        id=24, name="پرس", price=3500, description=''
    )
    component_category_paper = ComponentCategory.objects.get_or_create(
        id=25, name="کاغذ تبلیغ", price=500, description=''
    )
    component_category_grill_point = ComponentCategory.objects.get_or_create(
        id=26, name="گریل نقطه ای", price=126, description=''
    )
    component_category_grill_line = ComponentCategory.objects.get_or_create(
        id=27, name="گریل خطی", price=513, description=''
    )
    component_category_l_pin = ComponentCategory.objects.get_or_create(
        id=28, name="ال پین", price=2000, description=''
    )
    component_category_profile = ComponentCategory.objects.get_or_create(
        id=29, name="ورق استیل پروفیل", price=1.525, description=''
    )
    component_category_profile_cut = ComponentCategory.objects.get_or_create(
        id=30, name="برش پروفیل", price=500, description=''
    )
    component_category_adjust_jack = ComponentCategory.objects.get_or_create(
        id=31, name="جک تنظیم", price=5000, description=''
    )

    # =================================================================================
    # Kafshoor Custom
    # =================================================================================

    # Delete Product Kafshoor Custom
    product_kafshoor_custom_to_delete = Product.objects.filter(
        id=1, name="کفشور سفارشی",
    )
    if len(product_kafshoor_custom_to_delete) > 0:
        product_kafshoor_custom_to_delete[0].delete()

    # Create Product Kafshoor Custom
    product_kafshoor_custom = Product.objects.get_or_create(
        id=1, name="کفشور سفارشی", description='', no_prod_per_year=1,
    )

    # Create Components for Kafshoor Custom
    component_kafshoor_custom_steel_304_15 = Component.objects.get_or_create(
        id=1, category=component_category_steel_304_15[0], product=product_kafshoor_custom[0],
        name="ورق استیل 1.5 میلی متری 304 کفشور سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_custom_steel_304_30 = Component.objects.get_or_create(
        id=2, category=component_category_steel_304_30[0], product=product_kafshoor_custom[0],
        name="ورق استیل 3 میلی متری 304 کفشور سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_custom_steel_316_15 = Component.objects.get_or_create(
        id=3, category=component_category_steel_316_15[0], product=product_kafshoor_custom[0],
        name="ورق استیل 1.5 میلی متری 316 کفشور سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_custom_steel_316_30 = Component.objects.get_or_create(
        id=4, category=component_category_steel_316_30[0], product=product_kafshoor_custom[0],
        name="ورق استیل 3 میلی متری 316 کفشور سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_custom_flappy = Component.objects.get_or_create(
        id=5, category=component_category_flappy[0], product=product_kafshoor_custom[0],
        name="فلاپی کفشور سفارشی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_custom_pipe = Component.objects.get_or_create(
        id=6, category=component_category_pipe_51_mil[0], product=product_kafshoor_custom[0],
        name="لوله کفشور سفارشی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_custom_pipe_cutting = Component.objects.get_or_create(
        id=7, category=component_category_pipe_cutting[0], product=product_kafshoor_custom[0],
        name="برش لوله کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_laser_gas = Component.objects.get_or_create(
        id=8, category=component_category_laser_gas[0], product=product_kafshoor_custom[0],
        name="لیزر و گاز کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_dome = Component.objects.get_or_create(
        id=9, category=component_category_dome[0], product=product_kafshoor_custom[0],
        name="نکی کفشور سفارشی", description='', used_count=12,
        per_product=1
    )
    component_kafshoor_custom_screw_15 = Component.objects.get_or_create(
        id=10, category=component_category_screw_15[0], product=product_kafshoor_custom[0],
        name="پیچ 1.5 سانتی کفشور سفارشی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_custom_bend = Component.objects.get_or_create(
        id=11, category=component_category_bend[0], product=product_kafshoor_custom[0],
        name="خم کفشور سفارشی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_custom_spring = Component.objects.get_or_create(
        id=12, category=component_category_spring[0], product=product_kafshoor_custom[0],
        name="فنر کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_key = Component.objects.get_or_create(
        id=13, category=component_category_key[0], product=product_kafshoor_custom[0],
        name="کلید کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_weld = Component.objects.get_or_create(
        id=14, category=component_category_weld[0], product=product_kafshoor_custom[0],
        name="جوش کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_reamer = Component.objects.get_or_create(
        id=15, category=component_category_reamer[0], product=product_kafshoor_custom[0],
        name="قلاویز کفشور سفارشی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_custom_electropolish = Component.objects.get_or_create(
        id=16, category=component_category_electropolish[0], product=product_kafshoor_custom[0],
        name="الکتروپلیش کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_press = Component.objects.get_or_create(
        id=17, category=component_category_press[0], product=product_kafshoor_custom[0],
        name="پرس کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_paper = Component.objects.get_or_create(
        id=18, category=component_category_paper[0], product=product_kafshoor_custom[0],
        name="کاغذ تبلیغ کفشور سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_custom_grill = Component.objects.get_or_create(
        id=19, category=component_category_laser_gas[0], product=product_kafshoor_custom[0],
        name="گریل کفشور سفارشی", description='', used_count=1,
        per_product=1
    )

    # =================================================================================
    # Kafshoor Multi Lat Custom
    # =================================================================================

    # Delete Product Kafshoor Multi Lat Custom
    product_kafshoor_multi_lat_custom_to_delete = Product.objects.filter(
        id=2, name="کفشور چند لتی سفارشی"
    )
    if len(product_kafshoor_multi_lat_custom_to_delete) > 0:
        product_kafshoor_multi_lat_custom_to_delete[0].delete()

    # Create Product Kafshoor Multi Lat Custom
    product_kafshoor_multi_lat_custom = Product.objects.get_or_create(
        id=2, name="کفشور چند لتی سفارشی", description='', no_prod_per_year=1,
    )

    # Create Components for Kafshoor Multi Lat Custom
    component_kafshoor_multi_lat_custom_steel_15 = Component.objects.get_or_create(
        id=21, category=component_category_steel_304_15[0], product=product_kafshoor_multi_lat_custom[0],
        name="ورق استیل 1.5 میلی متری 304 کفشور چند لتی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_flappy = Component.objects.get_or_create(
        id=22, category=component_category_flappy[0], product=product_kafshoor_multi_lat_custom[0],
        name="فلاپی کفشور چند لتی سفارشی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_multi_lat_custom_laser_gas = Component.objects.get_or_create(
        id=23, category=component_category_laser_gas[0], product=product_kafshoor_multi_lat_custom[0],
        name="لیزر و گاز کفشور چند لتی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_screw_15 = Component.objects.get_or_create(
        id=24, category=component_category_screw_15[0], product=product_kafshoor_multi_lat_custom[0],
        name="پیچ 1.5 سانتی کفشور چند لتی سفارشی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_bend = Component.objects.get_or_create(
        id=25, category=component_category_bend[0], product=product_kafshoor_multi_lat_custom[0],
        name="خم کفشور چند لتی سفارشی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_weld = Component.objects.get_or_create(
        id=26, category=component_category_weld[0], product=product_kafshoor_multi_lat_custom[0],
        name="جوش کفشور چند لتی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_reamer = Component.objects.get_or_create(
        id=27, category=component_category_reamer[0], product=product_kafshoor_multi_lat_custom[0],
        name="قلاویز کفشور چند لتی سفارشی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_paper = Component.objects.get_or_create(
        id=28, category=component_category_paper[0], product=product_kafshoor_multi_lat_custom[0],
        name="کاغذ تبلیغ کفشور چند لتی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_steel_30_divider = Component.objects.get_or_create(
        id=29, category=component_category_steel_304_30[0], product=product_kafshoor_multi_lat_custom[0],
        name="ورق استیل 3 میلی متری 304 (برای دیوایدر) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_laser_gas_divider = Component.objects.get_or_create(
        id=30, category=component_category_laser_gas[0], product=product_kafshoor_multi_lat_custom[0],
        name="لیزر و گاز (برای دیوایدر) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_steel_15_z_branch = Component.objects.get_or_create(
        id=31, category=component_category_steel_304_15[0], product=product_kafshoor_multi_lat_custom[0],
        name="ورق استیل 1.5 میلی متری 304 (برای شاخه Z) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_l_pin = Component.objects.get_or_create(
        id=32, category=component_category_l_pin[0], product=product_kafshoor_multi_lat_custom[0],
        name="ال پین (برای شاخه Z) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_bend = Component.objects.get_or_create(
        id=33, category=component_category_bend[0], product=product_kafshoor_multi_lat_custom[0],
        name="خم (برای شاخه Z) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_laser_gas_z_branch = Component.objects.get_or_create(
        id=34, category=component_category_laser_gas[0], product=product_kafshoor_multi_lat_custom[0],
        name="لیزر و گاز (برای شاخه Z) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_steel_30_u_divider = Component.objects.get_or_create(
        id=35, category=component_category_steel_304_30[0], product=product_kafshoor_multi_lat_custom[0],
        name="ورق استیل 3 میلی متری 304 (برای دیوایدر U) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_kafshoor_multi_lat_custom_laser_gas_u_divider = Component.objects.get_or_create(
        id=36, category=component_category_laser_gas[0], product=product_kafshoor_multi_lat_custom[0],
        name="لیزر و گاز (برای دیوایدر U) کفشور چند لتی سفارشی", description='', used_count=0,
        per_product=1
    )

    # =================================================================================
    # Kafshoor Profile Custom
    # =================================================================================

    # Delete Product Kafshoor Profile Custom
    product_kafshoor_profile_custom_to_delete = Product.objects.filter(
        id=3, name="کفشور پروفیلی سفارشی"
    )
    if len(product_kafshoor_profile_custom_to_delete) > 0:
        product_kafshoor_profile_custom_to_delete[0].delete()

    # Create Product Kafshoor Profile Custom
    product_kafshoor_profile_custom = Product.objects.get_or_create(
        id=3, name="کفشور پروفیلی سفارشی", description='', no_prod_per_year=1,
    )

    # Create Components for Profile Custom
    component_profile_rod = Component.objects.get_or_create(
        id=41, category=component_category_profile[0], product=product_kafshoor_profile_custom[0],
        name="ورق استیل پروفیل کفشور پروفیلی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_profile_rod_cut = Component.objects.get_or_create(
        id=42, category=component_category_profile_cut[0], product=product_kafshoor_profile_custom[0],
        name="برش پروفیل کفشور پروفیلی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_profile_adjust_jack = Component.objects.get_or_create(
        id=43, category=component_category_adjust_jack[0], product=product_kafshoor_profile_custom[0],
        name="جک تنظیم کفشور پروفیلی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_profile_adjust_jack = Component.objects.get_or_create(
        id=43, category=component_category_adjust_jack[0], product=product_kafshoor_profile_custom[0],
        name="جک تنظیم کفشور پروفیلی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_profile_custom_steel_30_divider = Component.objects.get_or_create(
        id=44, category=component_category_steel_304_30[0], product=product_kafshoor_profile_custom[0],
        name="ورق استیل 3 میلی متری 304 (برای دیوایدر) کفشور پروفیلی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_profile_custom_laser_gas_divider = Component.objects.get_or_create(
        id=45, category=component_category_laser_gas[0], product=product_kafshoor_profile_custom[0],
        name="لیزر و گاز (برای دیوایدر) کفشور پروفیلی سفارشی", description='', used_count=0,
        per_product=1
    )
    component_profile_custom_screw_15 = Component.objects.get_or_create(
        id=46, category=component_category_screw_30[0], product=product_kafshoor_profile_custom[0],
        name="پیچ 3 سانتی کفشور پروفیلی سفارشی", description='', used_count=1,
        per_product=1
    )
    component_profile_custom_weld = Component.objects.get_or_create(
        id=47, category=component_category_weld[0], product=product_kafshoor_profile_custom[0],
        name="جوش کفشور پروفیلی سفارشی", description='', used_count=1,
        per_product=1
    )

    # =================================================================================
    # Ceramic
    # =================================================================================

    # Create Product Kafshoor Ceramic 10 * 10
    product_kafshoor_ceramic_10_10 = Product.objects.get_or_create(
        id=11, name="کفشور 10 * 10 سرامیک خور", description='', no_prod_per_year=260,
    )

    # Create Components for Kafshoor Ceramic 10 * 10
    component_kafshoor_ceramic_10_10_steel_15 = Component.objects.get_or_create(
        id=101, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_10_10[0],
        name="ورق استیل کفشور 10 * 10 سرامیک خور", description='', used_count=36304,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_flappy = Component.objects.get_or_create(
        id=102, category=component_category_flappy[0], product=product_kafshoor_ceramic_10_10[0],
        name="فلاپی کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_10_10_pipe = Component.objects.get_or_create(
        id=103, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_10_10[0],
        name="لوله کفشور 10 * 10 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_pipe_cutting = Component.objects.get_or_create(
        id=104, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_10_10[0],
        name="برش لوله کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_laser_gas = Component.objects.get_or_create(
        id=105, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_10_10[0],
        name="لیزر و گاز کفشور 10 * 10 سرامیک خور", description='', used_count=1647,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_dome = Component.objects.get_or_create(
        id=106, category=component_category_dome[0], product=product_kafshoor_ceramic_10_10[0],
        name="نکی کفشور 10 * 10 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_screw_15 = Component.objects.get_or_create(
        id=107, category=component_category_screw_15[0], product=product_kafshoor_ceramic_10_10[0],
        name="پیچ 1.5 سانتی کفشور 10 * 10 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_bend = Component.objects.get_or_create(
        id=108, category=component_category_bend[0], product=product_kafshoor_ceramic_10_10[0],
        name="خم کفشور 10 * 10 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_spring = Component.objects.get_or_create(
        id=109, category=component_category_spring[0], product=product_kafshoor_ceramic_10_10[0],
        name="فنر کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_key = Component.objects.get_or_create(
        id=110, category=component_category_key[0], product=product_kafshoor_ceramic_10_10[0],
        name="کلید کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_weld = Component.objects.get_or_create(
        id=111, category=component_category_weld[0], product=product_kafshoor_ceramic_10_10[0],
        name="جوش کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_reamer = Component.objects.get_or_create(
        id=112, category=component_category_reamer[0], product=product_kafshoor_ceramic_10_10[0],
        name="قلاویز کفشور 10 * 10 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_electropolish = Component.objects.get_or_create(
        id=113, category=component_category_electropolish[0], product=product_kafshoor_ceramic_10_10[0],
        name="الکتروپلیش کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_press = Component.objects.get_or_create(
        id=114, category=component_category_press[0], product=product_kafshoor_ceramic_10_10[0],
        name="پرس کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_10_10_paper = Component.objects.get_or_create(
        id=115, category=component_category_paper[0], product=product_kafshoor_ceramic_10_10[0],
        name="کاغذ تبلیغ کفشور 10 * 10 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 12 * 12
    product_kafshoor_ceramic_12_12 = Product.objects.get_or_create(
        id=12, name="کفشور 12 * 12 سرامیک خور", description='', no_prod_per_year=45,
    )

    # Create Components for Kafshoor Ceramic 10 * 10
    component_kafshoor_ceramic_12_12_steel_15 = Component.objects.get_or_create(
        id=121, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_12_12[0],
        name="ورق استیل کفشور 12 * 12 سرامیک خور", description='', used_count=47824,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_flappy = Component.objects.get_or_create(
        id=122, category=component_category_flappy[0], product=product_kafshoor_ceramic_12_12[0],
        name="فلاپی کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_12_12_pipe = Component.objects.get_or_create(
        id=123, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_12_12[0],
        name="لوله کفشور 12 * 12 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_pipe_cutting = Component.objects.get_or_create(
        id=124, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_12_12[0],
        name="برش لوله کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_laser_gas = Component.objects.get_or_create(
        id=125, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_12_12[0],
        name="لیزر و گاز کفشور 12 * 12 سرامیک خور", description='', used_count=1807,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_dome = Component.objects.get_or_create(
        id=126, category=component_category_dome[0], product=product_kafshoor_ceramic_12_12[0],
        name="نکی کفشور 12 * 12 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_screw_15 = Component.objects.get_or_create(
        id=127, category=component_category_screw_15[0], product=product_kafshoor_ceramic_12_12[0],
        name="پیچ 1.5 سانتی کفشور 12 * 12 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_bend = Component.objects.get_or_create(
        id=128, category=component_category_bend[0], product=product_kafshoor_ceramic_12_12[0],
        name="خم کفشور 12 * 12 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_spring = Component.objects.get_or_create(
        id=129, category=component_category_spring[0], product=product_kafshoor_ceramic_12_12[0],
        name="فنر کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_key = Component.objects.get_or_create(
        id=130, category=component_category_key[0], product=product_kafshoor_ceramic_12_12[0],
        name="کلید کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_weld = Component.objects.get_or_create(
        id=131, category=component_category_weld[0], product=product_kafshoor_ceramic_12_12[0],
        name="جوش کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_reamer = Component.objects.get_or_create(
        id=132, category=component_category_reamer[0], product=product_kafshoor_ceramic_12_12[0],
        name="قلاویز کفشور 12 * 12 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_electropolish = Component.objects.get_or_create(
        id=133, category=component_category_electropolish[0], product=product_kafshoor_ceramic_12_12[0],
        name="الکتروپلیش کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_press = Component.objects.get_or_create(
        id=134, category=component_category_press[0], product=product_kafshoor_ceramic_12_12[0],
        name="پرس کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_12_12_paper = Component.objects.get_or_create(
        id=135, category=component_category_paper[0], product=product_kafshoor_ceramic_12_12[0],
        name="کاغذ تبلیغ کفشور 12 * 12 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 15 * 15
    product_kafshoor_ceramic_15_15 = Product.objects.get_or_create(
        id=13, name="کفشور 15 * 15 سرامیک خور", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Ceramic 15 * 15
    component_kafshoor_ceramic_15_15_steel_15 = Component.objects.get_or_create(
        id=141, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_15_15[0],
        name="ورق استیل کفشور 15 * 15 سرامیک خور", description='', used_count=68104,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_flappy = Component.objects.get_or_create(
        id=142, category=component_category_flappy[0], product=product_kafshoor_ceramic_15_15[0],
        name="فلاپی کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_15_15_pipe = Component.objects.get_or_create(
        id=143, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_15_15[0],
        name="لوله کفشور 15 * 15 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_pipe_cutting = Component.objects.get_or_create(
        id=144, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_15_15[0],
        name="برش لوله کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_laser_gas = Component.objects.get_or_create(
        id=145, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_15_15[0],
        name="لیزر و گاز کفشور 15 * 15 سرامیک خور", description='', used_count=2047,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_dome = Component.objects.get_or_create(
        id=146, category=component_category_dome[0], product=product_kafshoor_ceramic_15_15[0],
        name="نکی کفشور 15 * 15 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_screw_15 = Component.objects.get_or_create(
        id=147, category=component_category_screw_15[0], product=product_kafshoor_ceramic_15_15[0],
        name="پیچ 1.5 سانتی کفشور 15 * 15 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_bend = Component.objects.get_or_create(
        id=148, category=component_category_bend[0], product=product_kafshoor_ceramic_15_15[0],
        name="خم کفشور 15 * 15 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_spring = Component.objects.get_or_create(
        id=149, category=component_category_spring[0], product=product_kafshoor_ceramic_15_15[0],
        name="فنر کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_key = Component.objects.get_or_create(
        id=150, category=component_category_key[0], product=product_kafshoor_ceramic_15_15[0],
        name="کلید کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_weld = Component.objects.get_or_create(
        id=151, category=component_category_weld[0], product=product_kafshoor_ceramic_15_15[0],
        name="جوش کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_reamer = Component.objects.get_or_create(
        id=152, category=component_category_reamer[0], product=product_kafshoor_ceramic_15_15[0],
        name="قلاویز کفشور 15 * 15 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_electropolish = Component.objects.get_or_create(
        id=153, category=component_category_electropolish[0], product=product_kafshoor_ceramic_15_15[0],
        name="الکتروپلیش کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_press = Component.objects.get_or_create(
        id=154, category=component_category_press[0], product=product_kafshoor_ceramic_15_15[0],
        name="پرس کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_15_15_paper = Component.objects.get_or_create(
        id=155, category=component_category_paper[0], product=product_kafshoor_ceramic_15_15[0],
        name="کاغذ تبلیغ کفشور 15 * 15 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 17 * 17
    product_kafshoor_ceramic_17_17 = Product.objects.get_or_create(
        id=14, name="کفشور 17 * 17 سرامیک خور", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Ceramic 17 * 17
    component_kafshoor_ceramic_17_17_steel_15 = Component.objects.get_or_create(
        id=161, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_17_17[0],
        name="ورق استیل کفشور 17 * 17 سرامیک خور", description='', used_count=83624,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_flappy = Component.objects.get_or_create(
        id=162, category=component_category_flappy[0], product=product_kafshoor_ceramic_17_17[0],
        name="فلاپی کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_17_17_pipe = Component.objects.get_or_create(
        id=163, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_17_17[0],
        name="لوله کفشور 17 * 17 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_pipe_cutting = Component.objects.get_or_create(
        id=164, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_17_17[0],
        name="برش لوله کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_laser_gas = Component.objects.get_or_create(
        id=165, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_17_17[0],
        name="لیزر و گاز کفشور 17 * 17 سرامیک خور", description='', used_count=2207,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_dome = Component.objects.get_or_create(
        id=166, category=component_category_dome[0], product=product_kafshoor_ceramic_17_17[0],
        name="نکی کفشور 17 * 17 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_screw_15 = Component.objects.get_or_create(
        id=167, category=component_category_screw_15[0], product=product_kafshoor_ceramic_17_17[0],
        name="پیچ 1.5 سانتی کفشور 17 * 17 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_bend = Component.objects.get_or_create(
        id=168, category=component_category_bend[0], product=product_kafshoor_ceramic_17_17[0],
        name="خم کفشور 17 * 17 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_spring = Component.objects.get_or_create(
        id=169, category=component_category_spring[0], product=product_kafshoor_ceramic_17_17[0],
        name="فنر کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_key = Component.objects.get_or_create(
        id=170, category=component_category_key[0], product=product_kafshoor_ceramic_17_17[0],
        name="کلید کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_weld = Component.objects.get_or_create(
        id=171, category=component_category_weld[0], product=product_kafshoor_ceramic_17_17[0],
        name="جوش کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_reamer = Component.objects.get_or_create(
        id=172, category=component_category_reamer[0], product=product_kafshoor_ceramic_17_17[0],
        name="قلاویز کفشور 17 * 17 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_electropolish = Component.objects.get_or_create(
        id=173, category=component_category_electropolish[0], product=product_kafshoor_ceramic_17_17[0],
        name="الکتروپلیش کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_press = Component.objects.get_or_create(
        id=174, category=component_category_press[0], product=product_kafshoor_ceramic_17_17[0],
        name="پرس کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_17_17_paper = Component.objects.get_or_create(
        id=175, category=component_category_paper[0], product=product_kafshoor_ceramic_17_17[0],
        name="کاغذ تبلیغ کفشور 17 * 17 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 20 * 20
    product_kafshoor_ceramic_20_20 = Product.objects.get_or_create(
        id=15, name="کفشور 20 * 20 سرامیک خور", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Ceramic 20 * 20
    component_kafshoor_ceramic_20_20_steel_15 = Component.objects.get_or_create(
        id=181, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_20_20[0],
        name="ورق استیل کفشور 20 * 20 سرامیک خور", description='', used_count=109904,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_flappy = Component.objects.get_or_create(
        id=182, category=component_category_flappy[0], product=product_kafshoor_ceramic_20_20[0],
        name="فلاپی کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_20_20_pipe = Component.objects.get_or_create(
        id=183, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_20_20[0],
        name="لوله کفشور 20 * 20 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_pipe_cutting = Component.objects.get_or_create(
        id=184, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_20_20[0],
        name="برش لوله کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_laser_gas = Component.objects.get_or_create(
        id=185, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_20_20[0],
        name="لیزر و گاز کفشور 20 * 20 سرامیک خور", description='', used_count=2447,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_dome = Component.objects.get_or_create(
        id=186, category=component_category_dome[0], product=product_kafshoor_ceramic_20_20[0],
        name="نکی کفشور 20 * 20 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_screw_15 = Component.objects.get_or_create(
        id=187, category=component_category_screw_15[0], product=product_kafshoor_ceramic_20_20[0],
        name="پیچ 1.5 سانتی کفشور 20 * 20 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_bend = Component.objects.get_or_create(
        id=188, category=component_category_bend[0], product=product_kafshoor_ceramic_20_20[0],
        name="خم کفشور 20 * 20 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_spring = Component.objects.get_or_create(
        id=189, category=component_category_spring[0], product=product_kafshoor_ceramic_20_20[0],
        name="فنر کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_key = Component.objects.get_or_create(
        id=190, category=component_category_key[0], product=product_kafshoor_ceramic_20_20[0],
        name="کلید کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_weld = Component.objects.get_or_create(
        id=191, category=component_category_weld[0], product=product_kafshoor_ceramic_20_20[0],
        name="جوش کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_reamer = Component.objects.get_or_create(
        id=192, category=component_category_reamer[0], product=product_kafshoor_ceramic_20_20[0],
        name="قلاویز کفشور 20 * 20 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_electropolish = Component.objects.get_or_create(
        id=193, category=component_category_electropolish[0], product=product_kafshoor_ceramic_20_20[0],
        name="الکتروپلیش کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_press = Component.objects.get_or_create(
        id=194, category=component_category_press[0], product=product_kafshoor_ceramic_20_20[0],
        name="پرس کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_20_20_paper = Component.objects.get_or_create(
        id=195, category=component_category_paper[0], product=product_kafshoor_ceramic_20_20[0],
        name="کاغذ تبلیغ کفشور 20 * 20 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 30 * 8
    product_kafshoor_ceramic_30_8 = Product.objects.get_or_create(
        id=16, name="کفشور 8 * 30 سرامیک خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Ceramic 30 * 8
    component_kafshoor_ceramic_30_8_steel_15 = Component.objects.get_or_create(
        id=201, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_30_8[0],
        name="ورق استیل کفشور 8 * 30 سرامیک خور", description='', used_count=76544,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_flappy = Component.objects.get_or_create(
        id=202, category=component_category_flappy[0], product=product_kafshoor_ceramic_30_8[0],
        name="فلاپی کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_30_8_pipe = Component.objects.get_or_create(
        id=203, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_30_8[0],
        name="لوله کفشور 8 * 30 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_pipe_cutting = Component.objects.get_or_create(
        id=204, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_30_8[0],
        name="برش لوله کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_laser_gas = Component.objects.get_or_create(
        id=205, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_30_8[0],
        name="لیزر و گاز کفشور 8 * 30 سرامیک خور", description='', used_count=2367,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_dome = Component.objects.get_or_create(
        id=206, category=component_category_dome[0], product=product_kafshoor_ceramic_30_8[0],
        name="نکی کفشور 8 * 30 سرامیک خور", description='', used_count=10,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_screw_15 = Component.objects.get_or_create(
        id=207, category=component_category_screw_15[0], product=product_kafshoor_ceramic_30_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 30 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_screw_30 = Component.objects.get_or_create(
        id=208, category=component_category_screw_30[0], product=product_kafshoor_ceramic_30_8[0],
        name="پیچ 3 سانتی کفشور 8 * 30 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_fasten = Component.objects.get_or_create(
        id=209, category=component_category_fasten[0], product=product_kafshoor_ceramic_30_8[0],
        name="بست کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_bend = Component.objects.get_or_create(
        id=210, category=component_category_bend[0], product=product_kafshoor_ceramic_30_8[0],
        name="خم کفشور 8 * 30 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_spring = Component.objects.get_or_create(
        id=211, category=component_category_spring[0], product=product_kafshoor_ceramic_30_8[0],
        name="فنر کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_key = Component.objects.get_or_create(
        id=212, category=component_category_key[0], product=product_kafshoor_ceramic_30_8[0],
        name="کلید کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_weld = Component.objects.get_or_create(
        id=213, category=component_category_weld[0], product=product_kafshoor_ceramic_30_8[0],
        name="جوش کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_reamer = Component.objects.get_or_create(
        id=214, category=component_category_reamer[0], product=product_kafshoor_ceramic_30_8[0],
        name="قلاویز کفشور 8 * 30 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_electropolish = Component.objects.get_or_create(
        id=215, category=component_category_electropolish[0], product=product_kafshoor_ceramic_30_8[0],
        name="الکتروپلیش کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_press = Component.objects.get_or_create(
        id=216, category=component_category_press[0], product=product_kafshoor_ceramic_30_8[0],
        name="پرس کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_30_8_paper = Component.objects.get_or_create(
        id=217, category=component_category_paper[0], product=product_kafshoor_ceramic_30_8[0],
        name="کاغذ تبلیغ کفشور 8 * 30 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 45 * 8
    product_kafshoor_ceramic_45_8 = Product.objects.get_or_create(
        id=17, name="کفشور 8 * 45 سرامیک خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Ceramic 45 * 8
    component_kafshoor_ceramic_45_8_steel_15 = Component.objects.get_or_create(
        id=221, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_45_8[0],
        name="ورق استیل کفشور 8 * 45 سرامیک خور", description='', used_count=110744,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_flappy = Component.objects.get_or_create(
        id=222, category=component_category_flappy[0], product=product_kafshoor_ceramic_45_8[0],
        name="فلاپی کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_45_8_pipe = Component.objects.get_or_create(
        id=223, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_45_8[0],
        name="لوله کفشور 8 * 45 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_pipe_cutting = Component.objects.get_or_create(
        id=224, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_45_8[0],
        name="برش لوله کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_laser_gas = Component.objects.get_or_create(
        id=225, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_45_8[0],
        name="لیزر و گاز کفشور 8 * 45 سرامیک خور", description='', used_count=2967,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_dome = Component.objects.get_or_create(
        id=226, category=component_category_dome[0], product=product_kafshoor_ceramic_45_8[0],
        name="نکی کفشور 8 * 45 سرامیک خور", description='', used_count=14,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_screw_15 = Component.objects.get_or_create(
        id=227, category=component_category_screw_15[0], product=product_kafshoor_ceramic_45_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 45 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_screw_30 = Component.objects.get_or_create(
        id=228, category=component_category_screw_30[0], product=product_kafshoor_ceramic_45_8[0],
        name="پیچ 3 سانتی کفشور 8 * 45 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_fasten = Component.objects.get_or_create(
        id=229, category=component_category_fasten[0], product=product_kafshoor_ceramic_45_8[0],
        name="بست کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_bend = Component.objects.get_or_create(
        id=230, category=component_category_bend[0], product=product_kafshoor_ceramic_45_8[0],
        name="خم کفشور 8 * 45 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_spring = Component.objects.get_or_create(
        id=231, category=component_category_spring[0], product=product_kafshoor_ceramic_45_8[0],
        name="فنر کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_key = Component.objects.get_or_create(
        id=232, category=component_category_key[0], product=product_kafshoor_ceramic_45_8[0],
        name="کلید کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_weld = Component.objects.get_or_create(
        id=233, category=component_category_weld[0], product=product_kafshoor_ceramic_45_8[0],
        name="جوش کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_reamer = Component.objects.get_or_create(
        id=234, category=component_category_reamer[0], product=product_kafshoor_ceramic_45_8[0],
        name="قلاویز کفشور 8 * 45 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_electropolish = Component.objects.get_or_create(
        id=235, category=component_category_electropolish[0], product=product_kafshoor_ceramic_45_8[0],
        name="الکتروپلیش کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_press = Component.objects.get_or_create(
        id=236, category=component_category_press[0], product=product_kafshoor_ceramic_45_8[0],
        name="پرس کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_45_8_paper = Component.objects.get_or_create(
        id=237, category=component_category_paper[0], product=product_kafshoor_ceramic_45_8[0],
        name="کاغذ تبلیغ کفشور 8 * 45 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 60 * 8
    product_kafshoor_ceramic_60_8 = Product.objects.get_or_create(
        id=18, name="کفشور 8 * 60 سرامیک خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Ceramic 60 * 8
    component_kafshoor_ceramic_60_8_steel_15 = Component.objects.get_or_create(
        id=241, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_60_8[0],
        name="ورق استیل کفشور 8 * 60 سرامیک خور", description='', used_count=144944,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_flappy = Component.objects.get_or_create(
        id=242, category=component_category_flappy[0], product=product_kafshoor_ceramic_60_8[0],
        name="فلاپی کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_60_8_pipe = Component.objects.get_or_create(
        id=243, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_60_8[0],
        name="لوله کفشور 8 * 60 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_pipe_cutting = Component.objects.get_or_create(
        id=244, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_60_8[0],
        name="برش لوله کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_laser_gas = Component.objects.get_or_create(
        id=245, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_60_8[0],
        name="لیزر و گاز کفشور 8 * 60 سرامیک خور", description='', used_count=3567,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_dome = Component.objects.get_or_create(
        id=246, category=component_category_dome[0], product=product_kafshoor_ceramic_60_8[0],
        name="نکی کفشور 8 * 60 سرامیک خور", description='', used_count=14,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_screw_15 = Component.objects.get_or_create(
        id=247, category=component_category_screw_15[0], product=product_kafshoor_ceramic_60_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 60 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_screw_30 = Component.objects.get_or_create(
        id=248, category=component_category_screw_30[0], product=product_kafshoor_ceramic_60_8[0],
        name="پیچ 3 سانتی کفشور 8 * 60 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_fasten = Component.objects.get_or_create(
        id=249, category=component_category_fasten[0], product=product_kafshoor_ceramic_60_8[0],
        name="بست کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_bend = Component.objects.get_or_create(
        id=250, category=component_category_bend[0], product=product_kafshoor_ceramic_60_8[0],
        name="خم کفشور 8 * 60 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_spring = Component.objects.get_or_create(
        id=251, category=component_category_spring[0], product=product_kafshoor_ceramic_60_8[0],
        name="فنر کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_key = Component.objects.get_or_create(
        id=252, category=component_category_key[0], product=product_kafshoor_ceramic_60_8[0],
        name="کلید کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_weld = Component.objects.get_or_create(
        id=253, category=component_category_weld[0], product=product_kafshoor_ceramic_60_8[0],
        name="جوش کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_reamer = Component.objects.get_or_create(
        id=254, category=component_category_reamer[0], product=product_kafshoor_ceramic_60_8[0],
        name="قلاویز کفشور 8 * 60 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_electropolish = Component.objects.get_or_create(
        id=255, category=component_category_electropolish[0], product=product_kafshoor_ceramic_60_8[0],
        name="الکتروپلیش کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_press = Component.objects.get_or_create(
        id=256, category=component_category_press[0], product=product_kafshoor_ceramic_60_8[0],
        name="پرس کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_60_8_paper = Component.objects.get_or_create(
        id=257, category=component_category_paper[0], product=product_kafshoor_ceramic_60_8[0],
        name="کاغذ تبلیغ کفشور 8 * 60 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 80 * 8
    product_kafshoor_ceramic_80_8 = Product.objects.get_or_create(
        id=19, name="کفشور 8 * 80 سرامیک خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Ceramic 80 * 8
    component_kafshoor_ceramic_80_8_steel_15 = Component.objects.get_or_create(
        id=261, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_80_8[0],
        name="ورق استیل کفشور 8 * 80 سرامیک خور", description='', used_count=190544,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_flappy = Component.objects.get_or_create(
        id=262, category=component_category_flappy[0], product=product_kafshoor_ceramic_80_8[0],
        name="فلاپی کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_80_8_pipe = Component.objects.get_or_create(
        id=263, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_80_8[0],
        name="لوله کفشور 8 * 80 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_pipe_cutting = Component.objects.get_or_create(
        id=264, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_80_8[0],
        name="برش لوله کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_laser_gas = Component.objects.get_or_create(
        id=265, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_80_8[0],
        name="لیزر و گاز کفشور 8 * 80 سرامیک خور", description='', used_count=4367,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_dome = Component.objects.get_or_create(
        id=266, category=component_category_dome[0], product=product_kafshoor_ceramic_80_8[0],
        name="نکی کفشور 8 * 80 سرامیک خور", description='', used_count=14,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_screw_15 = Component.objects.get_or_create(
        id=267, category=component_category_screw_15[0], product=product_kafshoor_ceramic_80_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 80 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_screw_30 = Component.objects.get_or_create(
        id=268, category=component_category_screw_30[0], product=product_kafshoor_ceramic_80_8[0],
        name="پیچ 3 سانتی کفشور 8 * 80 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_fasten = Component.objects.get_or_create(
        id=269, category=component_category_fasten[0], product=product_kafshoor_ceramic_80_8[0],
        name="بست کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_bend = Component.objects.get_or_create(
        id=270, category=component_category_bend[0], product=product_kafshoor_ceramic_80_8[0],
        name="خم کفشور 8 * 80 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_spring = Component.objects.get_or_create(
        id=271, category=component_category_spring[0], product=product_kafshoor_ceramic_80_8[0],
        name="فنر کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_key = Component.objects.get_or_create(
        id=272, category=component_category_key[0], product=product_kafshoor_ceramic_80_8[0],
        name="کلید کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_weld = Component.objects.get_or_create(
        id=273, category=component_category_weld[0], product=product_kafshoor_ceramic_80_8[0],
        name="جوش کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_reamer = Component.objects.get_or_create(
        id=274, category=component_category_reamer[0], product=product_kafshoor_ceramic_80_8[0],
        name="قلاویز کفشور 8 * 80 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_electropolish = Component.objects.get_or_create(
        id=275, category=component_category_electropolish[0], product=product_kafshoor_ceramic_80_8[0],
        name="الکتروپلیش کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_press = Component.objects.get_or_create(
        id=276, category=component_category_press[0], product=product_kafshoor_ceramic_80_8[0],
        name="پرس کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_80_8_paper = Component.objects.get_or_create(
        id=277, category=component_category_paper[0], product=product_kafshoor_ceramic_80_8[0],
        name="کاغذ تبلیغ کفشور 8 * 80 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 90 * 8
    product_kafshoor_ceramic_90_8 = Product.objects.get_or_create(
        id=20, name="کفشور 8 * 90 سرامیک خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Ceramic 90 * 8
    component_kafshoor_ceramic_90_8_steel_15 = Component.objects.get_or_create(
        id=281, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_90_8[0],
        name="ورق استیل کفشور 8 * 90 سرامیک خور", description='', used_count=213344,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_flappy = Component.objects.get_or_create(
        id=282, category=component_category_flappy[0], product=product_kafshoor_ceramic_90_8[0],
        name="فلاپی کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_90_8_pipe = Component.objects.get_or_create(
        id=283, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_90_8[0],
        name="لوله کفشور 8 * 90 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_pipe_cutting = Component.objects.get_or_create(
        id=284, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_90_8[0],
        name="برش لوله کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_laser_gas = Component.objects.get_or_create(
        id=285, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_90_8[0],
        name="لیزر و گاز کفشور 8 * 90 سرامیک خور", description='', used_count=4767,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_dome = Component.objects.get_or_create(
        id=286, category=component_category_dome[0], product=product_kafshoor_ceramic_90_8[0],
        name="نکی کفشور 8 * 90 سرامیک خور", description='', used_count=18,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_screw_15 = Component.objects.get_or_create(
        id=287, category=component_category_screw_15[0], product=product_kafshoor_ceramic_90_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 90 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_screw_30 = Component.objects.get_or_create(
        id=288, category=component_category_screw_30[0], product=product_kafshoor_ceramic_90_8[0],
        name="پیچ 3 سانتی کفشور 8 * 90 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_fasten = Component.objects.get_or_create(
        id=289, category=component_category_fasten[0], product=product_kafshoor_ceramic_90_8[0],
        name="بست کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_bend = Component.objects.get_or_create(
        id=290, category=component_category_bend[0], product=product_kafshoor_ceramic_90_8[0],
        name="خم کفشور 8 * 90 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_spring = Component.objects.get_or_create(
        id=291, category=component_category_spring[0], product=product_kafshoor_ceramic_90_8[0],
        name="فنر کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_key = Component.objects.get_or_create(
        id=292, category=component_category_key[0], product=product_kafshoor_ceramic_90_8[0],
        name="کلید کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_weld = Component.objects.get_or_create(
        id=293, category=component_category_weld[0], product=product_kafshoor_ceramic_90_8[0],
        name="جوش کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_reamer = Component.objects.get_or_create(
        id=294, category=component_category_reamer[0], product=product_kafshoor_ceramic_90_8[0],
        name="قلاویز کفشور 8 * 90 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_electropolish = Component.objects.get_or_create(
        id=295, category=component_category_electropolish[0], product=product_kafshoor_ceramic_90_8[0],
        name="الکتروپلیش کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_press = Component.objects.get_or_create(
        id=296, category=component_category_press[0], product=product_kafshoor_ceramic_90_8[0],
        name="پرس کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_90_8_paper = Component.objects.get_or_create(
        id=297, category=component_category_paper[0], product=product_kafshoor_ceramic_90_8[0],
        name="کاغذ تبلیغ کفشور 8 * 90 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Ceramic 100 * 8
    product_kafshoor_ceramic_100_8 = Product.objects.get_or_create(
        id=21, name="کفشور 8 * 100 سرامیک خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Ceramic 100 * 8
    component_kafshoor_ceramic_100_8_steel_15 = Component.objects.get_or_create(
        id=301, category=component_category_steel_304_15[0], product=product_kafshoor_ceramic_100_8[0],
        name="ورق استیل کفشور 8 * 100 سرامیک خور", description='', used_count=236144,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_flappy = Component.objects.get_or_create(
        id=302, category=component_category_flappy[0], product=product_kafshoor_ceramic_100_8[0],
        name="فلاپی کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_ceramic_100_8_pipe = Component.objects.get_or_create(
        id=303, category=component_category_pipe_51_mil[0], product=product_kafshoor_ceramic_100_8[0],
        name="لوله کفشور 8 * 100 سرامیک خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_pipe_cutting = Component.objects.get_or_create(
        id=304, category=component_category_pipe_cutting[0], product=product_kafshoor_ceramic_100_8[0],
        name="برش لوله کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_laser_gas = Component.objects.get_or_create(
        id=305, category=component_category_laser_gas[0], product=product_kafshoor_ceramic_100_8[0],
        name="لیزر و گاز کفشور 8 * 100 سرامیک خور", description='', used_count=5167,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_dome = Component.objects.get_or_create(
        id=306, category=component_category_dome[0], product=product_kafshoor_ceramic_100_8[0],
        name="نکی کفشور 8 * 100 سرامیک خور", description='', used_count=18,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_screw_15 = Component.objects.get_or_create(
        id=307, category=component_category_screw_15[0], product=product_kafshoor_ceramic_100_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 100 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_screw_30 = Component.objects.get_or_create(
        id=308, category=component_category_screw_30[0], product=product_kafshoor_ceramic_100_8[0],
        name="پیچ 3 سانتی کفشور 8 * 100 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_fasten = Component.objects.get_or_create(
        id=309, category=component_category_fasten[0], product=product_kafshoor_ceramic_100_8[0],
        name="بست کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_bend = Component.objects.get_or_create(
        id=310, category=component_category_bend[0], product=product_kafshoor_ceramic_100_8[0],
        name="خم کفشور 8 * 100 سرامیک خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_spring = Component.objects.get_or_create(
        id=311, category=component_category_spring[0], product=product_kafshoor_ceramic_100_8[0],
        name="فنر کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_key = Component.objects.get_or_create(
        id=312, category=component_category_key[0], product=product_kafshoor_ceramic_100_8[0],
        name="کلید کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_weld = Component.objects.get_or_create(
        id=313, category=component_category_weld[0], product=product_kafshoor_ceramic_100_8[0],
        name="جوش کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_reamer = Component.objects.get_or_create(
        id=314, category=component_category_reamer[0], product=product_kafshoor_ceramic_100_8[0],
        name="قلاویز کفشور 8 * 100 سرامیک خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_electropolish = Component.objects.get_or_create(
        id=315, category=component_category_electropolish[0], product=product_kafshoor_ceramic_100_8[0],
        name="الکتروپلیش کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_press = Component.objects.get_or_create(
        id=316, category=component_category_press[0], product=product_kafshoor_ceramic_100_8[0],
        name="پرس کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_ceramic_100_8_paper = Component.objects.get_or_create(
        id=317, category=component_category_paper[0], product=product_kafshoor_ceramic_100_8[0],
        name="کاغذ تبلیغ کفشور 8 * 100 سرامیک خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================
    # Stone
    # =================================================================================

    # Create Product Kafshoor Stone 10 * 10
    product_kafshoor_stone_10_10 = Product.objects.get_or_create(
        id=31, name="کفشور 10 * 10 سنگ خور", description='', no_prod_per_year=260,
    )

    # Create Components for Kafshoor Stone 10 * 10
    component_kafshoor_stone_10_10_steel_15 = Component.objects.get_or_create(
        id=401, category=component_category_steel_304_15[0], product=product_kafshoor_stone_10_10[0],
        name="ورق استیل کفشور 10 * 10 سنگ خور", description='', used_count=47824,
        per_product=1
    )
    component_kafshoor_stone_10_10_flappy = Component.objects.get_or_create(
        id=402, category=component_category_flappy[0], product=product_kafshoor_stone_10_10[0],
        name="فلاپی کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_10_10_pipe = Component.objects.get_or_create(
        id=403, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_10_10[0],
        name="لوله کفشور 10 * 10 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_10_10_pipe_cutting = Component.objects.get_or_create(
        id=404, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_10_10[0],
        name="برش لوله کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_10_10_laser_gas = Component.objects.get_or_create(
        id=405, category=component_category_laser_gas[0], product=product_kafshoor_stone_10_10[0],
        name="لیزر و گاز کفشور 10 * 10 سنگ خور", description='', used_count=1807,
        per_product=1
    )
    component_kafshoor_stone_10_10_dome = Component.objects.get_or_create(
        id=406, category=component_category_dome[0], product=product_kafshoor_stone_10_10[0],
        name="نکی کفشور 10 * 10 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_10_10_screw_15 = Component.objects.get_or_create(
        id=407, category=component_category_screw_15[0], product=product_kafshoor_stone_10_10[0],
        name="پیچ 1.5 سانتی کفشور 10 * 10 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_10_10_bend = Component.objects.get_or_create(
        id=408, category=component_category_bend[0], product=product_kafshoor_stone_10_10[0],
        name="خم کفشور 10 * 10 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_10_10_spring = Component.objects.get_or_create(
        id=409, category=component_category_spring[0], product=product_kafshoor_stone_10_10[0],
        name="فنر کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_10_10_key = Component.objects.get_or_create(
        id=410, category=component_category_key[0], product=product_kafshoor_stone_10_10[0],
        name="کلید کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_10_10_weld = Component.objects.get_or_create(
        id=411, category=component_category_weld[0], product=product_kafshoor_stone_10_10[0],
        name="جوش کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_10_10_reamer = Component.objects.get_or_create(
        id=412, category=component_category_reamer[0], product=product_kafshoor_stone_10_10[0],
        name="قلاویز کفشور 10 * 10 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_10_10_electropolish = Component.objects.get_or_create(
        id=413, category=component_category_electropolish[0], product=product_kafshoor_stone_10_10[0],
        name="الکتروپلیش کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_10_10_press = Component.objects.get_or_create(
        id=414, category=component_category_press[0], product=product_kafshoor_stone_10_10[0],
        name="پرس کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_10_10_paper = Component.objects.get_or_create(
        id=415, category=component_category_paper[0], product=product_kafshoor_stone_10_10[0],
        name="کاغذ تبلیغ کفشور 10 * 10 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =======================================================================================

    # Create Product Kafshoor Stone 12 * 12
    product_kafshoor_stone_12_12 = Product.objects.get_or_create(
        id=32, name="کفشور 12 * 12 سنگ خور", description='', no_prod_per_year=45,
    )

    # Create Components for Kafshoor Stone 10 * 10
    component_kafshoor_stone_12_12_steel_15 = Component.objects.get_or_create(
        id=421, category=component_category_steel_304_15[0], product=product_kafshoor_stone_12_12[0],
        name="ورق استیل کفشور 12 * 12 سنگ خور", description='', used_count=60944,
        per_product=1
    )
    component_kafshoor_stone_12_12_flappy = Component.objects.get_or_create(
        id=422, category=component_category_flappy[0], product=product_kafshoor_stone_12_12[0],
        name="فلاپی کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_12_12_pipe = Component.objects.get_or_create(
        id=423, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_12_12[0],
        name="لوله کفشور 12 * 12 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_12_12_pipe_cutting = Component.objects.get_or_create(
        id=424, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_12_12[0],
        name="برش لوله کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_12_12_laser_gas = Component.objects.get_or_create(
        id=425, category=component_category_laser_gas[0], product=product_kafshoor_stone_12_12[0],
        name="لیزر و گاز کفشور 12 * 12 سنگ خور", description='', used_count=1967,
        per_product=1
    )
    component_kafshoor_stone_12_12_dome = Component.objects.get_or_create(
        id=426, category=component_category_dome[0], product=product_kafshoor_stone_12_12[0],
        name="نکی کفشور 12 * 12 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_12_12_screw_15 = Component.objects.get_or_create(
        id=427, category=component_category_screw_15[0], product=product_kafshoor_stone_12_12[0],
        name="پیچ 1.5 سانتی کفشور 12 * 12 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_12_12_bend = Component.objects.get_or_create(
        id=428, category=component_category_bend[0], product=product_kafshoor_stone_12_12[0],
        name="خم کفشور 12 * 12 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_12_12_spring = Component.objects.get_or_create(
        id=429, category=component_category_spring[0], product=product_kafshoor_stone_12_12[0],
        name="فنر کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_12_12_key = Component.objects.get_or_create(
        id=430, category=component_category_key[0], product=product_kafshoor_stone_12_12[0],
        name="کلید کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_12_12_weld = Component.objects.get_or_create(
        id=431, category=component_category_weld[0], product=product_kafshoor_stone_12_12[0],
        name="جوش کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_12_12_reamer = Component.objects.get_or_create(
        id=432, category=component_category_reamer[0], product=product_kafshoor_stone_12_12[0],
        name="قلاویز کفشور 12 * 12 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_12_12_electropolish = Component.objects.get_or_create(
        id=433, category=component_category_electropolish[0], product=product_kafshoor_stone_12_12[0],
        name="الکتروپلیش کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_12_12_press = Component.objects.get_or_create(
        id=434, category=component_category_press[0], product=product_kafshoor_stone_12_12[0],
        name="پرس کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_12_12_paper = Component.objects.get_or_create(
        id=435, category=component_category_paper[0], product=product_kafshoor_stone_12_12[0],
        name="کاغذ تبلیغ کفشور 12 * 12 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 15 * 15
    product_kafshoor_stone_15_15 = Product.objects.get_or_create(
        id=33, name="کفشور 15 * 15 سنگ خور", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Stone 15 * 15
    component_kafshoor_stone_15_15_steel_15 = Component.objects.get_or_create(
        id=441, category=component_category_steel_304_15[0], product=product_kafshoor_stone_15_15[0],
        name="ورق استیل کفشور 15 * 15 سنگ خور", description='', used_count=83624,
        per_product=1
    )
    component_kafshoor_stone_15_15_flappy = Component.objects.get_or_create(
        id=442, category=component_category_flappy[0], product=product_kafshoor_stone_15_15[0],
        name="فلاپی کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_15_15_pipe = Component.objects.get_or_create(
        id=443, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_15_15[0],
        name="لوله کفشور 15 * 15 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_15_15_pipe_cutting = Component.objects.get_or_create(
        id=444, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_15_15[0],
        name="برش لوله کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_15_15_laser_gas = Component.objects.get_or_create(
        id=445, category=component_category_laser_gas[0], product=product_kafshoor_stone_15_15[0],
        name="لیزر و گاز کفشور 15 * 15 سنگ خور", description='', used_count=2207,
        per_product=1
    )
    component_kafshoor_stone_15_15_dome = Component.objects.get_or_create(
        id=446, category=component_category_dome[0], product=product_kafshoor_stone_15_15[0],
        name="نکی کفشور 15 * 15 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_15_15_screw_15 = Component.objects.get_or_create(
        id=447, category=component_category_screw_15[0], product=product_kafshoor_stone_15_15[0],
        name="پیچ 1.5 سانتی کفشور 15 * 15 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_15_15_bend = Component.objects.get_or_create(
        id=448, category=component_category_bend[0], product=product_kafshoor_stone_15_15[0],
        name="خم کفشور 15 * 15 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_15_15_spring = Component.objects.get_or_create(
        id=449, category=component_category_spring[0], product=product_kafshoor_stone_15_15[0],
        name="فنر کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_15_15_key = Component.objects.get_or_create(
        id=450, category=component_category_key[0], product=product_kafshoor_stone_15_15[0],
        name="کلید کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_15_15_weld = Component.objects.get_or_create(
        id=451, category=component_category_weld[0], product=product_kafshoor_stone_15_15[0],
        name="جوش کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_15_15_reamer = Component.objects.get_or_create(
        id=452, category=component_category_reamer[0], product=product_kafshoor_stone_15_15[0],
        name="قلاویز کفشور 15 * 15 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_15_15_electropolish = Component.objects.get_or_create(
        id=453, category=component_category_electropolish[0], product=product_kafshoor_stone_15_15[0],
        name="الکتروپلیش کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_15_15_press = Component.objects.get_or_create(
        id=454, category=component_category_press[0], product=product_kafshoor_stone_15_15[0],
        name="پرس کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_15_15_paper = Component.objects.get_or_create(
        id=455, category=component_category_paper[0], product=product_kafshoor_stone_15_15[0],
        name="کاغذ تبلیغ کفشور 15 * 15 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 17 * 17
    product_kafshoor_stone_17_17 = Product.objects.get_or_create(
        id=34, name="کفشور 17 * 17 سنگ خور", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Stone 17 * 17
    component_kafshoor_stone_17_17_steel_15 = Component.objects.get_or_create(
        id=461, category=component_category_steel_304_15[0], product=product_kafshoor_stone_17_17[0],
        name="ورق استیل کفشور 17 * 17 سنگ خور", description='', used_count=100744,
        per_product=1
    )
    component_kafshoor_stone_17_17_flappy = Component.objects.get_or_create(
        id=462, category=component_category_flappy[0], product=product_kafshoor_stone_17_17[0],
        name="فلاپی کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_17_17_pipe = Component.objects.get_or_create(
        id=463, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_17_17[0],
        name="لوله کفشور 17 * 17 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_17_17_pipe_cutting = Component.objects.get_or_create(
        id=464, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_17_17[0],
        name="برش لوله کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_17_17_laser_gas = Component.objects.get_or_create(
        id=465, category=component_category_laser_gas[0], product=product_kafshoor_stone_17_17[0],
        name="لیزر و گاز کفشور 17 * 17 سنگ خور", description='', used_count=2367,
        per_product=1
    )
    component_kafshoor_stone_17_17_dome = Component.objects.get_or_create(
        id=466, category=component_category_dome[0], product=product_kafshoor_stone_17_17[0],
        name="نکی کفشور 17 * 17 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_17_17_screw_15 = Component.objects.get_or_create(
        id=467, category=component_category_screw_15[0], product=product_kafshoor_stone_17_17[0],
        name="پیچ 1.5 سانتی کفشور 17 * 17 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_17_17_bend = Component.objects.get_or_create(
        id=468, category=component_category_bend[0], product=product_kafshoor_stone_17_17[0],
        name="خم کفشور 17 * 17 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_17_17_spring = Component.objects.get_or_create(
        id=469, category=component_category_spring[0], product=product_kafshoor_stone_17_17[0],
        name="فنر کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_17_17_key = Component.objects.get_or_create(
        id=470, category=component_category_key[0], product=product_kafshoor_stone_17_17[0],
        name="کلید کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_17_17_weld = Component.objects.get_or_create(
        id=471, category=component_category_weld[0], product=product_kafshoor_stone_17_17[0],
        name="جوش کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_17_17_reamer = Component.objects.get_or_create(
        id=472, category=component_category_reamer[0], product=product_kafshoor_stone_17_17[0],
        name="قلاویز کفشور 17 * 17 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_17_17_electropolish = Component.objects.get_or_create(
        id=473, category=component_category_electropolish[0], product=product_kafshoor_stone_17_17[0],
        name="الکتروپلیش کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_17_17_press = Component.objects.get_or_create(
        id=474, category=component_category_press[0], product=product_kafshoor_stone_17_17[0],
        name="پرس کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_17_17_paper = Component.objects.get_or_create(
        id=475, category=component_category_paper[0], product=product_kafshoor_stone_17_17[0],
        name="کاغذ تبلیغ کفشور 17 * 17 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 20 * 20
    product_kafshoor_stone_20_20 = Product.objects.get_or_create(
        id=35, name="کفشور 20 * 20 سنگ خور", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Stone 20 * 20
    component_kafshoor_stone_20_20_steel_15 = Component.objects.get_or_create(
        id=481, category=component_category_steel_304_15[0], product=product_kafshoor_stone_20_20[0],
        name="ورق استیل کفشور 20 * 20 سنگ خور", description='', used_count=129424,
        per_product=1
    )
    component_kafshoor_stone_20_20_flappy = Component.objects.get_or_create(
        id=482, category=component_category_flappy[0], product=product_kafshoor_stone_20_20[0],
        name="فلاپی کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_20_20_pipe = Component.objects.get_or_create(
        id=483, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_20_20[0],
        name="لوله کفشور 20 * 20 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_20_20_pipe_cutting = Component.objects.get_or_create(
        id=484, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_20_20[0],
        name="برش لوله کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_20_20_laser_gas = Component.objects.get_or_create(
        id=485, category=component_category_laser_gas[0], product=product_kafshoor_stone_20_20[0],
        name="لیزر و گاز کفشور 20 * 20 سنگ خور", description='', used_count=2607,
        per_product=1
    )
    component_kafshoor_stone_20_20_dome = Component.objects.get_or_create(
        id=486, category=component_category_dome[0], product=product_kafshoor_stone_20_20[0],
        name="نکی کفشور 20 * 20 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_20_20_screw_15 = Component.objects.get_or_create(
        id=487, category=component_category_screw_15[0], product=product_kafshoor_stone_20_20[0],
        name="پیچ 1.5 سانتی کفشور 20 * 20 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_20_20_bend = Component.objects.get_or_create(
        id=488, category=component_category_bend[0], product=product_kafshoor_stone_20_20[0],
        name="خم کفشور 20 * 20 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_20_20_spring = Component.objects.get_or_create(
        id=489, category=component_category_spring[0], product=product_kafshoor_stone_20_20[0],
        name="فنر کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_20_20_key = Component.objects.get_or_create(
        id=490, category=component_category_key[0], product=product_kafshoor_stone_20_20[0],
        name="کلید کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_20_20_weld = Component.objects.get_or_create(
        id=491, category=component_category_weld[0], product=product_kafshoor_stone_20_20[0],
        name="جوش کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_20_20_reamer = Component.objects.get_or_create(
        id=492, category=component_category_reamer[0], product=product_kafshoor_stone_20_20[0],
        name="قلاویز کفشور 20 * 20 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_20_20_electropolish = Component.objects.get_or_create(
        id=493, category=component_category_electropolish[0], product=product_kafshoor_stone_20_20[0],
        name="الکتروپلیش کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_20_20_press = Component.objects.get_or_create(
        id=494, category=component_category_press[0], product=product_kafshoor_stone_20_20[0],
        name="پرس کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_20_20_paper = Component.objects.get_or_create(
        id=495, category=component_category_paper[0], product=product_kafshoor_stone_20_20[0],
        name="کاغذ تبلیغ کفشور 20 * 20 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 30 * 8
    product_kafshoor_stone_30_8 = Product.objects.get_or_create(
        id=36, name="کفشور 8 * 30 سنگ خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Stone 30 * 8
    component_kafshoor_stone_30_8_steel_15 = Component.objects.get_or_create(
        id=501, category=component_category_steel_304_15[0], product=product_kafshoor_stone_30_8[0],
        name="ورق استیل کفشور 8 * 30 سنگ خور", description='', used_count=95264,
        per_product=1
    )
    component_kafshoor_stone_30_8_flappy = Component.objects.get_or_create(
        id=502, category=component_category_flappy[0], product=product_kafshoor_stone_30_8[0],
        name="فلاپی کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_30_8_pipe = Component.objects.get_or_create(
        id=503, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_30_8[0],
        name="لوله کفشور 8 * 30 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_30_8_pipe_cutting = Component.objects.get_or_create(
        id=504, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_30_8[0],
        name="برش لوله کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_30_8_laser_gas = Component.objects.get_or_create(
        id=505, category=component_category_laser_gas[0], product=product_kafshoor_stone_30_8[0],
        name="لیزر و گاز کفشور 8 * 30 سنگ خور", description='', used_count=2527,
        per_product=1
    )
    component_kafshoor_stone_30_8_dome = Component.objects.get_or_create(
        id=506, category=component_category_dome[0], product=product_kafshoor_stone_30_8[0],
        name="نکی کفشور 8 * 30 سنگ خور", description='', used_count=10,
        per_product=1
    )
    component_kafshoor_stone_30_8_screw_15 = Component.objects.get_or_create(
        id=507, category=component_category_screw_15[0], product=product_kafshoor_stone_30_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 30 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_30_8_screw_30 = Component.objects.get_or_create(
        id=508, category=component_category_screw_30[0], product=product_kafshoor_stone_30_8[0],
        name="پیچ 3 سانتی کفشور 8 * 30 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_30_8_fasten = Component.objects.get_or_create(
        id=509, category=component_category_fasten[0], product=product_kafshoor_stone_30_8[0],
        name="بست کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_30_8_bend = Component.objects.get_or_create(
        id=510, category=component_category_bend[0], product=product_kafshoor_stone_30_8[0],
        name="خم کفشور 8 * 30 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_30_8_spring = Component.objects.get_or_create(
        id=511, category=component_category_spring[0], product=product_kafshoor_stone_30_8[0],
        name="فنر کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_30_8_key = Component.objects.get_or_create(
        id=512, category=component_category_key[0], product=product_kafshoor_stone_30_8[0],
        name="کلید کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_30_8_weld = Component.objects.get_or_create(
        id=513, category=component_category_weld[0], product=product_kafshoor_stone_30_8[0],
        name="جوش کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoorstone_30_8_reamer = Component.objects.get_or_create(
        id=514, category=component_category_reamer[0], product=product_kafshoor_stone_30_8[0],
        name="قلاویز کفشور 8 * 30 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_30_8_electropolish = Component.objects.get_or_create(
        id=515, category=component_category_electropolish[0], product=product_kafshoor_stone_30_8[0],
        name="الکتروپلیش کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_30_8_press = Component.objects.get_or_create(
        id=516, category=component_category_press[0], product=product_kafshoor_stone_30_8[0],
        name="پرس کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_30_8_paper = Component.objects.get_or_create(
        id=517, category=component_category_paper[0], product=product_kafshoor_stone_30_8[0],
        name="کاغذ تبلیغ کفشور 8 * 30 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 45 * 8
    product_kafshoor_stone_45_8 = Product.objects.get_or_create(
        id=37, name="کفشور 8 * 45 سنگ خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Stone 45 * 8
    component_kafshoor_stone_45_8_steel_15 = Component.objects.get_or_create(
        id=521, category=component_category_steel_304_15[0], product=product_kafshoor_stone_45_8[0],
        name="ورق استیل کفشور 8 * 45 سنگ خور", description='', used_count=135464,
        per_product=1
    )
    component_kafshoor_stone_45_8_flappy = Component.objects.get_or_create(
        id=522, category=component_category_flappy[0], product=product_kafshoor_stone_45_8[0],
        name="فلاپی کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_45_8_pipe = Component.objects.get_or_create(
        id=523, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_45_8[0],
        name="لوله کفشور 8 * 45 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_45_8_pipe_cutting = Component.objects.get_or_create(
        id=524, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_45_8[0],
        name="برش لوله کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_laser_gas = Component.objects.get_or_create(
        id=525, category=component_category_laser_gas[0], product=product_kafshoor_stone_45_8[0],
        name="لیزر و گاز کفشور 8 * 45 سنگ خور", description='', used_count=3127,
        per_product=1
    )
    component_kafshoor_stone_45_8_dome = Component.objects.get_or_create(
        id=526, category=component_category_dome[0], product=product_kafshoor_stone_45_8[0],
        name="نکی کفشور 8 * 45 سنگ خور", description='', used_count=14,
        per_product=1
    )
    component_kafshoor_stone_45_8_screw_15 = Component.objects.get_or_create(
        id=527, category=component_category_screw_15[0], product=product_kafshoor_stone_45_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 45 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_45_8_screw_30 = Component.objects.get_or_create(
        id=528, category=component_category_screw_30[0], product=product_kafshoor_stone_45_8[0],
        name="پیچ 3 سانتی کفشور 8 * 45 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_45_8_fasten = Component.objects.get_or_create(
        id=529, category=component_category_fasten[0], product=product_kafshoor_stone_45_8[0],
        name="بست کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_bend = Component.objects.get_or_create(
        id=530, category=component_category_bend[0], product=product_kafshoor_stone_45_8[0],
        name="خم کفشور 8 * 45 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_45_8_spring = Component.objects.get_or_create(
        id=531, category=component_category_spring[0], product=product_kafshoor_stone_45_8[0],
        name="فنر کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_key = Component.objects.get_or_create(
        id=532, category=component_category_key[0], product=product_kafshoor_stone_45_8[0],
        name="کلید کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_weld = Component.objects.get_or_create(
        id=533, category=component_category_weld[0], product=product_kafshoor_stone_45_8[0],
        name="جوش کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_reamer = Component.objects.get_or_create(
        id=534, category=component_category_reamer[0], product=product_kafshoor_stone_45_8[0],
        name="قلاویز کفشور 8 * 45 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_45_8_electropolish = Component.objects.get_or_create(
        id=535, category=component_category_electropolish[0], product=product_kafshoor_stone_45_8[0],
        name="الکتروپلیش کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_press = Component.objects.get_or_create(
        id=536, category=component_category_press[0], product=product_kafshoor_stone_45_8[0],
        name="پرس کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_45_8_paper = Component.objects.get_or_create(
        id=537, category=component_category_paper[0], product=product_kafshoor_stone_45_8[0],
        name="کاغذ تبلیغ کفشور 8 * 45 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 60 * 8
    product_kafshoor_stone_60_8 = Product.objects.get_or_create(
        id=38, name="کفشور 8 * 60 سنگ خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Stone 60 * 8
    component_kafshoor_stone_60_8_steel_15 = Component.objects.get_or_create(
        id=541, category=component_category_steel_304_15[0], product=product_kafshoor_stone_60_8[0],
        name="ورق استیل کفشور 8 * 60 سنگ خور", description='', used_count=175664,
        per_product=1
    )
    component_kafshoor_stone_60_8_flappy = Component.objects.get_or_create(
        id=542, category=component_category_flappy[0], product=product_kafshoor_stone_60_8[0],
        name="فلاپی کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_60_8_pipe = Component.objects.get_or_create(
        id=543, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_60_8[0],
        name="لوله کفشور 8 * 60 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_60_8_pipe_cutting = Component.objects.get_or_create(
        id=544, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_60_8[0],
        name="برش لوله کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_laser_gas = Component.objects.get_or_create(
        id=545, category=component_category_laser_gas[0], product=product_kafshoor_stone_60_8[0],
        name="لیزر و گاز کفشور 8 * 60 سنگ خور", description='', used_count=3727,
        per_product=1
    )
    component_kafshoor_stone_60_8_dome = Component.objects.get_or_create(
        id=546, category=component_category_dome[0], product=product_kafshoor_stone_60_8[0],
        name="نکی کفشور 8 * 60 سنگ خور", description='', used_count=14,
        per_product=1
    )
    component_kafshoor_stone_60_8_screw_15 = Component.objects.get_or_create(
        id=547, category=component_category_screw_15[0], product=product_kafshoor_stone_60_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 60 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_60_8_screw_30 = Component.objects.get_or_create(
        id=548, category=component_category_screw_30[0], product=product_kafshoor_stone_60_8[0],
        name="پیچ 3 سانتی کفشور 8 * 60 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_60_8_fasten = Component.objects.get_or_create(
        id=549, category=component_category_fasten[0], product=product_kafshoor_stone_60_8[0],
        name="بست کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_bend = Component.objects.get_or_create(
        id=550, category=component_category_bend[0], product=product_kafshoor_stone_60_8[0],
        name="خم کفشور 8 * 60 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_60_8_spring = Component.objects.get_or_create(
        id=551, category=component_category_spring[0], product=product_kafshoor_stone_60_8[0],
        name="فنر کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_key = Component.objects.get_or_create(
        id=552, category=component_category_key[0], product=product_kafshoor_stone_60_8[0],
        name="کلید کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_weld = Component.objects.get_or_create(
        id=553, category=component_category_weld[0], product=product_kafshoor_stone_60_8[0],
        name="جوش کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_reamer = Component.objects.get_or_create(
        id=554, category=component_category_reamer[0], product=product_kafshoor_stone_60_8[0],
        name="قلاویز کفشور 8 * 60 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_60_8_electropolish = Component.objects.get_or_create(
        id=555, category=component_category_electropolish[0], product=product_kafshoor_stone_60_8[0],
        name="الکتروپلیش کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_press = Component.objects.get_or_create(
        id=556, category=component_category_press[0], product=product_kafshoor_stone_60_8[0],
        name="پرس کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_60_8_paper = Component.objects.get_or_create(
        id=557, category=component_category_paper[0], product=product_kafshoor_stone_60_8[0],
        name="کاغذ تبلیغ کفشور 8 * 60 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 80 * 8
    product_kafshoor_stone_80_8 = Product.objects.get_or_create(
        id=39, name="کفشور 8 * 80 سنگ خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Stone 80 * 8
    component_kafshoor_stone_80_8_steel_15 = Component.objects.get_or_create(
        id=561, category=component_category_steel_304_15[0], product=product_kafshoor_stone_80_8[0],
        name="ورق استیل کفشور 8 * 80 سنگ خور", description='', used_count=229264,
        per_product=1
    )
    component_kafshoor_stone_80_8_flappy = Component.objects.get_or_create(
        id=562, category=component_category_flappy[0], product=product_kafshoor_stone_80_8[0],
        name="فلاپی کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_80_8_pipe = Component.objects.get_or_create(
        id=563, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_80_8[0],
        name="لوله کفشور 8 * 80 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_80_8_pipe_cutting = Component.objects.get_or_create(
        id=564, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_80_8[0],
        name="برش لوله کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_laser_gas = Component.objects.get_or_create(
        id=565, category=component_category_laser_gas[0], product=product_kafshoor_stone_80_8[0],
        name="لیزر و گاز کفشور 8 * 80 سنگ خور", description='', used_count=4527,
        per_product=1
    )
    component_kafshoor_stone_80_8_dome = Component.objects.get_or_create(
        id=566, category=component_category_dome[0], product=product_kafshoor_stone_80_8[0],
        name="نکی کفشور 8 * 80 سنگ خور", description='', used_count=14,
        per_product=1
    )
    component_kafshoor_stone_80_8_screw_15 = Component.objects.get_or_create(
        id=567, category=component_category_screw_15[0], product=product_kafshoor_stone_80_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 80 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_80_8_screw_30 = Component.objects.get_or_create(
        id=568, category=component_category_screw_30[0], product=product_kafshoor_stone_80_8[0],
        name="پیچ 3 سانتی کفشور 8 * 80 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_80_8_fasten = Component.objects.get_or_create(
        id=569, category=component_category_fasten[0], product=product_kafshoor_stone_80_8[0],
        name="بست کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_bend = Component.objects.get_or_create(
        id=570, category=component_category_bend[0], product=product_kafshoor_stone_80_8[0],
        name="خم کفشور 8 * 80 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_80_8_spring = Component.objects.get_or_create(
        id=571, category=component_category_spring[0], product=product_kafshoor_stone_80_8[0],
        name="فنر کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_key = Component.objects.get_or_create(
        id=572, category=component_category_key[0], product=product_kafshoor_stone_80_8[0],
        name="کلید کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_weld = Component.objects.get_or_create(
        id=573, category=component_category_weld[0], product=product_kafshoor_stone_80_8[0],
        name="جوش کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_reamer = Component.objects.get_or_create(
        id=574, category=component_category_reamer[0], product=product_kafshoor_stone_80_8[0],
        name="قلاویز کفشور 8 * 80 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_80_8_electropolish = Component.objects.get_or_create(
        id=575, category=component_category_electropolish[0], product=product_kafshoor_stone_80_8[0],
        name="الکتروپلیش کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_press = Component.objects.get_or_create(
        id=576, category=component_category_press[0], product=product_kafshoor_stone_80_8[0],
        name="پرس کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_80_8_paper = Component.objects.get_or_create(
        id=577, category=component_category_paper[0], product=product_kafshoor_stone_80_8[0],
        name="کاغذ تبلیغ کفشور 8 * 80 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 90 * 8
    product_kafshoor_stone_90_8 = Product.objects.get_or_create(
        id=40, name="کفشور 8 * 90 سنگ خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Stone 90 * 8
    component_kafshoor_stone_90_8_steel_15 = Component.objects.get_or_create(
        id=581, category=component_category_steel_304_15[0], product=product_kafshoor_stone_90_8[0],
        name="ورق استیل کفشور 8 * 90 سنگ خور", description='', used_count=256064,
        per_product=1
    )
    component_kafshoor_stone_90_8_flappy = Component.objects.get_or_create(
        id=582, category=component_category_flappy[0], product=product_kafshoor_stone_90_8[0],
        name="فلاپی کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_90_8_pipe = Component.objects.get_or_create(
        id=583, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_90_8[0],
        name="لوله کفشور 8 * 90 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_90_8_pipe_cutting = Component.objects.get_or_create(
        id=584, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_90_8[0],
        name="برش لوله کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_laser_gas = Component.objects.get_or_create(
        id=585, category=component_category_laser_gas[0], product=product_kafshoor_stone_90_8[0],
        name="لیزر و گاز کفشور 8 * 90 سنگ خور", description='', used_count=4927,
        per_product=1
    )
    component_kafshoor_stone_90_8_dome = Component.objects.get_or_create(
        id=586, category=component_category_dome[0], product=product_kafshoor_stone_90_8[0],
        name="نکی کفشور 8 * 90 سنگ خور", description='', used_count=18,
        per_product=1
    )
    component_kafshoor_stone_90_8_screw_15 = Component.objects.get_or_create(
        id=587, category=component_category_screw_15[0], product=product_kafshoor_stone_90_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 90 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_90_8_screw_30 = Component.objects.get_or_create(
        id=588, category=component_category_screw_30[0], product=product_kafshoor_stone_90_8[0],
        name="پیچ 3 سانتی کفشور 8 * 90 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_90_8_fasten = Component.objects.get_or_create(
        id=589, category=component_category_fasten[0], product=product_kafshoor_stone_90_8[0],
        name="بست کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_bend = Component.objects.get_or_create(
        id=590, category=component_category_bend[0], product=product_kafshoor_stone_90_8[0],
        name="خم کفشور 8 * 90 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_90_8_spring = Component.objects.get_or_create(
        id=591, category=component_category_spring[0], product=product_kafshoor_stone_90_8[0],
        name="فنر کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_key = Component.objects.get_or_create(
        id=592, category=component_category_key[0], product=product_kafshoor_stone_90_8[0],
        name="کلید کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_weld = Component.objects.get_or_create(
        id=593, category=component_category_weld[0], product=product_kafshoor_stone_90_8[0],
        name="جوش کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_reamer = Component.objects.get_or_create(
        id=594, category=component_category_reamer[0], product=product_kafshoor_stone_90_8[0],
        name="قلاویز کفشور 8 * 90 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_90_8_electropolish = Component.objects.get_or_create(
        id=595, category=component_category_electropolish[0], product=product_kafshoor_stone_90_8[0],
        name="الکتروپلیش کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_press = Component.objects.get_or_create(
        id=596, category=component_category_press[0], product=product_kafshoor_stone_90_8[0],
        name="پرس کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_90_8_paper = Component.objects.get_or_create(
        id=597, category=component_category_paper[0], product=product_kafshoor_stone_90_8[0],
        name="کاغذ تبلیغ کفشور 8 * 90 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Stone 100 * 8
    product_kafshoor_stone_100_8 = Product.objects.get_or_create(
        id=41, name="کفشور 8 * 100 سنگ خور", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Stone 100 * 8
    component_kafshoor_stone_100_8_steel_15 = Component.objects.get_or_create(
        id=601, category=component_category_steel_304_15[0], product=product_kafshoor_stone_100_8[0],
        name="ورق استیل کفشور 8 * 100 سنگ خور", description='', used_count=282864,
        per_product=1
    )
    component_kafshoor_stone_100_8_flappy = Component.objects.get_or_create(
        id=602, category=component_category_flappy[0], product=product_kafshoor_stone_100_8[0],
        name="فلاپی کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_stone_100_8_pipe = Component.objects.get_or_create(
        id=603, category=component_category_pipe_51_mil[0], product=product_kafshoor_stone_100_8[0],
        name="لوله کفشور 8 * 100 سنگ خور", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_stone_100_8_pipe_cutting = Component.objects.get_or_create(
        id=604, category=component_category_pipe_cutting[0], product=product_kafshoor_stone_100_8[0],
        name="برش لوله کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_laser_gas = Component.objects.get_or_create(
        id=605, category=component_category_laser_gas[0], product=product_kafshoor_stone_100_8[0],
        name="لیزر و گاز کفشور 8 * 100 سنگ خور", description='', used_count=5327,
        per_product=1
    )
    component_kafshoor_stone_100_8_dome = Component.objects.get_or_create(
        id=606, category=component_category_dome[0], product=product_kafshoor_stone_100_8[0],
        name="نکی کفشور 8 * 100 سنگ خور", description='', used_count=18,
        per_product=1
    )
    component_kafshoor_stone_100_8_screw_15 = Component.objects.get_or_create(
        id=607, category=component_category_screw_15[0], product=product_kafshoor_stone_100_8[0],
        name="پیچ 1.5 سانتی کفشور 8 * 100 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_100_8_screw_30 = Component.objects.get_or_create(
        id=608, category=component_category_screw_30[0], product=product_kafshoor_stone_100_8[0],
        name="پیچ 3 سانتی کفشور 8 * 100 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_100_8_fasten = Component.objects.get_or_create(
        id=609, category=component_category_fasten[0], product=product_kafshoor_stone_100_8[0],
        name="بست کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_bend = Component.objects.get_or_create(
        id=610, category=component_category_bend[0], product=product_kafshoor_stone_100_8[0],
        name="خم کفشور 8 * 100 سنگ خور", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_stone_100_8_spring = Component.objects.get_or_create(
        id=611, category=component_category_spring[0], product=product_kafshoor_stone_100_8[0],
        name="فنر کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_key = Component.objects.get_or_create(
        id=612, category=component_category_key[0], product=product_kafshoor_stone_100_8[0],
        name="کلید کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_weld = Component.objects.get_or_create(
        id=613, category=component_category_weld[0], product=product_kafshoor_stone_100_8[0],
        name="جوش کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_reamer = Component.objects.get_or_create(
        id=614, category=component_category_reamer[0], product=product_kafshoor_stone_100_8[0],
        name="قلاویز کفشور 8 * 100 سنگ خور", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_stone_100_8_electropolish = Component.objects.get_or_create(
        id=615, category=component_category_electropolish[0], product=product_kafshoor_stone_100_8[0],
        name="الکتروپلیش کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_press = Component.objects.get_or_create(
        id=616, category=component_category_press[0], product=product_kafshoor_stone_100_8[0],
        name="پرس کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_stone_100_8_paper = Component.objects.get_or_create(
        id=617, category=component_category_paper[0], product=product_kafshoor_stone_100_8[0],
        name="کاغذ تبلیغ کفشور 8 * 100 سنگ خور", description='', used_count=1,
        per_product=1
    )

    # =================================================================================
    # Point Grill
    # =================================================================================

    # Create Product Kafshoor Point Grill 10 * 10
    product_kafshoor_grill_point_10_10 = Product.objects.get_or_create(
        id=51, name="کفشور 10 * 10 گریل نقطه ای", description='', no_prod_per_year=260,
    )

    # Create Components for Kafshoor Point Grill 10 * 10
    component_kafshoor_grill_point_10_10_steel_15 = Component.objects.get_or_create(
        id=701, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_10_10[0],
        name="ورق استیل کفشور 10 * 10 گریل نقطه ای", description='', used_count=41225,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_flappy = Component.objects.get_or_create(
        id=702, category=component_category_flappy[0], product=product_kafshoor_grill_point_10_10[0],
        name="فلاپی کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_10_10_pipe = Component.objects.get_or_create(
        id=703, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_10_10[0],
        name="لوله کفشور 10 * 10 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_pipe_cutting = Component.objects.get_or_create(
        id=704, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_10_10[0],
        name="برش لوله کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_laser_gas = Component.objects.get_or_create(
        id=705, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_10_10[0],
        name="لیزر و گاز کفشور 10 * 10 گریل نقطه ای", description='', used_count=1258,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_bend = Component.objects.get_or_create(
        id=706, category=component_category_bend[0], product=product_kafshoor_grill_point_10_10[0],
        name="خم کفشور 10 * 10 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_spring = Component.objects.get_or_create(
        id=707, category=component_category_spring[0], product=product_kafshoor_grill_point_10_10[0],
        name="فنر کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_key = Component.objects.get_or_create(
        id=708, category=component_category_key[0], product=product_kafshoor_grill_point_10_10[0],
        name="کلید کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_weld = Component.objects.get_or_create(
        id=709, category=component_category_weld[0], product=product_kafshoor_grill_point_10_10[0],
        name="جوش کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_reamer = Component.objects.get_or_create(
        id=710, category=component_category_reamer[0], product=product_kafshoor_grill_point_10_10[0],
        name="قلاویز کفشور 10 * 10 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_electropolish = Component.objects.get_or_create(
        id=711, category=component_category_electropolish[0], product=product_kafshoor_grill_point_10_10[0],
        name="الکتروپلیش کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_press = Component.objects.get_or_create(
        id=712, category=component_category_press[0], product=product_kafshoor_grill_point_10_10[0],
        name="پرس کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_paper = Component.objects.get_or_create(
        id=713, category=component_category_paper[0], product=product_kafshoor_grill_point_10_10[0],
        name="کاغذ تبلیغ کفشور 10 * 10 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_10_10_grill_point = Component.objects.get_or_create(
        id=714, category=component_category_grill_point[0], product=product_kafshoor_grill_point_10_10[0],
        name="گریل نقطه ای کفشور 10 * 10 گریل نقطه ای", description='', used_count=32,
        per_product=1
    )

    # =======================================================================================

    # Create Product Kafshoor Point Grill 12 * 12
    product_kafshoor_grill_point_12_12 = Product.objects.get_or_create(
        id=52, name="کفشور 12 * 12 گریل نقطه ای", description='', no_prod_per_year=45,
    )

    # Create Components for Kafshoor Point Grill 10 * 10
    component_kafshoor_grill_point_12_12_steel_15 = Component.objects.get_or_create(
        id=721, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_12_12[0],
        name="ورق استیل کفشور 12 * 12 گریل نقطه ای", description='', used_count=53505,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_flappy = Component.objects.get_or_create(
        id=722, category=component_category_flappy[0], product=product_kafshoor_grill_point_12_12[0],
        name="فلاپی کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_12_12_pipe = Component.objects.get_or_create(
        id=723, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_12_12[0],
        name="لوله کفشور 12 * 12 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_pipe_cutting = Component.objects.get_or_create(
        id=724, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_12_12[0],
        name="برش لوله کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_laser_gas = Component.objects.get_or_create(
        id=725, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_12_12[0],
        name="لیزر و گاز کفشور 12 * 12 گریل نقطه ای", description='', used_count=1418,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_bend = Component.objects.get_or_create(
        id=726, category=component_category_bend[0], product=product_kafshoor_grill_point_12_12[0],
        name="خم کفشور 12 * 12 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_spring = Component.objects.get_or_create(
        id=727, category=component_category_spring[0], product=product_kafshoor_grill_point_12_12[0],
        name="فنر کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_key = Component.objects.get_or_create(
        id=728, category=component_category_key[0], product=product_kafshoor_grill_point_12_12[0],
        name="کلید کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_weld = Component.objects.get_or_create(
        id=729, category=component_category_weld[0], product=product_kafshoor_grill_point_12_12[0],
        name="جوش کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_reamer = Component.objects.get_or_create(
        id=730, category=component_category_reamer[0], product=product_kafshoor_grill_point_12_12[0],
        name="قلاویز کفشور 12 * 12 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_electropolish = Component.objects.get_or_create(
        id=731, category=component_category_electropolish[0], product=product_kafshoor_grill_point_12_12[0],
        name="الکتروپلیش کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_press = Component.objects.get_or_create(
        id=732, category=component_category_press[0], product=product_kafshoor_grill_point_12_12[0],
        name="پرس کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_paper = Component.objects.get_or_create(
        id=733, category=component_category_paper[0], product=product_kafshoor_grill_point_12_12[0],
        name="کاغذ تبلیغ کفشور 12 * 12 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_12_12_grill_point = Component.objects.get_or_create(
        id=734, category=component_category_grill_point[0], product=product_kafshoor_grill_point_12_12[0],
        name="گریل نقطه ای کفشور 12 * 12 گریل نقطه ای", description='', used_count=41,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 15 * 15
    product_kafshoor_grill_point_15_15 = Product.objects.get_or_create(
        id=53, name="کفشور 15 * 15 گریل نقطه ای", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Point Grill 15 * 15
    component_kafshoor_grill_point_15_15_steel_15 = Component.objects.get_or_create(
        id=741, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_15_15[0],
        name="ورق استیل کفشور 15 * 15 گریل نقطه ای", description='', used_count=74925,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_flappy = Component.objects.get_or_create(
        id=742, category=component_category_flappy[0], product=product_kafshoor_grill_point_15_15[0],
        name="فلاپی کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_15_15_pipe = Component.objects.get_or_create(
        id=743, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_15_15[0],
        name="لوله کفشور 15 * 15 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_pipe_cutting = Component.objects.get_or_create(
        id=744, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_15_15[0],
        name="برش لوله کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_laser_gas = Component.objects.get_or_create(
        id=745, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_15_15[0],
        name="لیزر و گاز کفشور 15 * 15 گریل نقطه ای", description='', used_count=1658,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_bend = Component.objects.get_or_create(
        id=746, category=component_category_bend[0], product=product_kafshoor_grill_point_15_15[0],
        name="خم کفشور 15 * 15 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_spring = Component.objects.get_or_create(
        id=747, category=component_category_spring[0], product=product_kafshoor_grill_point_15_15[0],
        name="فنر کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_key = Component.objects.get_or_create(
        id=748, category=component_category_key[0], product=product_kafshoor_grill_point_15_15[0],
        name="کلید کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_weld = Component.objects.get_or_create(
        id=749, category=component_category_weld[0], product=product_kafshoor_grill_point_15_15[0],
        name="جوش کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_reamer = Component.objects.get_or_create(
        id=750, category=component_category_reamer[0], product=product_kafshoor_grill_point_15_15[0],
        name="قلاویز کفشور 15 * 15 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_electropolish = Component.objects.get_or_create(
        id=751, category=component_category_electropolish[0], product=product_kafshoor_grill_point_15_15[0],
        name="الکتروپلیش کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_press = Component.objects.get_or_create(
        id=752, category=component_category_press[0], product=product_kafshoor_grill_point_15_15[0],
        name="پرس کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_paper = Component.objects.get_or_create(
        id=753, category=component_category_paper[0], product=product_kafshoor_grill_point_15_15[0],
        name="کاغذ تبلیغ کفشور 15 * 15 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_15_15_grill_point = Component.objects.get_or_create(
        id=754, category=component_category_grill_point[0], product=product_kafshoor_grill_point_15_15[0],
        name="گریل نقطه ای کفشور 15 * 15 گریل نقطه ای", description='', used_count=60,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 17 * 17
    product_kafshoor_grill_point_17_17 = Product.objects.get_or_create(
        id=54, name="کفشور 17 * 17 گریل نقطه ای", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Point Grill 17 * 17
    component_kafshoor_grill_point_17_17_steel_15 = Component.objects.get_or_create(
        id=761, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_17_17[0],
        name="ورق استیل کفشور 17 * 17 گریل نقطه ای", description='', used_count=91205,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_flappy = Component.objects.get_or_create(
        id=762, category=component_category_flappy[0], product=product_kafshoor_grill_point_17_17[0],
        name="فلاپی کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_17_17_pipe = Component.objects.get_or_create(
        id=763, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_17_17[0],
        name="لوله کفشور 17 * 17 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_pipe_cutting = Component.objects.get_or_create(
        id=764, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_17_17[0],
        name="برش لوله کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_laser_gas = Component.objects.get_or_create(
        id=765, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_17_17[0],
        name="لیزر و گاز کفشور 17 * 17 گریل نقطه ای", description='', used_count=1818,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_bend = Component.objects.get_or_create(
        id=766, category=component_category_bend[0], product=product_kafshoor_grill_point_17_17[0],
        name="خم کفشور 17 * 17 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_spring = Component.objects.get_or_create(
        id=767, category=component_category_spring[0], product=product_kafshoor_grill_point_17_17[0],
        name="فنر کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_key = Component.objects.get_or_create(
        id=768, category=component_category_key[0], product=product_kafshoor_grill_point_17_17[0],
        name="کلید کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_weld = Component.objects.get_or_create(
        id=769, category=component_category_weld[0], product=product_kafshoor_grill_point_17_17[0],
        name="جوش کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_reamer = Component.objects.get_or_create(
        id=770, category=component_category_reamer[0], product=product_kafshoor_grill_point_17_17[0],
        name="قلاویز کفشور 17 * 17 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_electropolish = Component.objects.get_or_create(
        id=771, category=component_category_electropolish[0], product=product_kafshoor_grill_point_17_17[0],
        name="الکتروپلیش کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_press = Component.objects.get_or_create(
        id=772, category=component_category_press[0], product=product_kafshoor_grill_point_17_17[0],
        name="پرس کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_paper = Component.objects.get_or_create(
        id=773, category=component_category_paper[0], product=product_kafshoor_grill_point_17_17[0],
        name="کاغذ تبلیغ کفشور 17 * 17 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_17_17_grill_point = Component.objects.get_or_create(
        id=774, category=component_category_grill_point[0], product=product_kafshoor_grill_point_17_17[0],
        name="گریل نقطه ای کفشور 17 * 17 گریل نقطه ای", description='', used_count=80,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 20 * 20
    product_kafshoor_grill_point_20_20 = Product.objects.get_or_create(
        id=55, name="کفشور 20 * 20 گریل نقطه ای", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Point Grill 20 * 20
    component_kafshoor_grill_point_20_20_steel_15 = Component.objects.get_or_create(
        id=781, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_20_20[0],
        name="ورق استیل کفشور 20 * 20 گریل نقطه ای", description='', used_count=118625,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_flappy = Component.objects.get_or_create(
        id=782, category=component_category_flappy[0], product=product_kafshoor_grill_point_20_20[0],
        name="فلاپی کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_20_20_pipe = Component.objects.get_or_create(
        id=783, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_20_20[0],
        name="لوله کفشور 20 * 20 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_pipe_cutting = Component.objects.get_or_create(
        id=784, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_20_20[0],
        name="برش لوله کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_laser_gas = Component.objects.get_or_create(
        id=785, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_20_20[0],
        name="لیزر و گاز کفشور 20 * 20 گریل نقطه ای", description='', used_count=2058,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_bend = Component.objects.get_or_create(
        id=786, category=component_category_bend[0], product=product_kafshoor_grill_point_20_20[0],
        name="خم کفشور 20 * 20 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_spring = Component.objects.get_or_create(
        id=787, category=component_category_spring[0], product=product_kafshoor_grill_point_20_20[0],
        name="فنر کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_key = Component.objects.get_or_create(
        id=788, category=component_category_key[0], product=product_kafshoor_grill_point_20_20[0],
        name="کلید کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_weld = Component.objects.get_or_create(
        id=789, category=component_category_weld[0], product=product_kafshoor_grill_point_20_20[0],
        name="جوش کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_reamer = Component.objects.get_or_create(
        id=790, category=component_category_reamer[0], product=product_kafshoor_grill_point_20_20[0],
        name="قلاویز کفشور 20 * 20 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_electropolish = Component.objects.get_or_create(
        id=791, category=component_category_electropolish[0], product=product_kafshoor_grill_point_20_20[0],
        name="الکتروپلیش کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_press = Component.objects.get_or_create(
        id=792, category=component_category_press[0], product=product_kafshoor_grill_point_20_20[0],
        name="پرس کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_paper = Component.objects.get_or_create(
        id=793, category=component_category_paper[0], product=product_kafshoor_grill_point_20_20[0],
        name="کاغذ تبلیغ کفشور 20 * 20 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_20_20_grill_point = Component.objects.get_or_create(
        id=794, category=component_category_grill_point[0], product=product_kafshoor_grill_point_10_10[0],
        name="گریل نقطه ای کفشور 20 * 20 گریل نقطه ای", description='', used_count=94,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 30 * 8
    product_kafshoor_grill_point_30_8 = Product.objects.get_or_create(
        id=56, name="کفشور 8 * 30 گریل نقطه ای", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Point Grill 30 * 8
    component_kafshoor_grill_point_30_8_steel_15 = Component.objects.get_or_create(
        id=801, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_30_8[0],
        name="ورق استیل کفشور 8 * 30 گریل نقطه ای", description='', used_count=84885,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_flappy = Component.objects.get_or_create(
        id=802, category=component_category_flappy[0], product=product_kafshoor_grill_point_30_8[0],
        name="فلاپی کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_30_8_pipe = Component.objects.get_or_create(
        id=803, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_30_8[0],
        name="لوله کفشور 8 * 30 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_pipe_cutting = Component.objects.get_or_create(
        id=804, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_30_8[0],
        name="برش لوله کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_laser_gas = Component.objects.get_or_create(
        id=805, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_30_8[0],
        name="لیزر و گاز کفشور 8 * 30 گریل نقطه ای", description='', used_count=1978,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_screw_30 = Component.objects.get_or_create(
        id=806, category=component_category_screw_30[0], product=product_kafshoor_grill_point_30_8[0],
        name="پیچ 3 سانتی کفشور 8 * 30 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_fasten = Component.objects.get_or_create(
        id=807, category=component_category_fasten[0], product=product_kafshoor_grill_point_30_8[0],
        name="بست کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_bend = Component.objects.get_or_create(
        id=808, category=component_category_bend[0], product=product_kafshoor_grill_point_30_8[0],
        name="خم کفشور 8 * 30 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_spring = Component.objects.get_or_create(
        id=809, category=component_category_spring[0], product=product_kafshoor_grill_point_30_8[0],
        name="فنر کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_key = Component.objects.get_or_create(
        id=810, category=component_category_key[0], product=product_kafshoor_grill_point_30_8[0],
        name="کلید کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_weld = Component.objects.get_or_create(
        id=811, category=component_category_weld[0], product=product_kafshoor_grill_point_30_8[0],
        name="جوش کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoorstone_30_8_reamer = Component.objects.get_or_create(
        id=812, category=component_category_reamer[0], product=product_kafshoor_grill_point_30_8[0],
        name="قلاویز کفشور 8 * 30 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_electropolish = Component.objects.get_or_create(
        id=813, category=component_category_electropolish[0], product=product_kafshoor_grill_point_30_8[0],
        name="الکتروپلیش کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_press = Component.objects.get_or_create(
        id=814, category=component_category_press[0], product=product_kafshoor_grill_point_30_8[0],
        name="پرس کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_paper = Component.objects.get_or_create(
        id=815, category=component_category_paper[0], product=product_kafshoor_grill_point_30_8[0],
        name="کاغذ تبلیغ کفشور 8 * 30 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_30_8_grill_point = Component.objects.get_or_create(
        id=816, category=component_category_grill_point[0], product=product_kafshoor_grill_point_30_8[0],
        name="گریل نقطه ای کفشور 8 * 30 گریل نقطه ای", description='', used_count=72,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 45 * 8
    product_kafshoor_grill_point_45_8 = Product.objects.get_or_create(
        id=57, name="کفشور 8 * 45 گریل نقطه ای", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Point Grill 45 * 8
    component_kafshoor_grill_point_45_8_steel_15 = Component.objects.get_or_create(
        id=821, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_45_8[0],
        name="ورق استیل کفشور 8 * 45 گریل نقطه ای", description='', used_count=121935,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_flappy = Component.objects.get_or_create(
        id=822, category=component_category_flappy[0], product=product_kafshoor_grill_point_45_8[0],
        name="فلاپی کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_45_8_pipe = Component.objects.get_or_create(
        id=823, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_45_8[0],
        name="لوله کفشور 8 * 45 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_pipe_cutting = Component.objects.get_or_create(
        id=824, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_45_8[0],
        name="برش لوله کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_laser_gas = Component.objects.get_or_create(
        id=825, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_45_8[0],
        name="لیزر و گاز کفشور 8 * 45 گریل نقطه ای", description='', used_count=2578,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_screw_30 = Component.objects.get_or_create(
        id=826, category=component_category_screw_30[0], product=product_kafshoor_grill_point_45_8[0],
        name="پیچ 3 سانتی کفشور 8 * 45 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_fasten = Component.objects.get_or_create(
        id=827, category=component_category_fasten[0], product=product_kafshoor_grill_point_45_8[0],
        name="بست کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_bend = Component.objects.get_or_create(
        id=828, category=component_category_bend[0], product=product_kafshoor_grill_point_45_8[0],
        name="خم کفشور 8 * 45 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_spring = Component.objects.get_or_create(
        id=829, category=component_category_spring[0], product=product_kafshoor_grill_point_45_8[0],
        name="فنر کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_key = Component.objects.get_or_create(
        id=830, category=component_category_key[0], product=product_kafshoor_grill_point_45_8[0],
        name="کلید کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_weld = Component.objects.get_or_create(
        id=831, category=component_category_weld[0], product=product_kafshoor_grill_point_45_8[0],
        name="جوش کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_reamer = Component.objects.get_or_create(
        id=832, category=component_category_reamer[0], product=product_kafshoor_grill_point_45_8[0],
        name="قلاویز کفشور 8 * 45 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_electropolish = Component.objects.get_or_create(
        id=833, category=component_category_electropolish[0], product=product_kafshoor_grill_point_45_8[0],
        name="الکتروپلیش کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_press = Component.objects.get_or_create(
        id=834, category=component_category_press[0], product=product_kafshoor_grill_point_45_8[0],
        name="پرس کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_paper = Component.objects.get_or_create(
        id=835, category=component_category_paper[0], product=product_kafshoor_grill_point_45_8[0],
        name="کاغذ تبلیغ کفشور 8 * 45 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_45_8_grill_point = Component.objects.get_or_create(
        id=836, category=component_category_grill_point[0], product=product_kafshoor_grill_point_45_8[0],
        name="گریل نقطه ای کفشور 8 * 45 گریل نقطه ای", description='', used_count=112,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 60 * 8
    product_kafshoor_grill_point_60_8 = Product.objects.get_or_create(
        id=58, name="کفشور 8 * 60 گریل نقطه ای", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Point Grill 60 * 8
    component_kafshoor_grill_point_60_8_steel_15 = Component.objects.get_or_create(
        id=841, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_60_8[0],
        name="ورق استیل کفشور 8 * 60 گریل نقطه ای", description='', used_count=158985,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_flappy = Component.objects.get_or_create(
        id=842, category=component_category_flappy[0], product=product_kafshoor_grill_point_60_8[0],
        name="فلاپی کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_60_8_pipe = Component.objects.get_or_create(
        id=843, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_60_8[0],
        name="لوله کفشور 8 * 60 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_pipe_cutting = Component.objects.get_or_create(
        id=844, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_60_8[0],
        name="برش لوله کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_laser_gas = Component.objects.get_or_create(
        id=845, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_60_8[0],
        name="لیزر و گاز کفشور 8 * 60 گریل نقطه ای", description='', used_count=3178,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_screw_30 = Component.objects.get_or_create(
        id=846, category=component_category_screw_30[0], product=product_kafshoor_grill_point_60_8[0],
        name="پیچ 3 سانتی کفشور 8 * 60 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_fasten = Component.objects.get_or_create(
        id=847, category=component_category_fasten[0], product=product_kafshoor_grill_point_60_8[0],
        name="بست کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_bend = Component.objects.get_or_create(
        id=848, category=component_category_bend[0], product=product_kafshoor_grill_point_60_8[0],
        name="خم کفشور 8 * 60 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_spring = Component.objects.get_or_create(
        id=849, category=component_category_spring[0], product=product_kafshoor_grill_point_60_8[0],
        name="فنر کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_key = Component.objects.get_or_create(
        id=850, category=component_category_key[0], product=product_kafshoor_grill_point_60_8[0],
        name="کلید کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_weld = Component.objects.get_or_create(
        id=851, category=component_category_weld[0], product=product_kafshoor_grill_point_60_8[0],
        name="جوش کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_reamer = Component.objects.get_or_create(
        id=852, category=component_category_reamer[0], product=product_kafshoor_grill_point_60_8[0],
        name="قلاویز کفشور 8 * 60 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_electropolish = Component.objects.get_or_create(
        id=853, category=component_category_electropolish[0], product=product_kafshoor_grill_point_60_8[0],
        name="الکتروپلیش کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_press = Component.objects.get_or_create(
        id=854, category=component_category_press[0], product=product_kafshoor_grill_point_60_8[0],
        name="پرس کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_paper = Component.objects.get_or_create(
        id=855, category=component_category_paper[0], product=product_kafshoor_grill_point_60_8[0],
        name="کاغذ تبلیغ کفشور 8 * 60 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_60_8_grill_point = Component.objects.get_or_create(
        id=856, category=component_category_grill_point[0], product=product_kafshoor_grill_point_60_8[0],
        name="گریل نقطه ای کفشور 8 * 60 گریل نقطه ای", description='', used_count=152,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 80 * 8
    product_kafshoor_grill_point_80_8 = Product.objects.get_or_create(
        id=59, name="کفشور 8 * 80 گریل نقطه ای", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Point Grill 80 * 8
    component_kafshoor_grill_point_80_8_steel_15 = Component.objects.get_or_create(
        id=861, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_80_8[0],
        name="ورق استیل کفشور 8 * 80 گریل نقطه ای", description='', used_count=208385,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_flappy = Component.objects.get_or_create(
        id=862, category=component_category_flappy[0], product=product_kafshoor_grill_point_80_8[0],
        name="فلاپی کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_80_8_pipe = Component.objects.get_or_create(
        id=863, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_80_8[0],
        name="لوله کفشور 8 * 80 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_pipe_cutting = Component.objects.get_or_create(
        id=864, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_80_8[0],
        name="برش لوله کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_laser_gas = Component.objects.get_or_create(
        id=865, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_80_8[0],
        name="لیزر و گاز کفشور 8 * 80 گریل نقطه ای", description='', used_count=3978,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_screw_30 = Component.objects.get_or_create(
        id=866, category=component_category_screw_30[0], product=product_kafshoor_grill_point_80_8[0],
        name="پیچ 3 سانتی کفشور 8 * 80 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_fasten = Component.objects.get_or_create(
        id=867, category=component_category_fasten[0], product=product_kafshoor_grill_point_80_8[0],
        name="بست کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_bend = Component.objects.get_or_create(
        id=868, category=component_category_bend[0], product=product_kafshoor_grill_point_80_8[0],
        name="خم کفشور 8 * 80 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_spring = Component.objects.get_or_create(
        id=869, category=component_category_spring[0], product=product_kafshoor_grill_point_80_8[0],
        name="فنر کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_key = Component.objects.get_or_create(
        id=870, category=component_category_key[0], product=product_kafshoor_grill_point_80_8[0],
        name="کلید کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_weld = Component.objects.get_or_create(
        id=871, category=component_category_weld[0], product=product_kafshoor_grill_point_80_8[0],
        name="جوش کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_reamer = Component.objects.get_or_create(
        id=872, category=component_category_reamer[0], product=product_kafshoor_grill_point_80_8[0],
        name="قلاویز کفشور 8 * 80 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_electropolish = Component.objects.get_or_create(
        id=873, category=component_category_electropolish[0], product=product_kafshoor_grill_point_80_8[0],
        name="الکتروپلیش کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_press = Component.objects.get_or_create(
        id=874, category=component_category_press[0], product=product_kafshoor_grill_point_80_8[0],
        name="پرس کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_paper = Component.objects.get_or_create(
        id=875, category=component_category_paper[0], product=product_kafshoor_grill_point_80_8[0],
        name="کاغذ تبلیغ کفشور 8 * 80 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_80_8_grill_point = Component.objects.get_or_create(
        id=876, category=component_category_grill_point[0], product=product_kafshoor_grill_point_80_8[0],
        name="گریل نقطه ای کفشور 8 * 80 گریل نقطه ای", description='', used_count=204,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 90 * 8
    product_kafshoor_grill_point_90_8 = Product.objects.get_or_create(
        id=60, name="کفشور 8 * 90 گریل نقطه ای", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Point Grill 90 * 8
    component_kafshoor_grill_point_90_8_steel_15 = Component.objects.get_or_create(
        id=881, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_90_8[0],
        name="ورق استیل کفشور 8 * 90 گریل نقطه ای", description='', used_count=233085,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_flappy = Component.objects.get_or_create(
        id=882, category=component_category_flappy[0], product=product_kafshoor_grill_point_90_8[0],
        name="فلاپی کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_90_8_pipe = Component.objects.get_or_create(
        id=883, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_90_8[0],
        name="لوله کفشور 8 * 90 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_pipe_cutting = Component.objects.get_or_create(
        id=884, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_90_8[0],
        name="برش لوله کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_laser_gas = Component.objects.get_or_create(
        id=885, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_90_8[0],
        name="لیزر و گاز کفشور 8 * 90 گریل نقطه ای", description='', used_count=4378,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_screw_30 = Component.objects.get_or_create(
        id=886, category=component_category_screw_30[0], product=product_kafshoor_grill_point_90_8[0],
        name="پیچ 3 سانتی کفشور 8 * 90 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_fasten = Component.objects.get_or_create(
        id=887, category=component_category_fasten[0], product=product_kafshoor_grill_point_90_8[0],
        name="بست کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_bend = Component.objects.get_or_create(
        id=888, category=component_category_bend[0], product=product_kafshoor_grill_point_90_8[0],
        name="خم کفشور 8 * 90 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_spring = Component.objects.get_or_create(
        id=889, category=component_category_spring[0], product=product_kafshoor_grill_point_90_8[0],
        name="فنر کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_key = Component.objects.get_or_create(
        id=890, category=component_category_key[0], product=product_kafshoor_grill_point_90_8[0],
        name="کلید کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_weld = Component.objects.get_or_create(
        id=891, category=component_category_weld[0], product=product_kafshoor_grill_point_90_8[0],
        name="جوش کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_reamer = Component.objects.get_or_create(
        id=892, category=component_category_reamer[0], product=product_kafshoor_grill_point_90_8[0],
        name="قلاویز کفشور 8 * 90 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_electropolish = Component.objects.get_or_create(
        id=893, category=component_category_electropolish[0], product=product_kafshoor_grill_point_90_8[0],
        name="الکتروپلیش کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_press = Component.objects.get_or_create(
        id=894, category=component_category_press[0], product=product_kafshoor_grill_point_90_8[0],
        name="پرس کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_paper = Component.objects.get_or_create(
        id=895, category=component_category_paper[0], product=product_kafshoor_grill_point_90_8[0],
        name="کاغذ تبلیغ کفشور 8 * 90 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_90_8_grill_point = Component.objects.get_or_create(
        id=896, category=component_category_grill_point[0], product=product_kafshoor_grill_point_90_8[0],
        name="گریل نقطه ای کفشور 8 * 90 گریل نقطه ای", description='', used_count=232,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Point Grill 100 * 8
    product_kafshoor_grill_point_100_8 = Product.objects.get_or_create(
        id=61, name="کفشور 8 * 100 گریل نقطه ای", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Point Grill 100 * 8
    component_kafshoor_grill_point_100_8_steel_15 = Component.objects.get_or_create(
        id=901, category=component_category_steel_304_15[0], product=product_kafshoor_grill_point_100_8[0],
        name="ورق استیل کفشور 8 * 100 گریل نقطه ای", description='', used_count=257785,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_flappy = Component.objects.get_or_create(
        id=902, category=component_category_flappy[0], product=product_kafshoor_grill_point_100_8[0],
        name="فلاپی کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_point_100_8_pipe = Component.objects.get_or_create(
        id=903, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_point_100_8[0],
        name="لوله کفشور 8 * 100 گریل نقطه ای", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_pipe_cutting = Component.objects.get_or_create(
        id=904, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_point_100_8[0],
        name="برش لوله کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_laser_gas = Component.objects.get_or_create(
        id=905, category=component_category_laser_gas[0], product=product_kafshoor_grill_point_100_8[0],
        name="لیزر و گاز کفشور 8 * 100 گریل نقطه ای", description='', used_count=4778,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_screw_30 = Component.objects.get_or_create(
        id=906, category=component_category_screw_30[0], product=product_kafshoor_grill_point_100_8[0],
        name="پیچ 3 سانتی کفشور 8 * 100 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_fasten = Component.objects.get_or_create(
        id=907, category=component_category_fasten[0], product=product_kafshoor_grill_point_100_8[0],
        name="بست کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_bend = Component.objects.get_or_create(
        id=908, category=component_category_bend[0], product=product_kafshoor_grill_point_100_8[0],
        name="خم کفشور 8 * 100 گریل نقطه ای", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_spring = Component.objects.get_or_create(
        id=909, category=component_category_spring[0], product=product_kafshoor_grill_point_100_8[0],
        name="فنر کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_key = Component.objects.get_or_create(
        id=910, category=component_category_key[0], product=product_kafshoor_grill_point_100_8[0],
        name="کلید کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_weld = Component.objects.get_or_create(
        id=911, category=component_category_weld[0], product=product_kafshoor_grill_point_100_8[0],
        name="جوش کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_reamer = Component.objects.get_or_create(
        id=912, category=component_category_reamer[0], product=product_kafshoor_grill_point_100_8[0],
        name="قلاویز کفشور 8 * 100 گریل نقطه ای", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_electropolish = Component.objects.get_or_create(
        id=913, category=component_category_electropolish[0], product=product_kafshoor_grill_point_100_8[0],
        name="الکتروپلیش کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_press = Component.objects.get_or_create(
        id=914, category=component_category_press[0], product=product_kafshoor_grill_point_100_8[0],
        name="پرس کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_paper = Component.objects.get_or_create(
        id=915, category=component_category_paper[0], product=product_kafshoor_grill_point_100_8[0],
        name="کاغذ تبلیغ کفشور 8 * 100 گریل نقطه ای", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_point_100_8_grill_point = Component.objects.get_or_create(
        id=916, category=component_category_grill_point[0], product=product_kafshoor_grill_point_100_8[0],
        name="گریل نقطه ای کفشور 8 * 100 گریل نقطه ای", description='', used_count=258,
        per_product=1
    )

    # =================================================================================
    # Line Grill
    # =================================================================================

    # Create Product Kafshoor Line Grill 10 * 10
    product_kafshoor_grill_line_10_10 = Product.objects.get_or_create(
        id=71, name="کفشور 10 * 10 گریل خطی", description='', no_prod_per_year=260,
    )

    # Create Components for Kafshoor Line Grill 10 * 10
    component_kafshoor_grill_line_10_10_steel_15 = Component.objects.get_or_create(
        id=1001, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_10_10[0],
        name="ورق استیل کفشور 10 * 10 گریل خطی", description='', used_count=41225,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_flappy = Component.objects.get_or_create(
        id=1002, category=component_category_flappy[0], product=product_kafshoor_grill_line_10_10[0],
        name="فلاپی کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_10_10_pipe = Component.objects.get_or_create(
        id=1003, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_10_10[0],
        name="لوله کفشور 10 * 10 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_pipe_cutting = Component.objects.get_or_create(
        id=1004, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_10_10[0],
        name="برش لوله کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_laser_gas = Component.objects.get_or_create(
        id=1005, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_10_10[0],
        name="لیزر و گاز کفشور 10 * 10 گریل خطی", description='', used_count=1258,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_bend = Component.objects.get_or_create(
        id=1006, category=component_category_bend[0], product=product_kafshoor_grill_line_10_10[0],
        name="خم کفشور 10 * 10 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_spring = Component.objects.get_or_create(
        id=1007, category=component_category_spring[0], product=product_kafshoor_grill_line_10_10[0],
        name="فنر کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_key = Component.objects.get_or_create(
        id=1008, category=component_category_key[0], product=product_kafshoor_grill_line_10_10[0],
        name="کلید کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_weld = Component.objects.get_or_create(
        id=1009, category=component_category_weld[0], product=product_kafshoor_grill_line_10_10[0],
        name="جوش کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_reamer = Component.objects.get_or_create(
        id=1010, category=component_category_reamer[0], product=product_kafshoor_grill_line_10_10[0],
        name="قلاویز کفشور 10 * 10 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_electropolish = Component.objects.get_or_create(
        id=1011, category=component_category_electropolish[0], product=product_kafshoor_grill_line_10_10[0],
        name="الکتروپلیش کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_press = Component.objects.get_or_create(
        id=1012, category=component_category_press[0], product=product_kafshoor_grill_line_10_10[0],
        name="پرس کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_paper = Component.objects.get_or_create(
        id=1013, category=component_category_paper[0], product=product_kafshoor_grill_line_10_10[0],
        name="کاغذ تبلیغ کفشور 10 * 10 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_10_10_grill_line = Component.objects.get_or_create(
        id=1014, category=component_category_grill_line[0], product=product_kafshoor_grill_line_10_10[0],
        name="گریل خطی کفشور 10 * 10 گریل خطی", description='', used_count=6,
        per_product=1
    )

    # =======================================================================================

    # Create Product Kafshoor Line Grill 12 * 12
    product_kafshoor_grill_line_12_12 = Product.objects.get_or_create(
        id=72, name="کفشور 12 * 12 گریل خطی", description='', no_prod_per_year=45,
    )

    # Create Components for Kafshoor Line Grill 10 * 10
    component_kafshoor_grill_line_12_12_steel_15 = Component.objects.get_or_create(
        id=1021, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_12_12[0],
        name="ورق استیل کفشور 12 * 12 گریل خطی", description='', used_count=53505,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_flappy = Component.objects.get_or_create(
        id=1022, category=component_category_flappy[0], product=product_kafshoor_grill_line_12_12[0],
        name="فلاپی کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_12_12_pipe = Component.objects.get_or_create(
        id=1023, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_12_12[0],
        name="لوله کفشور 12 * 12 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_pipe_cutting = Component.objects.get_or_create(
        id=1024, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_12_12[0],
        name="برش لوله کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_laser_gas = Component.objects.get_or_create(
        id=1025, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_12_12[0],
        name="لیزر و گاز کفشور 12 * 12 گریل خطی", description='', used_count=1418,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_bend = Component.objects.get_or_create(
        id=1026, category=component_category_bend[0], product=product_kafshoor_grill_line_12_12[0],
        name="خم کفشور 12 * 12 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_spring = Component.objects.get_or_create(
        id=1027, category=component_category_spring[0], product=product_kafshoor_grill_line_12_12[0],
        name="فنر کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_key = Component.objects.get_or_create(
        id=1028, category=component_category_key[0], product=product_kafshoor_grill_line_12_12[0],
        name="کلید کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_weld = Component.objects.get_or_create(
        id=1029, category=component_category_weld[0], product=product_kafshoor_grill_line_12_12[0],
        name="جوش کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_reamer = Component.objects.get_or_create(
        id=1030, category=component_category_reamer[0], product=product_kafshoor_grill_line_12_12[0],
        name="قلاویز کفشور 12 * 12 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_electropolish = Component.objects.get_or_create(
        id=1031, category=component_category_electropolish[0], product=product_kafshoor_grill_line_12_12[0],
        name="الکتروپلیش کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_press = Component.objects.get_or_create(
        id=1032, category=component_category_press[0], product=product_kafshoor_grill_line_12_12[0],
        name="پرس کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_paper = Component.objects.get_or_create(
        id=1033, category=component_category_paper[0], product=product_kafshoor_grill_line_12_12[0],
        name="کاغذ تبلیغ کفشور 12 * 12 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_12_12_grill_line = Component.objects.get_or_create(
        id=1034, category=component_category_grill_line[0], product=product_kafshoor_grill_line_12_12[0],
        name="گریل خطی کفشور 12 * 12 گریل خطی", description='', used_count=14,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 15 * 15
    product_kafshoor_grill_line_15_15 = Product.objects.get_or_create(
        id=73, name="کفشور 15 * 15 گریل خطی", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Line Grill 15 * 15
    component_kafshoor_grill_line_15_15_steel_15 = Component.objects.get_or_create(
        id=1041, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_15_15[0],
        name="ورق استیل کفشور 15 * 15 گریل خطی", description='', used_count=74925,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_flappy = Component.objects.get_or_create(
        id=1042, category=component_category_flappy[0], product=product_kafshoor_grill_line_15_15[0],
        name="فلاپی کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_15_15_pipe = Component.objects.get_or_create(
        id=1043, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_15_15[0],
        name="لوله کفشور 15 * 15 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_pipe_cutting = Component.objects.get_or_create(
        id=1044, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_15_15[0],
        name="برش لوله کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_laser_gas = Component.objects.get_or_create(
        id=1045, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_15_15[0],
        name="لیزر و گاز کفشور 15 * 15 گریل خطی", description='', used_count=458,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_bend = Component.objects.get_or_create(
        id=1046, category=component_category_bend[0], product=product_kafshoor_grill_line_15_15[0],
        name="خم کفشور 15 * 15 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_spring = Component.objects.get_or_create(
        id=1047, category=component_category_spring[0], product=product_kafshoor_grill_line_15_15[0],
        name="فنر کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_key = Component.objects.get_or_create(
        id=1048, category=component_category_key[0], product=product_kafshoor_grill_line_15_15[0],
        name="کلید کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_weld = Component.objects.get_or_create(
        id=1049, category=component_category_weld[0], product=product_kafshoor_grill_line_15_15[0],
        name="جوش کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_reamer = Component.objects.get_or_create(
        id=1050, category=component_category_reamer[0], product=product_kafshoor_grill_line_15_15[0],
        name="قلاویز کفشور 15 * 15 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_electropolish = Component.objects.get_or_create(
        id=1051, category=component_category_electropolish[0], product=product_kafshoor_grill_line_15_15[0],
        name="الکتروپلیش کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_press = Component.objects.get_or_create(
        id=1052, category=component_category_press[0], product=product_kafshoor_grill_line_15_15[0],
        name="پرس کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_paper = Component.objects.get_or_create(
        id=1053, category=component_category_paper[0], product=product_kafshoor_grill_line_15_15[0],
        name="کاغذ تبلیغ کفشور 15 * 15 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_15_15_grill_line = Component.objects.get_or_create(
        id=1054, category=component_category_grill_line[0], product=product_kafshoor_grill_line_15_15[0],
        name="گریل خطی کفشور 15 * 15 گریل خطی", description='', used_count=16,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 17 * 17
    product_kafshoor_grill_line_17_17 = Product.objects.get_or_create(
        id=74, name="کفشور 17 * 17 گریل خطی", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Line Grill 17 * 17
    component_kafshoor_grill_line_17_17_steel_15 = Component.objects.get_or_create(
        id=1061, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_17_17[0],
        name="ورق استیل کفشور 17 * 17 گریل خطی", description='', used_count=91205,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_flappy = Component.objects.get_or_create(
        id=1062, category=component_category_flappy[0], product=product_kafshoor_grill_line_17_17[0],
        name="فلاپی کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_17_17_pipe = Component.objects.get_or_create(
        id=1063, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_17_17[0],
        name="لوله کفشور 17 * 17 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_pipe_cutting = Component.objects.get_or_create(
        id=1064, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_17_17[0],
        name="برش لوله کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_laser_gas = Component.objects.get_or_create(
        id=1065, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_17_17[0],
        name="لیزر و گاز کفشور 17 * 17 گریل خطی", description='', used_count=1818,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_bend = Component.objects.get_or_create(
        id=1066, category=component_category_bend[0], product=product_kafshoor_grill_line_17_17[0],
        name="خم کفشور 17 * 17 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_spring = Component.objects.get_or_create(
        id=1067, category=component_category_spring[0], product=product_kafshoor_grill_line_17_17[0],
        name="فنر کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_key = Component.objects.get_or_create(
        id=1068, category=component_category_key[0], product=product_kafshoor_grill_line_17_17[0],
        name="کلید کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_weld = Component.objects.get_or_create(
        id=1069, category=component_category_weld[0], product=product_kafshoor_grill_line_17_17[0],
        name="جوش کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_reamer = Component.objects.get_or_create(
        id=1070, category=component_category_reamer[0], product=product_kafshoor_grill_line_17_17[0],
        name="قلاویز کفشور 17 * 17 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_electropolish = Component.objects.get_or_create(
        id=1071, category=component_category_electropolish[0], product=product_kafshoor_grill_line_17_17[0],
        name="الکتروپلیش کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_press = Component.objects.get_or_create(
        id=1072, category=component_category_press[0], product=product_kafshoor_grill_line_17_17[0],
        name="پرس کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_paper = Component.objects.get_or_create(
        id=1073, category=component_category_paper[0], product=product_kafshoor_grill_line_17_17[0],
        name="کاغذ تبلیغ کفشور 17 * 17 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_17_17_grill_line = Component.objects.get_or_create(
        id=1074, category=component_category_grill_line[0], product=product_kafshoor_grill_line_17_17[0],
        name="گریل خطی کفشور 17 * 17 گریل خطی", description='', used_count=18,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 20 * 20
    product_kafshoor_grill_line_20_20 = Product.objects.get_or_create(
        id=75, name="کفشور 20 * 20 گریل خطی", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Line Grill 20 * 20
    component_kafshoor_grill_line_20_20_steel_15 = Component.objects.get_or_create(
        id=1081, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_20_20[0],
        name="ورق استیل کفشور 20 * 20 گریل خطی", description='', used_count=118625,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_flappy = Component.objects.get_or_create(
        id=1082, category=component_category_flappy[0], product=product_kafshoor_grill_line_20_20[0],
        name="فلاپی کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_20_20_pipe = Component.objects.get_or_create(
        id=1083, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_20_20[0],
        name="لوله کفشور 20 * 20 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_pipe_cutting = Component.objects.get_or_create(
        id=1084, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_20_20[0],
        name="برش لوله کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_laser_gas = Component.objects.get_or_create(
        id=1085, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_20_20[0],
        name="لیزر و گاز کفشور 20 * 20 گریل خطی", description='', used_count=2058,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_bend = Component.objects.get_or_create(
        id=1086, category=component_category_bend[0], product=product_kafshoor_grill_line_20_20[0],
        name="خم کفشور 20 * 20 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_spring = Component.objects.get_or_create(
        id=1087, category=component_category_spring[0], product=product_kafshoor_grill_line_20_20[0],
        name="فنر کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_key = Component.objects.get_or_create(
        id=1088, category=component_category_key[0], product=product_kafshoor_grill_line_20_20[0],
        name="کلید کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_weld = Component.objects.get_or_create(
        id=1089, category=component_category_weld[0], product=product_kafshoor_grill_line_20_20[0],
        name="جوش کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_reamer = Component.objects.get_or_create(
        id=1090, category=component_category_reamer[0], product=product_kafshoor_grill_line_20_20[0],
        name="قلاویز کفشور 20 * 20 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_electropolish = Component.objects.get_or_create(
        id=1091, category=component_category_electropolish[0], product=product_kafshoor_grill_line_20_20[0],
        name="الکتروپلیش کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_press = Component.objects.get_or_create(
        id=1092, category=component_category_press[0], product=product_kafshoor_grill_line_20_20[0],
        name="پرس کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_paper = Component.objects.get_or_create(
        id=1093, category=component_category_paper[0], product=product_kafshoor_grill_line_20_20[0],
        name="کاغذ تبلیغ کفشور 20 * 20 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_20_20_grill_line = Component.objects.get_or_create(
        id=1094, category=component_category_grill_line[0], product=product_kafshoor_grill_line_10_10[0],
        name="گریل خطی کفشور 20 * 20 گریل خطی", description='', used_count=20,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 30 * 8
    product_kafshoor_grill_line_30_8 = Product.objects.get_or_create(
        id=76, name="کفشور 8 * 30 گریل خطی", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Line Grill 30 * 8
    component_kafshoor_grill_line_30_8_steel_15 = Component.objects.get_or_create(
        id=1101, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_30_8[0],
        name="ورق استیل کفشور 8 * 30 گریل خطی", description='', used_count=84885,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_flappy = Component.objects.get_or_create(
        id=1102, category=component_category_flappy[0], product=product_kafshoor_grill_line_30_8[0],
        name="فلاپی کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_30_8_pipe = Component.objects.get_or_create(
        id=1103, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_30_8[0],
        name="لوله کفشور 8 * 30 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_pipe_cutting = Component.objects.get_or_create(
        id=1104, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_30_8[0],
        name="برش لوله کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_laser_gas = Component.objects.get_or_create(
        id=1105, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_30_8[0],
        name="لیزر و گاز کفشور 8 * 30 گریل خطی", description='', used_count=1978,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_screw_30 = Component.objects.get_or_create(
        id=1106, category=component_category_screw_30[0], product=product_kafshoor_grill_line_30_8[0],
        name="پیچ 3 سانتی کفشور 8 * 30 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_fasten = Component.objects.get_or_create(
        id=1107, category=component_category_fasten[0], product=product_kafshoor_grill_line_30_8[0],
        name="بست کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_bend = Component.objects.get_or_create(
        id=1108, category=component_category_bend[0], product=product_kafshoor_grill_line_30_8[0],
        name="خم کفشور 8 * 30 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_spring = Component.objects.get_or_create(
        id=1109, category=component_category_spring[0], product=product_kafshoor_grill_line_30_8[0],
        name="فنر کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_key = Component.objects.get_or_create(
        id=1110, category=component_category_key[0], product=product_kafshoor_grill_line_30_8[0],
        name="کلید کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_weld = Component.objects.get_or_create(
        id=1111, category=component_category_weld[0], product=product_kafshoor_grill_line_30_8[0],
        name="جوش کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoorstone_30_8_reamer = Component.objects.get_or_create(
        id=1112, category=component_category_reamer[0], product=product_kafshoor_grill_line_30_8[0],
        name="قلاویز کفشور 8 * 30 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_electropolish = Component.objects.get_or_create(
        id=1113, category=component_category_electropolish[0], product=product_kafshoor_grill_line_30_8[0],
        name="الکتروپلیش کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_press = Component.objects.get_or_create(
        id=1114, category=component_category_press[0], product=product_kafshoor_grill_line_30_8[0],
        name="پرس کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_paper = Component.objects.get_or_create(
        id=1115, category=component_category_paper[0], product=product_kafshoor_grill_line_30_8[0],
        name="کاغذ تبلیغ کفشور 8 * 30 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_30_8_grill_line = Component.objects.get_or_create(
        id=1116, category=component_category_grill_line[0], product=product_kafshoor_grill_line_30_8[0],
        name="گریل خطی کفشور 8 * 30 گریل خطی", description='', used_count=16,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 45 * 8
    product_kafshoor_grill_line_45_8 = Product.objects.get_or_create(
        id=77, name="کفشور 8 * 45 گریل خطی", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Line Grill 45 * 8
    component_kafshoor_grill_line_45_8_steel_15 = Component.objects.get_or_create(
        id=1121, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_45_8[0],
        name="ورق استیل کفشور 8 * 45 گریل خطی", description='', used_count=121935,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_flappy = Component.objects.get_or_create(
        id=1122, category=component_category_flappy[0], product=product_kafshoor_grill_line_45_8[0],
        name="فلاپی کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_45_8_pipe = Component.objects.get_or_create(
        id=1123, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_45_8[0],
        name="لوله کفشور 8 * 45 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_pipe_cutting = Component.objects.get_or_create(
        id=1124, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_45_8[0],
        name="برش لوله کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_laser_gas = Component.objects.get_or_create(
        id=1125, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_45_8[0],
        name="لیزر و گاز کفشور 8 * 45 گریل خطی", description='', used_count=2578,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_screw_30 = Component.objects.get_or_create(
        id=1126, category=component_category_screw_30[0], product=product_kafshoor_grill_line_45_8[0],
        name="پیچ 3 سانتی کفشور 8 * 45 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_fasten = Component.objects.get_or_create(
        id=1127, category=component_category_fasten[0], product=product_kafshoor_grill_line_45_8[0],
        name="بست کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_bend = Component.objects.get_or_create(
        id=1128, category=component_category_bend[0], product=product_kafshoor_grill_line_45_8[0],
        name="خم کفشور 8 * 45 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_spring = Component.objects.get_or_create(
        id=1129, category=component_category_spring[0], product=product_kafshoor_grill_line_45_8[0],
        name="فنر کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_key = Component.objects.get_or_create(
        id=1130, category=component_category_key[0], product=product_kafshoor_grill_line_45_8[0],
        name="کلید کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_weld = Component.objects.get_or_create(
        id=1131, category=component_category_weld[0], product=product_kafshoor_grill_line_45_8[0],
        name="جوش کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_reamer = Component.objects.get_or_create(
        id=1132, category=component_category_reamer[0], product=product_kafshoor_grill_line_45_8[0],
        name="قلاویز کفشور 8 * 45 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_electropolish = Component.objects.get_or_create(
        id=1133, category=component_category_electropolish[0], product=product_kafshoor_grill_line_45_8[0],
        name="الکتروپلیش کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_press = Component.objects.get_or_create(
        id=1134, category=component_category_press[0], product=product_kafshoor_grill_line_45_8[0],
        name="پرس کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_paper = Component.objects.get_or_create(
        id=1135, category=component_category_paper[0], product=product_kafshoor_grill_line_45_8[0],
        name="کاغذ تبلیغ کفشور 8 * 45 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_45_8_grill_line = Component.objects.get_or_create(
        id=1136, category=component_category_grill_line[0], product=product_kafshoor_grill_line_45_8[0],
        name="گریل خطی کفشور 8 * 45 گریل خطی", description='', used_count=22,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 60 * 8
    product_kafshoor_grill_line_60_8 = Product.objects.get_or_create(
        id=78, name="کفشور 8 * 60 گریل خطی", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Line Grill 60 * 8
    component_kafshoor_grill_line_60_8_steel_15 = Component.objects.get_or_create(
        id=1141, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_60_8[0],
        name="ورق استیل کفشور 8 * 60 گریل خطی", description='', used_count=158985,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_flappy = Component.objects.get_or_create(
        id=1142, category=component_category_flappy[0], product=product_kafshoor_grill_line_60_8[0],
        name="فلاپی کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_60_8_pipe = Component.objects.get_or_create(
        id=1143, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_60_8[0],
        name="لوله کفشور 8 * 60 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_pipe_cutting = Component.objects.get_or_create(
        id=1144, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_60_8[0],
        name="برش لوله کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_laser_gas = Component.objects.get_or_create(
        id=1145, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_60_8[0],
        name="لیزر و گاز کفشور 8 * 60 گریل خطی", description='', used_count=3178,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_screw_30 = Component.objects.get_or_create(
        id=1146, category=component_category_screw_30[0], product=product_kafshoor_grill_line_60_8[0],
        name="پیچ 3 سانتی کفشور 8 * 60 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_fasten = Component.objects.get_or_create(
        id=1147, category=component_category_fasten[0], product=product_kafshoor_grill_line_60_8[0],
        name="بست کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_bend = Component.objects.get_or_create(
        id=1148, category=component_category_bend[0], product=product_kafshoor_grill_line_60_8[0],
        name="خم کفشور 8 * 60 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_spring = Component.objects.get_or_create(
        id=1149, category=component_category_spring[0], product=product_kafshoor_grill_line_60_8[0],
        name="فنر کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_key = Component.objects.get_or_create(
        id=1150, category=component_category_key[0], product=product_kafshoor_grill_line_60_8[0],
        name="کلید کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_weld = Component.objects.get_or_create(
        id=1151, category=component_category_weld[0], product=product_kafshoor_grill_line_60_8[0],
        name="جوش کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_reamer = Component.objects.get_or_create(
        id=1152, category=component_category_reamer[0], product=product_kafshoor_grill_line_60_8[0],
        name="قلاویز کفشور 8 * 60 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_electropolish = Component.objects.get_or_create(
        id=1153, category=component_category_electropolish[0], product=product_kafshoor_grill_line_60_8[0],
        name="الکتروپلیش کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_press = Component.objects.get_or_create(
        id=1154, category=component_category_press[0], product=product_kafshoor_grill_line_60_8[0],
        name="پرس کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_paper = Component.objects.get_or_create(
        id=1155, category=component_category_paper[0], product=product_kafshoor_grill_line_60_8[0],
        name="کاغذ تبلیغ کفشور 8 * 60 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_60_8_grill_line = Component.objects.get_or_create(
        id=1156, category=component_category_grill_line[0], product=product_kafshoor_grill_line_60_8[0],
        name="گریل خطی کفشور 8 * 60 گریل خطی", description='', used_count=29,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 80 * 8
    product_kafshoor_grill_line_80_8 = Product.objects.get_or_create(
        id=79, name="کفشور 8 * 80 گریل خطی", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Line Grill 80 * 8
    component_kafshoor_grill_line_80_8_steel_15 = Component.objects.get_or_create(
        id=1161, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_80_8[0],
        name="ورق استیل کفشور 8 * 80 گریل خطی", description='', used_count=208385,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_flappy = Component.objects.get_or_create(
        id=1162, category=component_category_flappy[0], product=product_kafshoor_grill_line_80_8[0],
        name="فلاپی کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_80_8_pipe = Component.objects.get_or_create(
        id=1163, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_80_8[0],
        name="لوله کفشور 8 * 80 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_pipe_cutting = Component.objects.get_or_create(
        id=1164, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_80_8[0],
        name="برش لوله کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_laser_gas = Component.objects.get_or_create(
        id=1165, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_80_8[0],
        name="لیزر و گاز کفشور 8 * 80 گریل خطی", description='', used_count=3978,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_screw_30 = Component.objects.get_or_create(
        id=1166, category=component_category_screw_30[0], product=product_kafshoor_grill_line_80_8[0],
        name="پیچ 3 سانتی کفشور 8 * 80 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_fasten = Component.objects.get_or_create(
        id=1167, category=component_category_fasten[0], product=product_kafshoor_grill_line_80_8[0],
        name="بست کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_bend = Component.objects.get_or_create(
        id=1168, category=component_category_bend[0], product=product_kafshoor_grill_line_80_8[0],
        name="خم کفشور 8 * 80 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_spring = Component.objects.get_or_create(
        id=1169, category=component_category_spring[0], product=product_kafshoor_grill_line_80_8[0],
        name="فنر کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_key = Component.objects.get_or_create(
        id=1170, category=component_category_key[0], product=product_kafshoor_grill_line_80_8[0],
        name="کلید کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_weld = Component.objects.get_or_create(
        id=1171, category=component_category_weld[0], product=product_kafshoor_grill_line_80_8[0],
        name="جوش کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_reamer = Component.objects.get_or_create(
        id=1172, category=component_category_reamer[0], product=product_kafshoor_grill_line_80_8[0],
        name="قلاویز کفشور 8 * 80 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_electropolish = Component.objects.get_or_create(
        id=1173, category=component_category_electropolish[0], product=product_kafshoor_grill_line_80_8[0],
        name="الکتروپلیش کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_press = Component.objects.get_or_create(
        id=1174, category=component_category_press[0], product=product_kafshoor_grill_line_80_8[0],
        name="پرس کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_paper = Component.objects.get_or_create(
        id=1175, category=component_category_paper[0], product=product_kafshoor_grill_line_80_8[0],
        name="کاغذ تبلیغ کفشور 8 * 80 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_80_8_grill_line = Component.objects.get_or_create(
        id=1176, category=component_category_grill_line[0], product=product_kafshoor_grill_line_80_8[0],
        name="گریل خطی کفشور 8 * 80 گریل خطی", description='', used_count=39,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 90 * 8
    product_kafshoor_grill_line_90_8 = Product.objects.get_or_create(
        id=80, name="کفشور 8 * 90 گریل خطی", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Line Grill 90 * 8
    component_kafshoor_grill_line_90_8_steel_15 = Component.objects.get_or_create(
        id=1181, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_90_8[0],
        name="ورق استیل کفشور 8 * 90 گریل خطی", description='', used_count=233085,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_flappy = Component.objects.get_or_create(
        id=1182, category=component_category_flappy[0], product=product_kafshoor_grill_line_90_8[0],
        name="فلاپی کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_90_8_pipe = Component.objects.get_or_create(
        id=1183, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_90_8[0],
        name="لوله کفشور 8 * 90 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_pipe_cutting = Component.objects.get_or_create(
        id=1184, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_90_8[0],
        name="برش لوله کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_laser_gas = Component.objects.get_or_create(
        id=1185, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_90_8[0],
        name="لیزر و گاز کفشور 8 * 90 گریل خطی", description='', used_count=4378,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_screw_30 = Component.objects.get_or_create(
        id=1186, category=component_category_screw_30[0], product=product_kafshoor_grill_line_90_8[0],
        name="پیچ 3 سانتی کفشور 8 * 90 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_fasten = Component.objects.get_or_create(
        id=1187, category=component_category_fasten[0], product=product_kafshoor_grill_line_90_8[0],
        name="بست کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_bend = Component.objects.get_or_create(
        id=1188, category=component_category_bend[0], product=product_kafshoor_grill_line_90_8[0],
        name="خم کفشور 8 * 90 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_spring = Component.objects.get_or_create(
        id=1189, category=component_category_spring[0], product=product_kafshoor_grill_line_90_8[0],
        name="فنر کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_key = Component.objects.get_or_create(
        id=1190, category=component_category_key[0], product=product_kafshoor_grill_line_90_8[0],
        name="کلید کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_weld = Component.objects.get_or_create(
        id=1191, category=component_category_weld[0], product=product_kafshoor_grill_line_90_8[0],
        name="جوش کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_reamer = Component.objects.get_or_create(
        id=1192, category=component_category_reamer[0], product=product_kafshoor_grill_line_90_8[0],
        name="قلاویز کفشور 8 * 90 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_electropolish = Component.objects.get_or_create(
        id=1193, category=component_category_electropolish[0], product=product_kafshoor_grill_line_90_8[0],
        name="الکتروپلیش کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_press = Component.objects.get_or_create(
        id=1194, category=component_category_press[0], product=product_kafshoor_grill_line_90_8[0],
        name="پرس کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_paper = Component.objects.get_or_create(
        id=1195, category=component_category_paper[0], product=product_kafshoor_grill_line_90_8[0],
        name="کاغذ تبلیغ کفشور 8 * 90 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_90_8_grill_line = Component.objects.get_or_create(
        id=1196, category=component_category_grill_line[0], product=product_kafshoor_grill_line_90_8[0],
        name="گریل خطی کفشور 8 * 90 گریل خطی", description='', used_count=44,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Line Grill 100 * 8
    product_kafshoor_grill_line_100_8 = Product.objects.get_or_create(
        id=81, name="کفشور 8 * 100 گریل خطی", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Line Grill 100 * 8
    component_kafshoor_grill_line_100_8_steel_15 = Component.objects.get_or_create(
        id=1201, category=component_category_steel_304_15[0], product=product_kafshoor_grill_line_100_8[0],
        name="ورق استیل کفشور 8 * 100 گریل خطی", description='', used_count=257785,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_flappy = Component.objects.get_or_create(
        id=1202, category=component_category_flappy[0], product=product_kafshoor_grill_line_100_8[0],
        name="فلاپی کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_grill_line_100_8_pipe = Component.objects.get_or_create(
        id=1203, category=component_category_pipe_51_mil[0], product=product_kafshoor_grill_line_100_8[0],
        name="لوله کفشور 8 * 100 گریل خطی", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_pipe_cutting = Component.objects.get_or_create(
        id=1204, category=component_category_pipe_cutting[0], product=product_kafshoor_grill_line_100_8[0],
        name="برش لوله کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_laser_gas = Component.objects.get_or_create(
        id=1205, category=component_category_laser_gas[0], product=product_kafshoor_grill_line_100_8[0],
        name="لیزر و گاز کفشور 8 * 100 گریل خطی", description='', used_count=4778,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_screw_30 = Component.objects.get_or_create(
        id=1206, category=component_category_screw_30[0], product=product_kafshoor_grill_line_100_8[0],
        name="پیچ 3 سانتی کفشور 8 * 100 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_fasten = Component.objects.get_or_create(
        id=1207, category=component_category_fasten[0], product=product_kafshoor_grill_line_100_8[0],
        name="بست کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_bend = Component.objects.get_or_create(
        id=1208, category=component_category_bend[0], product=product_kafshoor_grill_line_100_8[0],
        name="خم کفشور 8 * 100 گریل خطی", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_spring = Component.objects.get_or_create(
        id=1209, category=component_category_spring[0], product=product_kafshoor_grill_line_100_8[0],
        name="فنر کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_key = Component.objects.get_or_create(
        id=1210, category=component_category_key[0], product=product_kafshoor_grill_line_100_8[0],
        name="کلید کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_weld = Component.objects.get_or_create(
        id=1211, category=component_category_weld[0], product=product_kafshoor_grill_line_100_8[0],
        name="جوش کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_reamer = Component.objects.get_or_create(
        id=1212, category=component_category_reamer[0], product=product_kafshoor_grill_line_100_8[0],
        name="قلاویز کفشور 8 * 100 گریل خطی", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_electropolish = Component.objects.get_or_create(
        id=1213, category=component_category_electropolish[0], product=product_kafshoor_grill_line_100_8[0],
        name="الکتروپلیش کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_press = Component.objects.get_or_create(
        id=1214, category=component_category_press[0], product=product_kafshoor_grill_line_100_8[0],
        name="پرس کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_paper = Component.objects.get_or_create(
        id=1215, category=component_category_paper[0], product=product_kafshoor_grill_line_100_8[0],
        name="کاغذ تبلیغ کفشور 8 * 100 گریل خطی", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_grill_line_100_8_grill_line = Component.objects.get_or_create(
        id=1216, category=component_category_grill_line[0], product=product_kafshoor_grill_line_100_8[0],
        name="گریل خطی کفشور 8 * 100 گریل خطی", description='', used_count=49,
        per_product=1
    )

    # =================================================================================
    # Full Steel
    # =================================================================================

    # Create Product Kafshoor Full Steel 10 * 10
    product_kafshoor_full_steel_10_10 = Product.objects.get_or_create(
        id=91, name="کفشور 10 * 10 فول استیل", description='', no_prod_per_year=260,
    )

    # Create Components for Kafshoor Full Steel 10 * 10
    component_kafshoor_full_steel_10_10_steel_15 = Component.objects.get_or_create(
        id=1301, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_10_10[0],
        name="ورق استیل کفشور 10 * 10 فول استیل", description='', used_count=41225,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_flappy = Component.objects.get_or_create(
        id=1302, category=component_category_flappy[0], product=product_kafshoor_full_steel_10_10[0],
        name="فلاپی کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_10_10_pipe = Component.objects.get_or_create(
        id=1303, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_10_10[0],
        name="لوله کفشور 10 * 10 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_pipe_cutting = Component.objects.get_or_create(
        id=1304, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_10_10[0],
        name="برش لوله کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_laser_gas = Component.objects.get_or_create(
        id=1305, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_10_10[0],
        name="لیزر و گاز کفشور 10 * 10 فول استیل", description='', used_count=1258,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_bend = Component.objects.get_or_create(
        id=1306, category=component_category_bend[0], product=product_kafshoor_full_steel_10_10[0],
        name="خم کفشور 10 * 10 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_spring = Component.objects.get_or_create(
        id=1307, category=component_category_spring[0], product=product_kafshoor_full_steel_10_10[0],
        name="فنر کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_key = Component.objects.get_or_create(
        id=1308, category=component_category_key[0], product=product_kafshoor_full_steel_10_10[0],
        name="کلید کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_weld = Component.objects.get_or_create(
        id=1309, category=component_category_weld[0], product=product_kafshoor_full_steel_10_10[0],
        name="جوش کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_reamer = Component.objects.get_or_create(
        id=1310, category=component_category_reamer[0], product=product_kafshoor_full_steel_10_10[0],
        name="قلاویز کفشور 10 * 10 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_electropolish = Component.objects.get_or_create(
        id=1311, category=component_category_electropolish[0], product=product_kafshoor_full_steel_10_10[0],
        name="الکتروپلیش کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_press = Component.objects.get_or_create(
        id=1312, category=component_category_press[0], product=product_kafshoor_full_steel_10_10[0],
        name="پرس کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_10_10_paper = Component.objects.get_or_create(
        id=1313, category=component_category_paper[0], product=product_kafshoor_full_steel_10_10[0],
        name="کاغذ تبلیغ کفشور 10 * 10 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =======================================================================================

    # Create Product Kafshoor Full Steel 12 * 12
    product_kafshoor_full_steel_12_12 = Product.objects.get_or_create(
        id=92, name="کفشور 12 * 12 فول استیل", description='', no_prod_per_year=45,
    )

    # Create Components for Kafshoor Full Steel 10 * 10
    component_kafshoor_full_steel_12_12_steel_15 = Component.objects.get_or_create(
        id=1321, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_12_12[0],
        name="ورق استیل کفشور 12 * 12 فول استیل", description='', used_count=53505,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_flappy = Component.objects.get_or_create(
        id=1322, category=component_category_flappy[0], product=product_kafshoor_full_steel_12_12[0],
        name="فلاپی کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_12_12_pipe = Component.objects.get_or_create(
        id=1323, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_12_12[0],
        name="لوله کفشور 12 * 12 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_pipe_cutting = Component.objects.get_or_create(
        id=1324, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_12_12[0],
        name="برش لوله کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_laser_gas = Component.objects.get_or_create(
        id=1325, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_12_12[0],
        name="لیزر و گاز کفشور 12 * 12 فول استیل", description='', used_count=1418,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_bend = Component.objects.get_or_create(
        id=1326, category=component_category_bend[0], product=product_kafshoor_full_steel_12_12[0],
        name="خم کفشور 12 * 12 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_spring = Component.objects.get_or_create(
        id=1327, category=component_category_spring[0], product=product_kafshoor_full_steel_12_12[0],
        name="فنر کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_key = Component.objects.get_or_create(
        id=1328, category=component_category_key[0], product=product_kafshoor_full_steel_12_12[0],
        name="کلید کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_weld = Component.objects.get_or_create(
        id=1329, category=component_category_weld[0], product=product_kafshoor_full_steel_12_12[0],
        name="جوش کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_reamer = Component.objects.get_or_create(
        id=1330, category=component_category_reamer[0], product=product_kafshoor_full_steel_12_12[0],
        name="قلاویز کفشور 12 * 12 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_electropolish = Component.objects.get_or_create(
        id=1331, category=component_category_electropolish[0], product=product_kafshoor_full_steel_12_12[0],
        name="الکتروپلیش کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_press = Component.objects.get_or_create(
        id=1332, category=component_category_press[0], product=product_kafshoor_full_steel_12_12[0],
        name="پرس کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_12_12_paper = Component.objects.get_or_create(
        id=1333, category=component_category_paper[0], product=product_kafshoor_full_steel_12_12[0],
        name="کاغذ تبلیغ کفشور 12 * 12 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 15 * 15
    product_kafshoor_full_steel_15_15 = Product.objects.get_or_create(
        id=93, name="کفشور 15 * 15 فول استیل", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Full Steel 15 * 15
    component_kafshoor_full_steel_15_15_steel_15 = Component.objects.get_or_create(
        id=1341, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_15_15[0],
        name="ورق استیل کفشور 15 * 15 فول استیل", description='', used_count=74925,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_flappy = Component.objects.get_or_create(
        id=1342, category=component_category_flappy[0], product=product_kafshoor_full_steel_15_15[0],
        name="فلاپی کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_15_15_pipe = Component.objects.get_or_create(
        id=1343, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_15_15[0],
        name="لوله کفشور 15 * 15 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_pipe_cutting = Component.objects.get_or_create(
        id=1344, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_15_15[0],
        name="برش لوله کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_laser_gas = Component.objects.get_or_create(
        id=1345, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_15_15[0],
        name="لیزر و گاز کفشور 15 * 15 فول استیل", description='', used_count=458,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_bend = Component.objects.get_or_create(
        id=1346, category=component_category_bend[0], product=product_kafshoor_full_steel_15_15[0],
        name="خم کفشور 15 * 15 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_spring = Component.objects.get_or_create(
        id=1347, category=component_category_spring[0], product=product_kafshoor_full_steel_15_15[0],
        name="فنر کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_key = Component.objects.get_or_create(
        id=1348, category=component_category_key[0], product=product_kafshoor_full_steel_15_15[0],
        name="کلید کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_weld = Component.objects.get_or_create(
        id=1349, category=component_category_weld[0], product=product_kafshoor_full_steel_15_15[0],
        name="جوش کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_reamer = Component.objects.get_or_create(
        id=1350, category=component_category_reamer[0], product=product_kafshoor_full_steel_15_15[0],
        name="قلاویز کفشور 15 * 15 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_electropolish = Component.objects.get_or_create(
        id=1351, category=component_category_electropolish[0], product=product_kafshoor_full_steel_15_15[0],
        name="الکتروپلیش کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_press = Component.objects.get_or_create(
        id=1352, category=component_category_press[0], product=product_kafshoor_full_steel_15_15[0],
        name="پرس کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_15_15_paper = Component.objects.get_or_create(
        id=1353, category=component_category_paper[0], product=product_kafshoor_full_steel_15_15[0],
        name="کاغذ تبلیغ کفشور 15 * 15 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 17 * 17
    product_kafshoor_full_steel_17_17 = Product.objects.get_or_create(
        id=94, name="کفشور 17 * 17 فول استیل", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Full Steel 17 * 17
    component_kafshoor_full_steel_17_17_steel_15 = Component.objects.get_or_create(
        id=1361, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_17_17[0],
        name="ورق استیل کفشور 17 * 17 فول استیل", description='', used_count=91205,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_flappy = Component.objects.get_or_create(
        id=1362, category=component_category_flappy[0], product=product_kafshoor_full_steel_17_17[0],
        name="فلاپی کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_17_17_pipe = Component.objects.get_or_create(
        id=1363, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_17_17[0],
        name="لوله کفشور 17 * 17 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_pipe_cutting = Component.objects.get_or_create(
        id=1364, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_17_17[0],
        name="برش لوله کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_laser_gas = Component.objects.get_or_create(
        id=1365, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_17_17[0],
        name="لیزر و گاز کفشور 17 * 17 فول استیل", description='', used_count=1818,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_bend = Component.objects.get_or_create(
        id=1366, category=component_category_bend[0], product=product_kafshoor_full_steel_17_17[0],
        name="خم کفشور 17 * 17 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_spring = Component.objects.get_or_create(
        id=1367, category=component_category_spring[0], product=product_kafshoor_full_steel_17_17[0],
        name="فنر کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_key = Component.objects.get_or_create(
        id=1368, category=component_category_key[0], product=product_kafshoor_full_steel_17_17[0],
        name="کلید کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_weld = Component.objects.get_or_create(
        id=1369, category=component_category_weld[0], product=product_kafshoor_full_steel_17_17[0],
        name="جوش کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_reamer = Component.objects.get_or_create(
        id=1370, category=component_category_reamer[0], product=product_kafshoor_full_steel_17_17[0],
        name="قلاویز کفشور 17 * 17 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_electropolish = Component.objects.get_or_create(
        id=1371, category=component_category_electropolish[0], product=product_kafshoor_full_steel_17_17[0],
        name="الکتروپلیش کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_press = Component.objects.get_or_create(
        id=1372, category=component_category_press[0], product=product_kafshoor_full_steel_17_17[0],
        name="پرس کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_17_17_paper = Component.objects.get_or_create(
        id=1373, category=component_category_paper[0], product=product_kafshoor_full_steel_17_17[0],
        name="کاغذ تبلیغ کفشور 17 * 17 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 20 * 20
    product_kafshoor_full_steel_20_20 = Product.objects.get_or_create(
        id=95, name="کفشور 20 * 20 فول استیل", description='', no_prod_per_year=25,
    )

    # Create Components for Kafshoor Full Steel 20 * 20
    component_kafshoor_full_steel_20_20_steel_15 = Component.objects.get_or_create(
        id=1381, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_20_20[0],
        name="ورق استیل کفشور 20 * 20 فول استیل", description='', used_count=118625,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_flappy = Component.objects.get_or_create(
        id=1382, category=component_category_flappy[0], product=product_kafshoor_full_steel_20_20[0],
        name="فلاپی کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_20_20_pipe = Component.objects.get_or_create(
        id=1383, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_20_20[0],
        name="لوله کفشور 20 * 20 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_pipe_cutting = Component.objects.get_or_create(
        id=1384, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_20_20[0],
        name="برش لوله کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_laser_gas = Component.objects.get_or_create(
        id=1385, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_20_20[0],
        name="لیزر و گاز کفشور 20 * 20 فول استیل", description='', used_count=2058,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_bend = Component.objects.get_or_create(
        id=1386, category=component_category_bend[0], product=product_kafshoor_full_steel_20_20[0],
        name="خم کفشور 20 * 20 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_spring = Component.objects.get_or_create(
        id=1387, category=component_category_spring[0], product=product_kafshoor_full_steel_20_20[0],
        name="فنر کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_key = Component.objects.get_or_create(
        id=1388, category=component_category_key[0], product=product_kafshoor_full_steel_20_20[0],
        name="کلید کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_weld = Component.objects.get_or_create(
        id=1389, category=component_category_weld[0], product=product_kafshoor_full_steel_20_20[0],
        name="جوش کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_reamer = Component.objects.get_or_create(
        id=1390, category=component_category_reamer[0], product=product_kafshoor_full_steel_20_20[0],
        name="قلاویز کفشور 20 * 20 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_electropolish = Component.objects.get_or_create(
        id=1391, category=component_category_electropolish[0], product=product_kafshoor_full_steel_20_20[0],
        name="الکتروپلیش کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_press = Component.objects.get_or_create(
        id=1392, category=component_category_press[0], product=product_kafshoor_full_steel_20_20[0],
        name="پرس کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_20_20_paper = Component.objects.get_or_create(
        id=1393, category=component_category_paper[0], product=product_kafshoor_full_steel_20_20[0],
        name="کاغذ تبلیغ کفشور 20 * 20 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 30 * 8
    product_kafshoor_full_steel_30_8 = Product.objects.get_or_create(
        id=96, name="کفشور 8 * 30 فول استیل", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Full Steel 30 * 8
    component_kafshoor_full_steel_30_8_steel_15 = Component.objects.get_or_create(
        id=1401, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_30_8[0],
        name="ورق استیل کفشور 8 * 30 فول استیل", description='', used_count=84885,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_flappy = Component.objects.get_or_create(
        id=1402, category=component_category_flappy[0], product=product_kafshoor_full_steel_30_8[0],
        name="فلاپی کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_30_8_pipe = Component.objects.get_or_create(
        id=1403, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_30_8[0],
        name="لوله کفشور 8 * 30 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_pipe_cutting = Component.objects.get_or_create(
        id=1404, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_30_8[0],
        name="برش لوله کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_laser_gas = Component.objects.get_or_create(
        id=1405, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_30_8[0],
        name="لیزر و گاز کفشور 8 * 30 فول استیل", description='', used_count=1978,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_screw_30 = Component.objects.get_or_create(
        id=1406, category=component_category_screw_30[0], product=product_kafshoor_full_steel_30_8[0],
        name="پیچ 3 سانتی کفشور 8 * 30 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_fasten = Component.objects.get_or_create(
        id=1407, category=component_category_fasten[0], product=product_kafshoor_full_steel_30_8[0],
        name="بست کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_bend = Component.objects.get_or_create(
        id=1408, category=component_category_bend[0], product=product_kafshoor_full_steel_30_8[0],
        name="خم کفشور 8 * 30 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_spring = Component.objects.get_or_create(
        id=1409, category=component_category_spring[0], product=product_kafshoor_full_steel_30_8[0],
        name="فنر کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_key = Component.objects.get_or_create(
        id=1410, category=component_category_key[0], product=product_kafshoor_full_steel_30_8[0],
        name="کلید کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_weld = Component.objects.get_or_create(
        id=1411, category=component_category_weld[0], product=product_kafshoor_full_steel_30_8[0],
        name="جوش کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoorstone_30_8_reamer = Component.objects.get_or_create(
        id=1412, category=component_category_reamer[0], product=product_kafshoor_full_steel_30_8[0],
        name="قلاویز کفشور 8 * 30 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_electropolish = Component.objects.get_or_create(
        id=1413, category=component_category_electropolish[0], product=product_kafshoor_full_steel_30_8[0],
        name="الکتروپلیش کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_press = Component.objects.get_or_create(
        id=1414, category=component_category_press[0], product=product_kafshoor_full_steel_30_8[0],
        name="پرس کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_30_8_paper = Component.objects.get_or_create(
        id=1415, category=component_category_paper[0], product=product_kafshoor_full_steel_30_8[0],
        name="کاغذ تبلیغ کفشور 8 * 30 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 45 * 8
    product_kafshoor_full_steel_45_8 = Product.objects.get_or_create(
        id=97, name="کفشور 8 * 45 فول استیل", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Full Steel 45 * 8
    component_kafshoor_full_steel_45_8_steel_15 = Component.objects.get_or_create(
        id=1421, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_45_8[0],
        name="ورق استیل کفشور 8 * 45 فول استیل", description='', used_count=121935,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_flappy = Component.objects.get_or_create(
        id=1422, category=component_category_flappy[0], product=product_kafshoor_full_steel_45_8[0],
        name="فلاپی کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_45_8_pipe = Component.objects.get_or_create(
        id=1423, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_45_8[0],
        name="لوله کفشور 8 * 45 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_pipe_cutting = Component.objects.get_or_create(
        id=1424, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_45_8[0],
        name="برش لوله کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_laser_gas = Component.objects.get_or_create(
        id=1425, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_45_8[0],
        name="لیزر و گاز کفشور 8 * 45 فول استیل", description='', used_count=2578,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_screw_30 = Component.objects.get_or_create(
        id=1426, category=component_category_screw_30[0], product=product_kafshoor_full_steel_45_8[0],
        name="پیچ 3 سانتی کفشور 8 * 45 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_fasten = Component.objects.get_or_create(
        id=1427, category=component_category_fasten[0], product=product_kafshoor_full_steel_45_8[0],
        name="بست کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_bend = Component.objects.get_or_create(
        id=1428, category=component_category_bend[0], product=product_kafshoor_full_steel_45_8[0],
        name="خم کفشور 8 * 45 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_spring = Component.objects.get_or_create(
        id=1429, category=component_category_spring[0], product=product_kafshoor_full_steel_45_8[0],
        name="فنر کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_key = Component.objects.get_or_create(
        id=1430, category=component_category_key[0], product=product_kafshoor_full_steel_45_8[0],
        name="کلید کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_weld = Component.objects.get_or_create(
        id=1431, category=component_category_weld[0], product=product_kafshoor_full_steel_45_8[0],
        name="جوش کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_reamer = Component.objects.get_or_create(
        id=1432, category=component_category_reamer[0], product=product_kafshoor_full_steel_45_8[0],
        name="قلاویز کفشور 8 * 45 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_electropolish = Component.objects.get_or_create(
        id=1433, category=component_category_electropolish[0], product=product_kafshoor_full_steel_45_8[0],
        name="الکتروپلیش کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_press = Component.objects.get_or_create(
        id=1434, category=component_category_press[0], product=product_kafshoor_full_steel_45_8[0],
        name="پرس کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_45_8_paper = Component.objects.get_or_create(
        id=1435, category=component_category_paper[0], product=product_kafshoor_full_steel_45_8[0],
        name="کاغذ تبلیغ کفشور 8 * 45 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 60 * 8
    product_kafshoor_full_steel_60_8 = Product.objects.get_or_create(
        id=98, name="کفشور 8 * 60 فول استیل", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Full Steel 60 * 8
    component_kafshoor_full_steel_60_8_steel_15 = Component.objects.get_or_create(
        id=1441, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_60_8[0],
        name="ورق استیل کفشور 8 * 60 فول استیل", description='', used_count=158985,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_flappy = Component.objects.get_or_create(
        id=1442, category=component_category_flappy[0], product=product_kafshoor_full_steel_60_8[0],
        name="فلاپی کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_60_8_pipe = Component.objects.get_or_create(
        id=1443, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_60_8[0],
        name="لوله کفشور 8 * 60 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_pipe_cutting = Component.objects.get_or_create(
        id=1444, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_60_8[0],
        name="برش لوله کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_laser_gas = Component.objects.get_or_create(
        id=1445, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_60_8[0],
        name="لیزر و گاز کفشور 8 * 60 فول استیل", description='', used_count=3178,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_screw_30 = Component.objects.get_or_create(
        id=1446, category=component_category_screw_30[0], product=product_kafshoor_full_steel_60_8[0],
        name="پیچ 3 سانتی کفشور 8 * 60 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_fasten = Component.objects.get_or_create(
        id=1447, category=component_category_fasten[0], product=product_kafshoor_full_steel_60_8[0],
        name="بست کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_bend = Component.objects.get_or_create(
        id=1448, category=component_category_bend[0], product=product_kafshoor_full_steel_60_8[0],
        name="خم کفشور 8 * 60 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_spring = Component.objects.get_or_create(
        id=1449, category=component_category_spring[0], product=product_kafshoor_full_steel_60_8[0],
        name="فنر کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_key = Component.objects.get_or_create(
        id=1450, category=component_category_key[0], product=product_kafshoor_full_steel_60_8[0],
        name="کلید کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_weld = Component.objects.get_or_create(
        id=1451, category=component_category_weld[0], product=product_kafshoor_full_steel_60_8[0],
        name="جوش کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_reamer = Component.objects.get_or_create(
        id=1452, category=component_category_reamer[0], product=product_kafshoor_full_steel_60_8[0],
        name="قلاویز کفشور 8 * 60 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_electropolish = Component.objects.get_or_create(
        id=1453, category=component_category_electropolish[0], product=product_kafshoor_full_steel_60_8[0],
        name="الکتروپلیش کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_press = Component.objects.get_or_create(
        id=1454, category=component_category_press[0], product=product_kafshoor_full_steel_60_8[0],
        name="پرس کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_60_8_paper = Component.objects.get_or_create(
        id=1455, category=component_category_paper[0], product=product_kafshoor_full_steel_60_8[0],
        name="کاغذ تبلیغ کفشور 8 * 60 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 80 * 8
    product_kafshoor_full_steel_80_8 = Product.objects.get_or_create(
        id=99, name="کفشور 8 * 80 فول استیل", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Full Steel 80 * 8
    component_kafshoor_full_steel_80_8_steel_15 = Component.objects.get_or_create(
        id=1461, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_80_8[0],
        name="ورق استیل کفشور 8 * 80 فول استیل", description='', used_count=208385,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_flappy = Component.objects.get_or_create(
        id=1462, category=component_category_flappy[0], product=product_kafshoor_full_steel_80_8[0],
        name="فلاپی کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_80_8_pipe = Component.objects.get_or_create(
        id=1463, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_80_8[0],
        name="لوله کفشور 8 * 80 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_pipe_cutting = Component.objects.get_or_create(
        id=1464, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_80_8[0],
        name="برش لوله کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_laser_gas = Component.objects.get_or_create(
        id=1465, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_80_8[0],
        name="لیزر و گاز کفشور 8 * 80 فول استیل", description='', used_count=3978,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_screw_30 = Component.objects.get_or_create(
        id=1466, category=component_category_screw_30[0], product=product_kafshoor_full_steel_80_8[0],
        name="پیچ 3 سانتی کفشور 8 * 80 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_fasten = Component.objects.get_or_create(
        id=1467, category=component_category_fasten[0], product=product_kafshoor_full_steel_80_8[0],
        name="بست کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_bend = Component.objects.get_or_create(
        id=1468, category=component_category_bend[0], product=product_kafshoor_full_steel_80_8[0],
        name="خم کفشور 8 * 80 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_spring = Component.objects.get_or_create(
        id=1469, category=component_category_spring[0], product=product_kafshoor_full_steel_80_8[0],
        name="فنر کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_key = Component.objects.get_or_create(
        id=1470, category=component_category_key[0], product=product_kafshoor_full_steel_80_8[0],
        name="کلید کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_weld = Component.objects.get_or_create(
        id=1471, category=component_category_weld[0], product=product_kafshoor_full_steel_80_8[0],
        name="جوش کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_reamer = Component.objects.get_or_create(
        id=1472, category=component_category_reamer[0], product=product_kafshoor_full_steel_80_8[0],
        name="قلاویز کفشور 8 * 80 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_electropolish = Component.objects.get_or_create(
        id=1473, category=component_category_electropolish[0], product=product_kafshoor_full_steel_80_8[0],
        name="الکتروپلیش کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_press = Component.objects.get_or_create(
        id=1474, category=component_category_press[0], product=product_kafshoor_full_steel_80_8[0],
        name="پرس کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_80_8_paper = Component.objects.get_or_create(
        id=1475, category=component_category_paper[0], product=product_kafshoor_full_steel_80_8[0],
        name="کاغذ تبلیغ کفشور 8 * 80 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 90 * 8
    product_kafshoor_full_steel_90_8 = Product.objects.get_or_create(
        id=100, name="کفشور 8 * 90 فول استیل", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Full Steel 90 * 8
    component_kafshoor_full_steel_90_8_steel_15 = Component.objects.get_or_create(
        id=1481, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_90_8[0],
        name="ورق استیل کفشور 8 * 90 فول استیل", description='', used_count=233085,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_flappy = Component.objects.get_or_create(
        id=1482, category=component_category_flappy[0], product=product_kafshoor_full_steel_90_8[0],
        name="فلاپی کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_90_8_pipe = Component.objects.get_or_create(
        id=1483, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_90_8[0],
        name="لوله کفشور 8 * 90 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_pipe_cutting = Component.objects.get_or_create(
        id=1484, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_90_8[0],
        name="برش لوله کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_laser_gas = Component.objects.get_or_create(
        id=1485, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_90_8[0],
        name="لیزر و گاز کفشور 8 * 90 فول استیل", description='', used_count=4378,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_screw_30 = Component.objects.get_or_create(
        id=1486, category=component_category_screw_30[0], product=product_kafshoor_full_steel_90_8[0],
        name="پیچ 3 سانتی کفشور 8 * 90 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_fasten = Component.objects.get_or_create(
        id=1487, category=component_category_fasten[0], product=product_kafshoor_full_steel_90_8[0],
        name="بست کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_bend = Component.objects.get_or_create(
        id=1488, category=component_category_bend[0], product=product_kafshoor_full_steel_90_8[0],
        name="خم کفشور 8 * 90 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_spring = Component.objects.get_or_create(
        id=1489, category=component_category_spring[0], product=product_kafshoor_full_steel_90_8[0],
        name="فنر کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_key = Component.objects.get_or_create(
        id=1490, category=component_category_key[0], product=product_kafshoor_full_steel_90_8[0],
        name="کلید کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_weld = Component.objects.get_or_create(
        id=1491, category=component_category_weld[0], product=product_kafshoor_full_steel_90_8[0],
        name="جوش کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_reamer = Component.objects.get_or_create(
        id=1492, category=component_category_reamer[0], product=product_kafshoor_full_steel_90_8[0],
        name="قلاویز کفشور 8 * 90 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_electropolish = Component.objects.get_or_create(
        id=1493, category=component_category_electropolish[0], product=product_kafshoor_full_steel_90_8[0],
        name="الکتروپلیش کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_press = Component.objects.get_or_create(
        id=1494, category=component_category_press[0], product=product_kafshoor_full_steel_90_8[0],
        name="پرس کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_90_8_paper = Component.objects.get_or_create(
        id=1495, category=component_category_paper[0], product=product_kafshoor_full_steel_90_8[0],
        name="کاغذ تبلیغ کفشور 8 * 90 فول استیل", description='', used_count=1,
        per_product=1
    )

    # =================================================================================

    # Create Product Kafshoor Full Steel 100 * 8
    product_kafshoor_full_steel_100_8 = Product.objects.get_or_create(
        id=101, name="کفشور 8 * 100 فول استیل", description='', no_prod_per_year=60,
    )

    # Create Components for Kafshoor Full Steel 100 * 8
    component_kafshoor_full_steel_100_8_steel_15 = Component.objects.get_or_create(
        id=1501, category=component_category_steel_304_15[0], product=product_kafshoor_full_steel_100_8[0],
        name="ورق استیل کفشور 8 * 100 فول استیل", description='', used_count=257785,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_flappy = Component.objects.get_or_create(
        id=1502, category=component_category_flappy[0], product=product_kafshoor_full_steel_100_8[0],
        name="فلاپی کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=25
    )
    component_kafshoor_full_steel_100_8_pipe = Component.objects.get_or_create(
        id=1503, category=component_category_pipe_51_mil[0], product=product_kafshoor_full_steel_100_8[0],
        name="لوله کفشور 8 * 100 فول استیل", description='', used_count=30,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_pipe_cutting = Component.objects.get_or_create(
        id=1504, category=component_category_pipe_cutting[0], product=product_kafshoor_full_steel_100_8[0],
        name="برش لوله کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_laser_gas = Component.objects.get_or_create(
        id=1505, category=component_category_laser_gas[0], product=product_kafshoor_full_steel_100_8[0],
        name="لیزر و گاز کفشور 8 * 100 فول استیل", description='', used_count=4778,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_screw_30 = Component.objects.get_or_create(
        id=1506, category=component_category_screw_30[0], product=product_kafshoor_full_steel_100_8[0],
        name="پیچ 3 سانتی کفشور 8 * 100 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_fasten = Component.objects.get_or_create(
        id=1507, category=component_category_fasten[0], product=product_kafshoor_full_steel_100_8[0],
        name="بست کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_bend = Component.objects.get_or_create(
        id=1508, category=component_category_bend[0], product=product_kafshoor_full_steel_100_8[0],
        name="خم کفشور 8 * 100 فول استیل", description='', used_count=8,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_spring = Component.objects.get_or_create(
        id=1509, category=component_category_spring[0], product=product_kafshoor_full_steel_100_8[0],
        name="فنر کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_key = Component.objects.get_or_create(
        id=1510, category=component_category_key[0], product=product_kafshoor_full_steel_100_8[0],
        name="کلید کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_weld = Component.objects.get_or_create(
        id=1511, category=component_category_weld[0], product=product_kafshoor_full_steel_100_8[0],
        name="جوش کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_reamer = Component.objects.get_or_create(
        id=1512, category=component_category_reamer[0], product=product_kafshoor_full_steel_100_8[0],
        name="قلاویز کفشور 8 * 100 فول استیل", description='', used_count=4,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_electropolish = Component.objects.get_or_create(
        id=1513, category=component_category_electropolish[0], product=product_kafshoor_full_steel_100_8[0],
        name="الکتروپلیش کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_press = Component.objects.get_or_create(
        id=1514, category=component_category_press[0], product=product_kafshoor_full_steel_100_8[0],
        name="پرس کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )
    component_kafshoor_full_steel_100_8_paper = Component.objects.get_or_create(
        id=1515, category=component_category_paper[0], product=product_kafshoor_full_steel_100_8[0],
        name="کاغذ تبلیغ کفشور 8 * 100 فول استیل", description='', used_count=1,
        per_product=1
    )

    # ======================================================================#
    # Indexing Query
    # ======================================================================#
    cursor = connection.cursor()
    cursor.execute('''ALTER SEQUENCE cost_componentcategory_id_seq RESTART WITH 100;''')
    cursor.execute('''ALTER SEQUENCE cost_product_id_seq RESTART WITH 500;''')
    cursor.execute('''ALTER SEQUENCE cost_component_id_seq RESTART WITH 5000;''')
    print('Done!! ')
