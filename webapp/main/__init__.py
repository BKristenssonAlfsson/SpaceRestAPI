from sqlalchemy import create_engine, orm
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from .config.mysql import mysql


Base = declarative_base()



def create_app():
    app = Flask(__name__)

    return app