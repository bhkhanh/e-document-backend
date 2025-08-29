# from datetime import date

from django import forms


class CustomDatePickerWidget(forms.DateInput):
    """Custom date picker widget for date field."""

    def __init__(self, attrs={}, format=None):
        attrs.update({"class": "form-control", "type": "date"})
        super().__init__(attrs=attrs, format=format)
