from django import forms
from firstapp.models import InputUser
class FormName(forms.ModelForm):
    class Meta:
        model = InputUser
        fields='__all__'