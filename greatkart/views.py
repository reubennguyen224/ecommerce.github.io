from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context=context)

def statistics(request):
    products = Product.objects.all()
    total = 0
    for product in products:
        total += product.totalpriceget
    context = {
        'products': products,
        'total' : total,
    }
    return render(request, 'statistics.html', context=context)