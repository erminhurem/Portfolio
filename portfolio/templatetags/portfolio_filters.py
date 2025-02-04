from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    """
    Returns the string split by delimiter.
    """
    return value.split(delimiter) 