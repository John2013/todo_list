# Todo_list

A simple todo api on django-rest-framework.

## Build

```bash
docker-compose build
docker-compose run web python manage.py migrate
```

## Run

```bash
docker-compose up
```
The app will run on http://127.0.0.1:8000

## Test

```bash
docker-compose run web python manage.py test
``` 