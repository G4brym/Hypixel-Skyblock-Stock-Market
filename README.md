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
 SENTRY_DSN=debug_key \
 HYPIXEL_API_KEY=debug_key
```

```bash
git remote add piku ssh://piku@your_server:1234/hystocks
git push piku master
```
