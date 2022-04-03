from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomerClearableFileInput(ClearableFileInput):
    """create our customer widget class"""
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/customer_widget_template/customer_clearable_file_input.html'
