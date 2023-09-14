from django.core.management.base import BaseCommand
from HW_2.models import Client


class Command(BaseCommand):
    help = "Get all clients by address."

    def add_arguments(self, parser):
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **kwargs):
        address = kwargs.get('address')
        client = Client.objects.filter(address__iexact=address)
        intro = f'All clients with address {address}\n'
        self.stdout.write(f'{intro} {client}')