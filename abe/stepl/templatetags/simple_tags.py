from django import template

register = template.Library()

@register.filter(name='twonum')
def twonum(value):
    value = int(value)
    return '%02i' % value;

@register.filter(name='gr0')
def gr0(value):
    if float(value) > 0:
        return True
    else:
        return False

@register.filter(name='eq0')
def eq0(value):
    if float(value) == 0:
        return True
    else:
        return False


@register.filter(name='get')
def get(o, index):
    try:
        return o[index]
    except:
        return settings.TEMPLATE_STRING_IF_INVALID

@register.filter(name='geti')
def geti(o, index):
    try:
        return o[str(index)]
    except:
        return settings.TEMPLATE_STRING_IF_INVALID