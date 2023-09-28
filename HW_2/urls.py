from django.urls import path, include
from . import views
# from HW_2.views import product_of_client

urlpatterns = [
    # path('base/', views.base, name='base'),
    path('client/<int:customer_id>', views.product_of_client, name='product_of_client'),
    path('add_product/', views.catalog_form, name='catalog_form'),
    # path('products/<int:client_id>', views.AllProductsViews.as_view(), name='products'),
    # path('orders/year/<int:year>/<int:pk>/', views.AllYearProducts.as_view(), name='orders_by_year'),
    # path('orders/monthly/<int:year>/<int:month>/<int:pk>/', views.AllMonthProducts.as_view(), name='orders_by_month'),
    # path('orders/week/<int:year>/<int:week>/<int:pk>/', views.AllWeekProducts.as_view(), name='orders_by_week'),
    # path('__debug__/', include("debug_toolbar.urls")),
]