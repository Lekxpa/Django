from datetime import datetime
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import DetailView

from HW_2.models import Client, Order, Product
from django.shortcuts import render, get_object_or_404
from django.views.generic.dates import MonthArchiveView, WeekArchiveView, ArchiveIndexView, YearArchiveView

def product_of_client(request, customer_id):
    client = get_object_or_404(Client, pk=customer_id)
    orders = Order.objects.filter(customer_id=customer_id).all()
    products = set(product for order in orders for product in order.products.values_list('name_of_product'))

    return render(request, 'HW_2/products_of_client.html', {'client': client,
                                                            'orders': orders,
                                                            'products': products})



# class AllProductsViews(TemplateView):
#     template_name = 'HW_2/products_of_client.html'


#     def get_context_dat(self, **kwargs):
#         client = Client.objects.get(pk=self.kwargs.get('pk'))
#         orders = super().get_qyeryset().filter(client=client).prefetch_related('products')
#         products = set(product for order in orders for product in order.products.values_list('title'))

#         context = super().get_context_data(**kwargs)
#         context['products'] = products
#         context['client'] = client
#         return context
#         # return render(request, 'HW_2/products_of_client.html', {'client': client,
#                                                             # 'orders': orders,
#                                                             # 'products': products})
    
#     def get_qyeryset(self, **kwargs):
#         orders = Order.objects.get_queryset().filter(client=self.kwargs.get('pk'))
#         return orders

#     # def get_context_dat(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     client = Client.objects.get(pk=self.kwargs['client_id'])
#     #     products = Product.objects.filter(client=client).all()

#     #     context['products'] = products 
#     #     return context
    

# class AllYearProducts(AllProductsViews, YearArchiveView):
#     pass


# class AllMonthProducts(AllProductsViews, MonthArchiveView):
#     pass


# class AllWeekProducts(AllProductsViews, WeekArchiveView):
#     pass
