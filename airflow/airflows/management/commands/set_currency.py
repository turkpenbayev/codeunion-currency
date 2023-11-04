from django.core.management.base import BaseCommand
from airflows.models import Currency

class Command(BaseCommand):
    help = 'Update or view currency data'

    def add_arguments(self, parser):
        # Определите аргументы команды. В данном случае, id валюты и значение.
        parser.add_argument('currency_id', type=int, help='ID of the currency')
        parser.add_argument('rate', type=float, help='New rate for the currency')

    def handle(self, *args, **kwargs):
        currency_id = kwargs['currency_id']
        rate = kwargs['rate']

        # Получите объект валюты по id
        currency = Currency.objects.get(id=currency_id)

        # Обновите значение валюты
        currency.rate = rate
        currency.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully updated currency {currency.name} to {rate}'))
