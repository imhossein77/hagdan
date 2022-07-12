from django.shortcuts import render

from .forms import Contactus


# Create your views here.

def reg_product(request):
    contact = Contactus()
    if request.method == "POST":
        contact = Contactus(request.POST, request.FILES)
        if contact.is_valid():
            contact.save()
    else:
        contact = Contactus()

    context = {
        "form": contact,
    }

    return render(request, "index.html", context)
