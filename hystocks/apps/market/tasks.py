import math
from datetime import datetime

from django.utils import timezone
from django.utils.timezone import make_aware

from hystocks.apps.market.models import ProductMarketPrice
from hystocks.apps.market.utils import get_30_mins_split
from hystocks.apps.products.models import Product
from hystocks.settings.celery import app


@app.task(ignore_result=True)
def calculate_market_data():
    print("#TASK: Running Calculate Market Data")
    now = timezone.now()
    candles = []

    for product in Product.objects.all():
        open_time = None
        close_time = None
        open = None
        high = 0
        low = math.inf
        close = None

        last_product_candle = ProductMarketPrice.objects.filter(product=product).order_by("-close_time").first()

        if last_product_candle:
            last_close_time = make_aware(datetime.fromtimestamp(last_product_candle.close_time/1000))
            qs = product.prices.filter(created_at__gt=last_close_time)
        else:
            qs = product.prices.filter()

        for index, price in enumerate(qs):
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

    print("Finished calculating")
