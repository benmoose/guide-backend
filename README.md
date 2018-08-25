# Guide Backend

### Setup

With [Docker installed](https://docs.docker.com/install/), simply run:

```
docker-compose up
```

Note: if this is the first time you're running the project, or you've
removed previously created containers, you need to run migrations first:

```
docker-compose run db web python manage.py migrate --noinput
```
