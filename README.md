## About the project
This is a configured django setup with basic setup already done out of the box for you. 
Note: This setup was done using ubuntu os.

Tools completely configured

    docker
    black
    mypy
    bandit
    prospector
    pytest
    celery
    django
    djangorest
    postgres

## Getting Started

    git clone https://github.com/Baronchibuikem/mydjangosetup
    pip install -r requirement.txt
    cd src
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

## To run the project with docker

    docker-compose exec db psql --username=djangosetup --dbname=djangosetup_dev   
    docker-compose up -d --build
    docker-compose down -v
    docker-compose -logs -f
    docker volume inspect djdocker_postgres_data
    docker-compose run db bash

## Testing

- `$ ./scripts/test_local_backend.sh`


### To run black

- `$ black src`
- `$ black tests`
## Static analysis

- `$ ./scripts/static_validate_backend.sh`

### To run mypy we need to run it inside the src folder

- `$ cd src/ `
- `$ mypy .`
