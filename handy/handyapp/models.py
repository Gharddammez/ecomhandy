from django.db import models
import datetime


# Create your models here.
# Product Model

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.TextField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='static/products/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


# Contact Model
class Contact(models.Model):
    email = models.CharField(max_length=105, default='', blank=False, null=False)
    username = models.CharField(max_length=100, default='', blank=False, null=False)
    contact = models.CharField(max_length=15, default='', blank=False, null=False)
    subject = models.CharField(max_length=200, default='', blank=False, null=False)
    message = models.TextField(max_length=1000, default='', blank=False, null=False)

    def __str__(self):
        return f'{self.email}'


class Order(models.Model):
    product = models.CharField(max_length=100, default='', blank=False, null=False)
    customer = models.CharField(max_length=100, default='', blank=False, null=False)
    quantity = models.IntegerField(default=1, blank=False, null=False)
    address = models.CharField(max_length=100, default='', null=False)
    phone = models.CharField(max_length=13, default='', blank=True, null=False)
    cost = models.IntegerField(default=0, blank=False, null=False)
    date = models.DateField(default=datetime.datetime.today)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product} {self.customer} {self.address} {self.date}'
