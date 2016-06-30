from __future__ import absolute_import

from django.contrib.auth.forms import ReadOnlyPasswordHashWidget
from django.contrib.admin.widgets import (AdminDateWidget, AdminTimeWidget,
                                          AdminSplitDateTime, RelatedFieldWidgetWrapper)
from django.forms import (FileInput, CheckboxInput, RadioSelect, CheckboxSelectMultiple, Select )

from bootstrap3 import renderers
try:
    from bootstrap3.utils import add_css_class
except ImportError:
    from bootstrap3.html import add_css_class
from bootstrap3.text import text_value

class BootstrapFieldRenderer(renderers.FieldRenderer):
    def _render(self):
        # See if we're not excluded
        if self.field.name in self.exclude.replace(' ', '').split(','):
            return ''
        # Hidden input requires no special treatment
        if self.field.is_hidden:
            return text_value(self.field)
        # Render the widget
        self.add_widget_attrs()
        html = self.field.as_widget(attrs=self.widget.attrs)
        self.restore_widget_attrs()
        # Start post render
        html = self.post_widget_render(html)
        html = self.wrap_widget(html)
        html = self.make_input_group(html)
        html = self.append_to_field(html)
        html = self.wrap_field(html)
        html = self.wrap_label_and_field(html)
        return html

