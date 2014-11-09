## danpalmer.me

This is the Django application that power my personal site.

#### Usage

Install `requirements/dev.txt` for development tooling.

```
# Build the Docker images
$ shipwright

# Run the application 
$ docker-compose up web

# Run migrations/tests/etc
$ docker-compose run web python manage.py migrate
```
