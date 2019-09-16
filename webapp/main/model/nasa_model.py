from .. import Base
from sqlalchemy import String, Integer, DateTime, Column, Text


class Nasa(Base):
    __tablename__ = 'imageoftheday'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    date = Column(DateTime)
    explanation = Column(Text)
    hdurl = Column(String(200))
    media_type = Column(String(50))
    title = Column(String(60))
    url = Column(String(200))
    copyright = Column(String(150), default="", nullable=True)

    def __init__(self, date, explanation, hdurl, media_type, title, url, copyright):
        self.date = date
        self.explanation = explanation
        self.hdurl = hdurl
        self.media_type = media_type
        self.service_version = service_version
        self.title = title
        self.url = url
        self.copyright = copyright

    def __repr__(self):
        return '{} {} {} {} {} {} {} {} '.format(self.id, self.title, self.explanation, self.date, self.hdurl, self.url, self.media_type, self.copyright)
    
