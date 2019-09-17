# Rewrite with Celery Beats, Routes, Scheduler to have async updates to SpringBoot
from celery.schedules import crontab

CELERY_RESULT_BACKEND = "amqp"

CELERY_BROKER = "pyamqp://guest@localhost//"

CELERY_ROUTES = {
    'nasa': {'queue': 'nasa'}
}

CELERY_BEATS = {
    'nasa': {
        'task': 'main.to_rabbit.NasaRequests.nasa',
        'schedule': crontab(minute=1)
    },
}