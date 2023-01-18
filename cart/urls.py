from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    # path('', views.index, name='index'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path(' ', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('remove/<int:product_id>/', views.cart_full_remove, name='cart_full_remove'),
    path('payment/', views.payment, name='index'),

]
