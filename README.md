# Hystocks.com

### Run celery
celery -A hystocks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
