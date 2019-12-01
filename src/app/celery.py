import sentry_sdk
from celery import Celery
from celery.schedules import crontab
from envparse import env
from sentry_sdk.integrations.celery import CeleryIntegration

env.read_envfile()

sentry_sdk.init(env("SENTRY_SDN", default=None), integrations=[CeleryIntegration()])

celery = Celery("app", broker=env("CELERY_BACKEND"))

celery.autodiscover_tasks(lambda: ("app",))

celery.conf.beat_schedule = {
    "example_task": {"task": "app.tasks.example_task", "schedule": crontab(minute="*")}
}
