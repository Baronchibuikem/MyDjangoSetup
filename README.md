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

- `$ ./scripts/run_testcases.sh`

### To run black
- `$ ./scripts/run_blank.sh`

### To run mypy
- `$ ./scripts/run_mypy.sh`

### To run prospector
- `$ ./scripts/run_prospector.sh`
## You can run all the above script using the command below

Before you push your code after running all the inidvidual scripts, I recommend you run this script to be sure everything is covered

- `$ ./scripts/validate_backend_code.sh`

