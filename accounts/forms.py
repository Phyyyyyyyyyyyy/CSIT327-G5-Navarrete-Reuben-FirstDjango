from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm)
from .models import CustomUser


class BootstrapFormMixin:
    """Give every field the matching Bootstrap 5 class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"
            else:
                field.widget.attrs["class"] = "form-control"

    def full_clean(self):
        super().full_clean()
        for name in self.errors:
            if name in self.fields:
                self.fields[name].widget.attrs["class"] += " is-invalid"


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name",
                  "last_name", "course")


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass
