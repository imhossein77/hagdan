from django import forms
from product.models import Product


class Reg_product(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
