from django.contrib import admin
from .models import Product, Contact, Category, RegPrice


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('date_type', 'active', 'category', 'Product_tonnage', 'phone')
    # list_select_related = ('date_type', 'active', 'category')
    search_fields = ('date_type', 'active', 'category', 'Product_tonnage', 'phone')
    ordering = ('date_type', 'active', 'category', 'Product_tonnage', 'phone')


admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(RegPrice)
admin.site.register(Product, ProductAdmin)
