from django.core.paginator import Paginator
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import Input
from .models import Inputtabel


# Create your views here.

def input(request):
    inputtabel = Input()
    product = Inputtabel.objects.all()
    if request.method == "POST":
        inputtabel = Input(request.POST , request.FILES)
        if inputtabel.is_valid():
            inputtabel.save()
    else:
        inputtabel = Input()

    context = {
        "form": inputtabel,
        "Product": product
    }

    return render(request, "gifts_table.html", context)

# def Prouduct_list(request):
#     product = Inputtabel.objects.all()
#     context = {
#         "Product": product
#     }
#     print(context)
#     return render(request, "gifts_table.html", context)


