from .cart import Cart


# make cart available
def cart(request):
    return {'cart': Cart(request)}
