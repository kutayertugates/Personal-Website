from django import template
from Main.models import DynamicContent

register = template.Library()

@register.simple_tag
def get_dynamic_content(key_name):
    """
    Kullanım: {% get_dynamic_content 'logo' as logo_obj %}
    """
    try:
        return DynamicContent.objects.get(title=key_name)
    except DynamicContent.DoesNotExist:
        return None