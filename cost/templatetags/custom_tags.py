from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.simple_tag()
def total_cost(price, per_product, used_count=1, *args, **kwargs):
    total = price * used_count / per_product
    return intcomma(int(total), False)
