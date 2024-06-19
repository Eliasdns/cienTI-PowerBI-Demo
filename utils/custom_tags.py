from django.conf import settings
from django.forms import BoundField
from django.forms.utils import ErrorList
from django.template import Library, Node
from django.utils.safestring import SafeString
if settings.DEBUG:
    import ipdb  # type: ignore


register = Library()


class IpdbNode(Node):
    def render(self, context):
        if settings.DEBUG:
            _context = context  # noqa: F841
            ipdb.set_trace()
        return ''

@register.tag
def ipdb_trace(parser, token):
    return IpdbNode()


@register.filter
def field_with_attr(field: BoundField, custom_attr) -> BoundField:
    custom_attr = custom_attr.split('=')
    field.field.widget.attrs.update({custom_attr[0]: custom_attr[1].replace('"', '').replace("'", "")})
    return field

@register.filter
def field_required(field: BoundField, required=True) -> BoundField:
    if required == 'False' or required == 'false':
        field.field.required = False
    else:
        field.field.required = True
    return field

@register.filter
def field_with_classes(field: BoundField, custom_classes: str) -> BoundField:
    widget = field.field.widget
    widget.attrs['class'] = f"{widget.attrs['class']} {custom_classes}" if 'class' in widget.attrs else custom_classes
    return field

@register.filter
def field_label_with_classes(field: BoundField, custom_classes: str) -> SafeString:
    return field.label_tag(attrs={'class': custom_classes})

@register.filter
def field_errors_with_classes(error_list: ErrorList, custom_classes: str) -> SafeString:
    context = error_list.get_context()  # noqa
    context |= {'error_class': f"{context['error_class']} {custom_classes}"}
    return error_list.render(context=context)  # noqa
