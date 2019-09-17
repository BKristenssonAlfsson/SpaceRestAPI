import requests
from celery import Celery
from ..config.celeryconfig import CELERY_RESULT_BACKEND

app = Celery("nasa", broker="pyamqp://guest@localhost//", backend=CELERY_RESULT_BACKEND)


class NasaRequests:

    req = requests.Session()

    def __init__(self):
        self.req.auth = ()
    
    @app.task(queue='nasa')
    def start():
        app.send_task("NASA", kwargs=dict(value="Foo"))