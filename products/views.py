from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')

def list(request):
    product1 = Product()
    product1.id = 1
    product1.name = "Yoda"
    product2 = Product()
    product2.id = 2
    product2.name = "Yoda"

    all_products = {product1, product2}
    return render(request, 'list.html', {'all_products': all_products})

def new(request):
    return HttpResponse('New Products')

def detail(request, album_id):
    # return HttpResponse("<h1>Detailed Product number " + str(album_id) + " </h1>")
    return render(request, 'detail.html', {'album_id': album_id})
