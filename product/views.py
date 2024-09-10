from django.shortcuts import get_object_or_404, render

from .models import Product

def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product.html',{'product':product})
