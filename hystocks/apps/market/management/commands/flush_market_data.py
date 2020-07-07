import math
from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from hystocks.apps.market.models import ProductMarketPrice
from hystocks.apps.products.models import Product


def get_30_mins_split(date: timezone):
    date = date.replace(second=0, microsecond=0)

    if date.minute < 30:
        date = date.replace(minute=0)
    else:
        date = date.replace(minute=30)

    return date, date + timedelta(minutes=29, seconds=59)


class Command(BaseCommand):
    def handle(self, *args, **options):
        clandles = []

        for product in Product.objects.all():
            print("Processing {}".format(product.name))
            product.market.all().delete()

            open_time = None
            close_time = None
            open = None
            high = 0
            low = math.inf
            close = None
            for price in product.prices.all():
                if open_time and close_time and price.created_at > close_time:
                    clandles.append(ProductMarketPrice(
                        product=product,
                        open_time=open_time,
                        open=open,
                        high=high,
                        low=low if low != math.inf else high,
                        close=close,
                        volume=0,
                        close_time=close_time,
                    ))

                    open_time = None
                    close_time = None
                    open = None
                    high = 0
                    low = math.inf
                    close = None

                if not open_time:
                    open_time, close_time = get_30_mins_split(price.created_at)
                    open = price.price

                if price.price > high:
                    high = price.price
                elif price.price < low:
                    low = price.price

                close = price.price

        ProductMarketPrice.objects.bulk_create(clandles)
