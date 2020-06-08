from django.core.management import BaseCommand

from hystocks.apps.products.tasks import crawl_products_prices

"""
python manage.py crawl
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        crawl_products_prices()
