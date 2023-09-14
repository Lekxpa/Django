from django.core.management import BaseCommand
from HW_2.models import Product

class Command(BaseCommand):
    help = "Add product"

    def handle(self, *args, **kwargs):
        product = Product(name_of_product='milk', description='milk 0.9',
        price=100.60, quantity=25)
        product.save()
        self.stdout.write(f'{product}')