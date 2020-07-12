from django.core.management import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask

"""
python manage.py loadcelery
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        every_half_minute_interval, _ = IntervalSchedule.objects.get_or_create(
            every=30, period="seconds"
        )
        every_minute_interval, _ = IntervalSchedule.objects.get_or_create(
            every=1, period="minutes"
        )
        every_5_minutes_interval, _ = IntervalSchedule.objects.get_or_create(
            every=5, period="minutes"
        )
        every_half_hour_interval, _ = IntervalSchedule.objects.get_or_create(
            every=30, period="minutes"
        )

        PeriodicTask.objects.exclude(name__startswith="celery").delete()

        PeriodicTask.objects.update_or_create(
            name="Crawl prices",
            defaults={
                "task": "hystocks.apps.products.tasks.crawl_products_prices",
                "interval": every_5_minutes_interval,
            },
        )

        PeriodicTask.objects.update_or_create(
            name="Run Market calculation",
            defaults={
                "task": "hystocks.apps.market.tasks.calculate_market_data",
                "interval": every_half_hour_interval,
            },
        )

        print("Loaded celery cronjobs")
