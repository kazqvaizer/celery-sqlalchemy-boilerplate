# celery-sqlalchemy-boilerplate
[![build](https://github.com/kazqvaizer/celery-sqlalchemy-boilerplate/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/kazqvaizer/celery-sqlalchemy-boilerplate/actions/workflows/main.yml)

Boilerplate for services with Celery, SQLAlchemy, Docker, Alembic and Pytest.
            
## Why 

Here is a stable way to run scheduled or triggered tasks in python using celery. This boilerplate will fit any integration purpose when you need to synchronize resources or databases. 

Current project is pytest friendly. It is very easy to start writing tests for your code here. 

## How to start
Copy whole project and remove or rewrite all dummy code with `example` in it. There is an example migration file in `migrations/versions/` directory, so you may want to remove it also.

To set up your environment locally you need to define `SQLALCHEMY_DATABASE_URI` and `CELERY_BACKEND` parameters in `.env` file. Check `.env.example` as an example.

## Dependencies

Install pipenv
```
pip install pipenv
```

Then run 

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
cd src && pytest
```

## Code style and linters

Run all-in-one command:

```
isort . && black . && flake8
```

## Migrations

This boilerplate uses Alembic to run and create new migrations.

To auto-generate migrations:

```
alembic revision --autogenerate -m "Some migration name"
``` 

To run migration (with database on):
```
cd src && alembic upgrade head
```

To run migration in prod compose:
```
docker-compose -f docker-compose.prod.yml run celery alembic upgrade head
```
