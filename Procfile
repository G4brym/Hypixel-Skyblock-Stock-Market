release: ./manage.py migrate --no-input
web: gunicorn hystocks.settings.wsgi -b 0.0.0.0:5000 -c "gunicorn.conf.py" # --access-logfile "/var/log/gunicorn-acess.log" --error-logfile "/var/log/gunicorn-error.log"
worker: celery worker -B -A hystocks.settings.celery.app -E --autoscale=2,1 -l warning --scheduler django_celery_beat.schedulers.DatabaseScheduler
