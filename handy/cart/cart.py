from handyapp.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('sesh_key')
        # create a session key for new user
        if 'sesh_key' not in request.session:
            cart = self.session['sesh_key'] = {}

        # cart availability on each page
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price:': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        # get ids
        product_ids = self.cart.keys()
        # use the id to get products
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def cart_total(self):
        # products id
        product_ids = self.cart.keys()
        # check keys in db
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0

        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (int(product.sale_price) * int(value))
                    else:
                        total = total + (int(product.price) * int(value))

        return total

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        # obtain the cart
        our_cart = self.cart
        # dictionary update
        our_cart[product_id] = product_qty
        self.session.modified = True

        something = self.cart

        return something

    def delete(self, product):

        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True