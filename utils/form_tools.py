class LabelSuffixEmptyMixin:
    def __init__(self, *args, **kwargs):
        kwargs['label_suffix'] = ''
        super().__init__(*args, **kwargs)


class PlaceholderFromHelptextMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.help_text:
                field.widget.attrs['placeholder'] = field.help_text
