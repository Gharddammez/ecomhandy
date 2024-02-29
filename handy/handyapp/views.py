from django.shortcuts import render, redirect
from .models import Product, Contact
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    prod_all = Product.objects.all()
    # cat = Category.objects.all()
    return render(request, 'products.html', {'product': prod_all})# , 'category': cat})


def product(request, pk):
    prod = Product.objects.get(id=pk)

    return render(request, 'product.html', {'product': prod})


@csrf_exempt
def contact(request):
    # check method request
    if request.method == "POST":
        # get the form data
        username = request.POST['username']
        subject = request.POST['subject']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        # get the data into the database
        reach = Contact(email=email, username=username, contact=number, subject=subject, message=message)
        # save our data
        reach.save()
        # give message
        messages.success(request, 'We have successfully received your message. We will get back to you')

        return redirect('home')
    return render(request, 'contact.html')
