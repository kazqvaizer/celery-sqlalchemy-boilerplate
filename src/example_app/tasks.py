from core.celery import celery
from core.db import session_scope


@celery.task
def example_task():
    with session_scope() as session:
        session.query()
