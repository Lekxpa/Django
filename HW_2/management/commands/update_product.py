from django.core.management import BaseCommand
from HW_2.models import Product


class Command(BaseCommand):
    help = "Update name_of_product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name_of_product', type=str, help='Name_of_product')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name_of_product = kwargs.get('name_of_product')
        product = Product.objects.filter(pk=pk).first()
        product.name_of_product = name_of_product
        product.save()
        self.stdout.write(f'{product}')