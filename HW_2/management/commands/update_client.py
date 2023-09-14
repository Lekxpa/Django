from django.core.management.base import BaseCommand
from HW_2.models import Client


class Command(BaseCommand):
    help = "Update client name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('phone_number', type=str, help='phone_number of client')
        parser.add_argument('address', type=str, help='Address of client')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        phone_number = kwargs.get('phone_number')
        address = kwargs.get('address')

        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.phone_number = phone_number
        client.address = address
        client.save()
        self.stdout.write(f'{client}')