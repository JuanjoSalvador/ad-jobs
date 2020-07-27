from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app import db

class Offers(db.Model):
    __tablename__ = 'ofertas'
    id = Column(Integer, primary_key=True)
    job = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    description = Column(String(255))
    salary = Column(Integer)
    localization = Column(String(50))
    requirements = Column(Text)
    extra = Column(Text)
    contact = Column(String(100), nullable=False)	

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))