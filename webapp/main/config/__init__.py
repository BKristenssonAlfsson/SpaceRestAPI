from .mysql import cnx
from .mongo import MongoDatabase
from celery.schedules import crontab
from .celeryconfig import CELERY_BEATS

class Config(object):
    """
    Base configs
    """

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = cnx
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MONGO_URI = MongoDatabase
    CELERY_HEARTBEAT = CELERY_BEATS


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}