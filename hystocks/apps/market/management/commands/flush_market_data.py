import math

from django.core.management import BaseCommand
from django.utils import timezone

from hystocks.apps.market.models import ProductMarketPrice
from hystocks.apps.market.utils import get_30_mins_split
from hystocks.apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = timezone.now()
        candles = []

        ProductMarketPrice.objects.all().delete()
        for product in Product.objects.all():
            print("Processing {}".format(product.name))

            open_time = None
            close_time = None
            open = None
            high = 0
            low = math.inf
            close = None

            total = product.prices.count()
            for index, price in enumerate(product.prices.all()):
                if index % 10 == 0:
                    print("{}/{}".format(index, total))

                if open_time and close_time and price.created_at > close_time:
                    candles.append(ProductMarketPrice(
                        product=product,
                        open_time=int(open_time.timestamp())*1000,
                        open=open,
                        high=high,
                        low=low if low != math.inf else high,
                        close=close,
                        volume=0,
                        close_time=int(close_time.timestamp())*1000,
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

                    if close_time > now:
                        break

                if price.price > high:
                    high = price.price
                elif price.price < low:
                    low = price.price

                close = price.price

        ProductMarketPrice.objects.bulk_create(candles)
