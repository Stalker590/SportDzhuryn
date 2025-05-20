from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)  # По 9 товарів на сторінці (3x3)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'goods/product_list.html', {'page_obj': page_obj})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'goods/product_detail.html', {'product': product})
