from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple


from . import models


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-input'
        self.fields['email'].widget.attrs['class'] = 'form-input'
        self.fields['password1'].widget.attrs['class'] = 'form-input'
        self.fields['password2'].widget.attrs['class'] = 'form-input'

        self.fields['password2'].label = "Confirm Password"


class CertForm(forms.ModelForm):
    class Meta:
        model = models.Cert
        fields = ("__all__")


class CodeForm(forms.ModelForm):
    class Meta:
        model = models.Code
        fields = ("__all__")

    def __init__(self, *args, **kwargs):

        super(CodeForm, self).__init__(*args, **kwargs)

        self.fields["skill_used"].widget = CheckboxSelectMultiple()
        self.fields["skill_used"].queryset = models.Skill.objects.all()


class ExpForm(forms.ModelForm):
    class Meta:
        model = models.Exp
        fields = ("__all__")


class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ("__all__")
