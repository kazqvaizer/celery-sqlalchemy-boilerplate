# celery-sqlalchemy-boilerplate
Boilerplate for services with Celery, SQLAlchemy, Docker, Alembic and Pytest.


## How to start
Copy whole project and remove or rewrite all dummy code with `example` in it. There is an example migration file in `migrations/versions/` directory, so you may want to remove it also.

To setup your environment locally for tests you need to define database and tasks broker urls. You can copy `.env.example` file to `.env` for this. It is ready to use with `docker-compose up` command.

In production you need to define `SQLALCHEMY_DATABASE_URI` and `CELERY_BACKEND` enviroment variables for your service.


## Dependencies

Install pipenv if you don`t have one:
```
pip install pipenv
```

Then simply run 

```
pipenv install
```

## Code your project

Create celery tasks inside `src/app/tasks.py` files as usual:

```
from app.celery import celery
from app.db import session_scope


@celery.task
def example_task():
    with session_scope() as session:
        my_celery_task_logic(session)
```

Extend `src/app/celery.py` with schedule for your tasks: 

```
from celery.schedules import crontab

celery.conf.beat_schedule = {
    "example_task": {
        "task": "app.tasks.example_task", 
        "schedule": crontab(minute="*")
    }
}

```

## Tests

There are ready-to-use database fixtures which can greatly help with testing your code in near to production way. Don't forget to run your database, e.g. with `docker-compose up -d` command.

To run tests:


```
pytest
```

## Code style and linters

Run all-in-one command:

```
isort -rc . && black . && flake8
```

## Migrations

This boilerplate uses Alembic to run and create new migrations.

To auto-generate migrations:

```
alembic revision --autogenerate -m "Some migration name"
``` 

To run migration (with database on):
```
alembic upgrade head
```