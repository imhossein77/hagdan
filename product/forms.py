from django import forms
from product.models import RegPrice


class Reg_price(forms.ModelForm):
    class Meta:
        model = RegPrice
        fields = "__all__"
