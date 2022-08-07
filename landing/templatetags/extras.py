from django import template

register = template.Library()


@register.filter
def phone(value):
    return "%s-%s-%s" % (value[0:3], value[3:6], value[6:])

