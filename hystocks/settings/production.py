import dj_database_url

from .base import *  # NOQA

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY", "")
USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "").split(",")]

# Database
# --------------------------------------------------------------------------

if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.parse(
        os.environ.get("DATABASE_URL", ""), conn_max_age=10
    )  # NOQA

# SENTRY
# --------------------------------------------------------------------------

if "SENTRY_DSN" in os.environ:
    import sentry_sdk

    SENTRY_DSN = os.environ.get("SENTRY_DSN")

    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(SENTRY_DSN, integrations=[DjangoIntegration()])

# REDIS
# --------------------------------------------------------------------------

if "REDIS_URL" in os.environ:
    cache_locations = [os.environ.get("REDIS_URL")]
    if "REDIS_URL_SLAVE" in os.environ:
        cache_locations.append(os.environ.get("REDIS_URL_SLAVE"))
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": cache_locations,
            "KEY_PREFIX": "live",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "MAX_ENTRIES": 10000000,
            },
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"

# Celery Settings
# ----------------------------------------------------------------------------

if 'BROKER_URL' in os.environ:
    BROKER_URL = os.environ.get('BROKER_URL')

if 'RESULT_BACKEND_URL' in os.environ:
    CELERY_RESULT_BACKEND = os.environ.get('RESULT_BACKEND_URL')

if 'CELERY_RUNNING' in os.environ:
    CELERY_RUNNING = True

