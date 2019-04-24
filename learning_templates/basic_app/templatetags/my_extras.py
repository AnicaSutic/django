from django import template

register = template.Library()

#register filter using decorators
@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

#register.filter('cut', cut)
