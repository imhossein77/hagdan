from django import forms
from .models import Inputtabel


class Input(forms.ModelForm):
    class Meta:
        model = Inputtabel
        fields = "__all__"
