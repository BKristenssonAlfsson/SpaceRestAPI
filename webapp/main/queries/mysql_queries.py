from .. import session
from ..model.nasa_model import Nasa

def check_title(title):
    exist = session.query(Nasa).filter(Nasa.title == title).scalar()

    if (exist is not None):
        return "False"
    else:
        return "OK"