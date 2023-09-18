from django.core.management.base import BaseCommand
from HW_2.models import Product
from random import randint, uniform


class Command(BaseCommand):
    help = 'fake products'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of products')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        for i in range(1, number + 1):
            product = Product(name_of_product=f'name_of_product_{i}',
                              description=f'the best product {i}',
                              price=f'{uniform(1, 5_000)}',
                              quantity=f'{randint(10, 100)}',
                              )
            product.save()
        self.stdout.write('fake products done')