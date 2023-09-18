from django.core.management.base import BaseCommand
from HW_2.models import Client, Product, Order
from random import randint


class Command(BaseCommand):
    help = 'fake orders'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='number orders')

    def handle(self, *args, **kwargs):
        number_client = len(Client.objects.all())
        number_product = len(Product.objects.all())
        number = kwargs.get('number')
        for k in range(1, number + 1):
            customer = Client.objects.get(id=randint(1, number_client + 1))
            order = Order(customer=customer, total_price=0)
            order.save()
            lst_products = []
            for i in range(1, 5):
                tmp = randint(1, number_product)
                product = Product.objects.get(pk=tmp)
                lst_products.append(product)
            for product in lst_products:
                order.products.add(product)
            order.total_price = sum(product.price for product in lst_products)
            order.save()

        self.stdout.write('Fake orders added')