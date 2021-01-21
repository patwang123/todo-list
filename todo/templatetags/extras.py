from django import template

register = template.Library()

@register.filter
def int_divide(value,arg):
    try:
        return value//arg
    except:
        return None