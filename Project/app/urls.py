from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),  # Тут добавляем так, как нужно
]
