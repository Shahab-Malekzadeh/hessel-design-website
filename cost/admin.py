from django.contrib import admin
from .models import (
    ComponentCategory, Product, Component, ComponentConstant,
    CurrentExpense, TutorialVideo
)


@admin.register(ComponentCategory)
class ComponentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'no_prod_per_year', 'components_cost',
        'current_expense', 'profit_percent', 'final_price',
    )


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'product', 'name', 'description', 'used_count',
        'per_product',
    )


@admin.register(ComponentConstant)
class ComponentConstantAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'product', 'price', 'per_product',
    )


@admin.register(CurrentExpense)
class CurrentExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'cost_in_a_year',
    )


@admin.register(TutorialVideo)
class TutorialVideoAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'video',
    )
