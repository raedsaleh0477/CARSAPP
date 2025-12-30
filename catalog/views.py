from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def catalog_home(request):
    return render(request, 'catalog-app/catalog_home.html')
