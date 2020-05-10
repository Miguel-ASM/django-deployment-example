from django.template import Library
import re
register = Library()

@register.filter(name='ninini')
def ninini(value):
    s = re.sub(r'[aeou]','i',value)
    s = re.sub(r'[AEOU]','I',s)
    return s
