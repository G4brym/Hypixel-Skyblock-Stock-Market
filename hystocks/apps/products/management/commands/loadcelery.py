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

        PeriodicTask.objects.exclude(name__startswith="celery").delete()

        PeriodicTask.objects.get_or_create(
            name="Half Minute Cronjob",
            defaults={
                "task": "hystocks.apps.products.tasks.crawl_products_prices",
                "interval": every_half_minute_interval,
            },
        )

        print("Loaded celery cronjobs")
