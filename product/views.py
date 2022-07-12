from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def Prouduct_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)

    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    context = {
        "productlist": productlist,
    }
    return render(request, "products.html", context)


def Product_detail(request, id):
    product = Product.objects.get(id=id)
    productt = Product.objects.filter(date_type=product.date_type)
    context = {
        "Product": product,
        'ppp': productt
    }
    return render(request, "product.html", context)


def prouduct(request, category):
    product_list = Product.objects.filter(category__type=category)
    paginator = Paginator(product_list, 9)

    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    context = {
        "productlist": productlist,
    }
    return render(request, "products.html", context)
