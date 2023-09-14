from django.core.management import BaseCommand
from HW_2.models import Client

class Command(BaseCommand):
    help = "Create client"

    def handle(self, *args, **kwargs):
        client = Client(name='Helen', email='helen@gmail.com',
        phone_number='+79031000101', address='NN, str.Central, 5, 2')
        client.save()
        self.stdout.write(f'{client}')