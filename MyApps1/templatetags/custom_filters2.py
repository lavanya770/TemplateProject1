from django import template
register=template.Library();
@register.filter(name='c_and_c')
def cut_and_concate(value,arg):
    result=value[:3]+str(arg);
    return result;
