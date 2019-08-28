from sqlalchemy import create_engine, orm
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from .config.mysql import engine_connection


Base = declarative_base()
engine = create_engine(engine_connection)

Session = orm.sessionmaker(bind=engine)
session = Session()

from .model import nasa_model

Base.metadata.create_all(engine)
    
def create_app():
    app = Flask(__name__)

    return app