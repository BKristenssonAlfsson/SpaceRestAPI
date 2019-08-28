from sqlalchemy import create_engine, orm
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
#Swap to MySQL
#engine = create_engine(postgres)

Base.metadata.create_all(engine, checkfirst=True)
Session = orm.sessionmaker(bind=engine)
session = Session()


def create_app():
    app = Flask(__name__)

    return app