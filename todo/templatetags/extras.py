from django import template

register = template.Library()

@register.filter
def int_divide(value,arg):
    try:
        return value//arg
    except:
        return None

priorities = {0:'N/A',1:'Low',2: 'Medium',3:'High',4: 'ASAP'}
@register.filter
def convert_priority(value):
    return priorities[value]