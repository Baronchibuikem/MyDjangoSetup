## To Start the project

            docker-compose exec db psql --username=hello_django --dbname=hello_django_dev   ---> create database
            docker-compose up -d --build   ---> build the container and start it
            docker-compose down -v         ---> take down the container and associated volume
            docker-compose -logs -f        ---> view your logs
            docker volume inspect djdocker_postgres_data   ---> check that postgres volumes where created
            sudo docker-compose run db bash


## Testing

- `$ ./scripts/test_local_backend.sh`

## Static analysis

- `$ ./scripts/static_validate_backend.sh`

### To run black

- `$ black src`
- `$ black tests`

### To run mypy we need to run it inside the src folder

- `$ cd src/ `
- `$ mypy .`
