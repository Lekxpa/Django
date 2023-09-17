from django.shortcuts import render
from HW_2.models import Client, Order, Product
from django.shortcuts import render, get_object_or_404

def product_of_client(request, customer_id):
    client = get_object_or_404(Client, pk=customer_id)
    orders = Order.objects.filter(customer_id=customer_id).all()
    products = set(product for order in orders for product in order.products.values_list('name_of_product'))

    return render(request, 'HW_2/product_of_client.html', {'client': client,
                                                            'orders': orders,
                                                            'products': products})

