from django.core.management.base import BaseCommand
from HW_2.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('customer', type=int, help='Client ID')
        parser.add_argument('products', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        customer = Client.objects.get(pk=kwargs.get('customer'))
        products = Product.objects.get(pk=kwargs.get('products'))

        order = Order(customer=customer,
                      products=products,
                      total_amount=0,
        )

        order.save()

        self.stdout.write(f'{order.pk}')