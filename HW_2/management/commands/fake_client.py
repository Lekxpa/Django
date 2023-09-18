from django.core.management.base import BaseCommand

from HW_2.models import Client
from random import randint
import random


class Command(BaseCommand):
    help = "fake clients"

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of client')

    def handle(self, *args, **kwargs):
        address_list = ["Moscow", "SPb", "NN", "Rostov", "Sochi", "Ekb"]
        number = kwargs.get('number')
        for i in range(1, number + 1):
            client = Client(name=f'client_{i}',
                          email=f'mail{i}@mail.ru',
                          phone_number=f'+7900{randint(100, 999)}{randint(10, 99)}{randint(10, 99)}',
                          address=f'{random.choice(address_list)}')
            client.save()
        self.stdout.write("fake clients done")