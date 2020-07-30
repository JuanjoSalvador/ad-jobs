from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from app import db

class Offers(db.Model):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    description = Column(String(255))
    salary = Column(Integer)
    localization = Column(String(50))
    requirements = Column(Text)
    extra = Column(Text)
    contact = Column(String(100), nullable=False)
    approbed = Column(Boolean)
    
    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

    @staticmethod
    def get_all():
        return Offers.query.all()

    @staticmethod
    def get_not_reviewed():
        return Offers.query.filter_by(approbed = None)

    @staticmethod
    def get_last_offers():
        return Offers.query.filter_by(approbed = None).order_by(Offers.id.desc()).limit(3)

    @staticmethod
    def get_approbed():
        return Offers.query.filter_by(approbed = True)

    @staticmethod
    def get_rejected():
        return Offers.query.filter_by(approbed = False)

    @staticmethod
    def get_by_id(id):
        return Offers.query.filter_by(id=id).first()