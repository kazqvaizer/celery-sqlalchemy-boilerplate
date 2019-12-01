# celery-sqlalchemy-boilerplate
Boilerplate for services with DB and scheduled tasks in celery with migrations and tests.

## Structure

You can easily add apps in this project with alchemy models and celery tasks like this:

```
my_project/
└── src/
    ├── example_app/
    │   ├── models.py
    │   └── tasks.py
    └── another_example_app/
       ├── models.py
       └── tasks.py

```

Create celery tasks inside `tasks.py` files as usual:

```
from app.celery import celery
from app.db import session_scope


@celery.task
def example_task():
    with session_scope() as session:
        my_celery_task_logic(session)
```


Extend `src/app/celery.py` with schudele for your tasks: 

```
from celery.schedules import crontab
celery.autodiscover_tasks(lambda: ("example_app",))
 
celery.conf.beat_schedule = {
    "example_task": {
        "task": "example_app.tasks.example_task",
        "schedule": crontab(hour="*", minute="0,30"),
    },
}
```

## Migrations

