# Hystocks

## Env keys

These keys needs to be defined
 - SECRET_KEY
 - HYPIXEL_API_KEY
 - SENTRY_DSN
 - CELERY_RUNNING

## Deploy to Piku

#####Setup env keys
Nginx
```bash
ssh piku@your_server config:set hystocks \
 NGINX_SERVER_NAME=your_server.tld \
 NGINX_HTTPS_ONLY=1
```

Django
```bash
ssh piku@your_server config:set hystocks \
 SECRET_KEY=debug_key \
 ALLOWED_HOSTS=your_server.tld \
 SENTRY_DSN=debug_key \
 DATABASE_URL=postgres://hystocks:hystocks@db_host:5432/hystocks \
 REDIS_URL=redis://192.168.0.11:6379/1 \
 BROKER_URL=redis://192.168.0.11:6379/2 \
 RESULT_BACKEND_URL=redis://192.168.0.11:6379/3 \
 CELERY_RUNNING=true \
 HYPIXEL_API_KEY=debug_key
```

```bash
git remote add piku ssh://piku@your_server:1234/hystocks
git push piku master
```
