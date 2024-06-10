from django.shortcuts import render
from .models import Product

# def home(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {'products': products})

def blank_view(request):
    return render(request, 'home.html')