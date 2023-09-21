from datetime import datetime
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import DetailView
import logging
from .forms import CatalogForm
from django.core.files.storage import FileSystemStorage

from HW_2.models import Client, Order, Product
from django.shortcuts import render, get_object_or_404
from django.views.generic.dates import MonthArchiveView, WeekArchiveView, ArchiveIndexView, YearArchiveView

logger = logging.getLogger(__name__)

def base(request):
    logger.info('Index page accessed')
    return render(request, 'base.html')

def product_of_client(request, customer_id):
    client = get_object_or_404(Client, pk=customer_id)
    orders = Order.objects.filter(customer_id=customer_id).all()
    products = set(product for order in orders for product in order.products.values_list('name_of_product'))

    return render(request, 'HW_2/products_of_client.html', {'client': client,
                                                            'orders': orders,
                                                            'products': products})
def catalog_form(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            name_of_product = form.cleaned_data['name_of_product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(name_of_product=name_of_product, description=description,
                              price=price, quantity=quantity, image=image)
            product.save()
            logger.info(f'Добавлено: {name_of_product=}, {price=}, {quantity=}.')
    else:
        form = CatalogForm()
    return render(request, 'HW_2/catalog_form.html', {'form': form})


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
