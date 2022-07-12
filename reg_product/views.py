from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import Reg_product


# Create your views here.

def reg_product(request):
    register_product = Reg_product()
    if request.method == "POST":
        register_product = Reg_product(request.POST , request.FILES)
        if register_product.is_valid():
            register_product.save()
    else:
        register_product = Reg_product()

    context = {
        "form": register_product,
    }

    return render(request, "product_reg.html", context)
