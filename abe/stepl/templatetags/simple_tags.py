from django import template

register = template.Library()

@register.filter(name='twonum')
def twonum(value):
    return '%02i' % value;

@register.filter(name='get')
def get(o, index):
    try:
        return o[index]
    except:
        return settings.TEMPLATE_STRING_IF_INVALID