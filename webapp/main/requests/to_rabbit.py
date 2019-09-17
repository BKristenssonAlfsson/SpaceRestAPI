import requests
from celery import Celery
from ..config.celeryconfig import CELERY_RESULT_BACKEND, CELERY_ROUTES, CELERY_BROKER

app = Celery("nasa", broker=CELERY_BROKER, backend=CELERY_RESULT_BACKEND)


class NasaRequests:

    req = requests.Session()

    def __init__(self):
        self.req.auth = ()
    
    @app.task()
    def nasa():
        app.send_task(name="NASA", queue='nasa', kwargs=dict(value="iotd"))