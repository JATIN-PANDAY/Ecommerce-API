from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<uuid:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<uuid:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
