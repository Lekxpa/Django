from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('client/<int:order_client_id>', views.products_of_client, name='products_of_client'),
]