# Hystocks

## Env keys

These keys needs to be defined
 - SECRET_KEY
 - HYPIXEL_API_KEY
 - SENTRY_DSN
 - CELERY_RUNNING

## Deploy to Dokku

#####Setup env keys
```bash
dokku config:set hystocks \
 DISABLE_COLLECTSTATIC=1 \
 DJANGO_SETTINGS_MODULE=hystocks.settings.production \
 ALLOWED_HOSTS=hystocks.com \
 C_FORCE_ROOT=true \
 SECRET_KEY=debug_key \
 HYPIXEL_API_KEY=debug_key
```

```bash
git remote add dokku ssh://dokku@your_server:1234/hystocks
git push dokku master
```
