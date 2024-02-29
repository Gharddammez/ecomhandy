from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_cart, name='my_cart'),
    path('add/', views.my_cart_add, name='my_cart_add'),
    path('delete', views.my_cart_delete, name='my_cart_delete'),
    path('update/', views.my_cart_update, name='my_cart_update'),
    path('orders/', views.orders, name='orders'),
]