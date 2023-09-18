from django.core.management.base import BaseCommand
from HW_2.models import Client


class Command(BaseCommand):
    help = "Get all clients by phone_number"

    def add_arguments(self, parser):
        parser.add_argument('phone_number', type=str, help='Client phone_number')

    def handle(self, *args, **kwargs):
        phone_number = kwargs.get('phone_number')
        client = Client.objects.filter(phone_number__iexact=phone_number)
        intro = f'All clients with phone_number {phone_number}\n'
        self.stdout.write(f'{intro} {client}')