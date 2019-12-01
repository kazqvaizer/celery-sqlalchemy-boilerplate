from app.celery import celery
from app.db import session_scope
from app.models import ExampleModel


@celery.task
def example_task():
    with session_scope() as session:
        session.add(ExampleModel())
