from datetime import timedelta

from django.utils import timezone


def get_30_mins_split(date: timezone):
    date = date.replace(second=0, microsecond=0)

    if date.minute < 30:
        date = date.replace(minute=0)
    else:
        date = date.replace(minute=30)

    return date, date + timedelta(minutes=29, seconds=59)
