from django import template

register = template.Library()

@register.filter(name='cutter')
def mycut(value, arg):
  """
   This cuts out all values of arg from string
  """
  return value.replace(arg,'>>>')


#register.filter('cutter', mycut)
