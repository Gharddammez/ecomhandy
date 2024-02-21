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
    # get products from the database

    return render(request, 'products.html')


@csrf_exempt
def contact(request):
    # check method request
    if request.method == "POST":
        # get the form data
        username = request.POST.get('username')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        number = request.POST.get('contact')
        message = request.POST.get('message')

        # get the data into the database
        reach = Contact(username=username, contact=number, email=email, subject=subject, message=message)
        # save our data
        reach.save()
        # give message
        messages.success(request, 'We have successfully received your message. We will get back to you')

        return redirect('home')
    return render(request, 'contact.html')
