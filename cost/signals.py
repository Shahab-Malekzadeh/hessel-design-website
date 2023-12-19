from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import (
    ComponentCategory, Product, Component, ComponentConstant,
    CurrentExpense,
)


def calculate_components_price(product):
    product_components = product.component_set.all()
    product_constant_components = product.componentconstant_set.all()

    total_price = 0
    for component in product_components:
        total_price += component.category.price * component.used_count / component.per_product
    for constant_component in product_constant_components:
        total_price += constant_component.price / constant_component.per_product

    return int(total_price)


def calculate_current_expense_per_product():
    current_expenses = CurrentExpense.objects.all()
    current_expenses_price = 0
    for current_expense in current_expenses:
        current_expenses_price += current_expense.cost_in_a_year

    all_products = Product.objects.all()
    yearly_cost_for_components = 0
    for product in all_products:
        no_prod_per_year = 0 if product.no_prod_per_year is None else product.no_prod_per_year
        components_cost = 0 if product.components_cost is None else product.components_cost
        yearly_cost_for_components += no_prod_per_year * components_cost

    if yearly_cost_for_components:
        current_expense_division_per_toman = current_expenses_price / yearly_cost_for_components
    else:
        current_expense_division_per_toman = 0

    for product in all_products:
        components_cost = 0 if product.components_cost is None else product.components_cost
        product.current_expense = components_cost * current_expense_division_per_toman
        product.save()


@receiver(post_save, sender=ComponentCategory)
def component_category_post_save_handler(sender, instance, **kwargs):
    components = instance.component_set.all()
    for component in components:
        product_price = calculate_components_price(component.product)
        product = Product.objects.filter(id=component.product.id)[0]
        product.components_cost = product_price
        product.save()

    calculate_current_expense_per_product()


products = []


@receiver(pre_delete, sender=ComponentCategory)
def component_category_pre_delete_handler(sender, instance, **kwargs):
    components = instance.component_set.all()
    global products
    products = []
    for component in components:
        products.append(component.product)
        component.delete()
    # print('products : ', products)


@receiver(post_delete, sender=ComponentCategory)
def component_category_post_delete_handler(sender, instance, **kwargs):
    for product in products:
        product_price = calculate_components_price(product)
        product = Product.objects.filter(id=product.id)[0]
        product.components_cost = product_price
        product.save()

    calculate_current_expense_per_product()


@receiver(post_save, sender=Component)
def component_post_save_handler(sender, instance, **kwargs):
    if instance.product is not None:
        product_price = calculate_components_price(instance.product)
        product = Product.objects.filter(id=instance.product.id)[0]
        product.components_cost = product_price
        product.save()

        calculate_current_expense_per_product()


@receiver(post_delete, sender=Component)
def component_post_delete_handler(sender, instance, **kwargs):
    if instance.product is not None:
        product_price = calculate_components_price(instance.product)
        product = Product.objects.filter(id=instance.product.id)[0]
        product.components_cost = product_price
        product.save()

        calculate_current_expense_per_product()


@receiver(post_save, sender=ComponentConstant)
def component_constant_post_save_handler(sender, instance, **kwargs):
    if instance.product is not None:
        product_price = calculate_components_price(instance.product)
        product = Product.objects.filter(id=instance.product.id)[0]
        product.components_cost = product_price
        product.save()

        calculate_current_expense_per_product()


@receiver(post_delete, sender=ComponentConstant)
def component_constant_post_delete_handler(sender, instance, **kwargs):
    if instance.product is not None:
        product_price = calculate_components_price(instance.product)
        product = Product.objects.filter(id=instance.product.id)[0]
        product.components_cost = product_price
        product.save()

        calculate_current_expense_per_product()


@receiver(post_save, sender=CurrentExpense)
def current_expense_post_save_handler(sender, instance, **kwargs):
    calculate_current_expense_per_product()


@receiver(post_delete, sender=CurrentExpense)
def current_expense_post_delete_handler(sender, instance, **kwargs):
    calculate_current_expense_per_product()
