from django.core.management import BaseCommand

from hystocks.apps.market.tasks import calculate_market_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        calculate_market_data()
