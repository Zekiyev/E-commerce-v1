from django.shortcuts import render

from .models import Category, Product

def categories(request):
    #for content process
    categories = Category.objects.all
    context = {'categories':categories}
    return context

def all_products(request):
    
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context)
