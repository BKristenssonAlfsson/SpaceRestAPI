from .mysql import cnx

class Config(object):
    """
    Base configs
    """

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = cnx
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}