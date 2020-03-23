from django import template

register = template.Library()
@register.filter(name='cutting')
def cutting(value,arg):
    """
        This cuts ou all the values of rgs from the String
    """

    return value.replace(arg,'')

#register.filter('cut',cut)
