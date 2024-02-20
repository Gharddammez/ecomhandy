from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def products(request):
    # get products from the database

    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')
