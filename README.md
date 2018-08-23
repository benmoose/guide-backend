# Guide Backend

### Setup

The easiest way is to have Docker installed.

With Docker installed, simply run

```
docker-compose run db web python manage.py migrate --noinput
docker-compose up
```
