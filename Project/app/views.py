from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderCreateForm
from .models import Category, Product, Order
from .cart import Cart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(available=True)

    data = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'list.html', data)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    data = {'product': product}
    return render(request, 'detail.html', data)


def cart(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('product_list')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('product_list')


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart.clear()
            return render(request, 'order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order_create.html', {'form': form, 'cart': cart})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})
