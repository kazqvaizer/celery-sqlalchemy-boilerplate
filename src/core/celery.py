import sentry_sdk
from celery import Celery
from envparse import env
from sentry_sdk.integrations.celery import CeleryIntegration

env.read_envfile()

sentry_sdk.init(env("SENTRY_SDN", default=None), integrations=[CeleryIntegration()])

celery = Celery("celery", broker=env("CELERY_BACKEND"))
