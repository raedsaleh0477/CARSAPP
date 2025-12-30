from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'catalog-app/product_list.html', {
        'products': products
    })
