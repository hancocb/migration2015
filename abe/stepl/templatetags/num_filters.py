from django import template

register = template.Library()

@register.filter(name='twonum')
def twonum(value):
    return '%02i' % value;

