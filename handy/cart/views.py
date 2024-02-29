from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from handy import settings
from handyapp.models import Product, Order

from django.contrib.auth import authenticate, login, logout


# Create your views here.

@csrf_exempt
def my_cart(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, 'my_cart.html',
                  {'products': cart_products, 'quantities': quantities, 'totals': totals})


@csrf_exempt
def my_cart_add(request):
    cart = Cart(request)
    # post test
    if request.POST.get('action') == 'post':
        # get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # look data
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        # cart quantity
        cart_qnt = cart.__len__()
        # response return
        messages.success(request, f'Added Successfully')
        response = JsonResponse({'Product Id': product_id, 'Product Qty': product_qty})

        return response


@csrf_exempt
def my_cart_delete(request):
    cart = Cart(request)
    # post test
    if request.POST.get('action') == 'post':
        # get the data
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'Product Deleted ID': product_id})
        messages.error(request, f'Product deleted from cart')
        return response


@csrf_exempt
def my_cart_update(request):
    cart = Cart(request)
    # post test
    if request.POST.get('action') == 'post':
        # get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'Product ID': product_id, 'qty': product_qty})
        return response


@csrf_exempt
def orders(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    quantity = cart.get_quants()
    quants = 0
    products = []
    user = request.user.username

    if request.method == 'POST':
        for product in cart_products:
            for key, value in quantity.items():
                key = int(key)
                if product.id == key:
                    quants = int(value)

            if product.is_sale:
                cost = product.sale_price * quants
            else:
                cost = product.price * quants

            order = Order(product=product.name, cost=cost, quantity=quants,
                          customer=user)
            if user:
                order.save()
            else:
                messages.info(request, "Login to make an order")
                url = reverse('login_user')
                # Redirecting to the generated URL
                return HttpResponseRedirect(url)

            products.append(product.name)
        if user:
            messages.success(request, "Your order has been received, please check your email for more instructions")
            send_mail('Order Received',
                      f'Dear {request.user.username} your order for the items {products} will be delivered to you at the location stated. Please be patient as we assign you the nearest driver to get you your order.',
                      settings.EMAIL_HOST_USER,
                      [request.user.email],
                      fail_silently=False
                      )
            url = reverse('home')

            # Redirecting to the generated URL
            return HttpResponseRedirect(url)
        else:
            messages.info(request, "Login to make an order")
            url = reverse('login_user')
            # Redirecting to the generated URL
            return HttpResponseRedirect(url)
