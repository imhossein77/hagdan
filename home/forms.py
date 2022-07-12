from django import forms
from product.models import Contact


class Contactus(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
