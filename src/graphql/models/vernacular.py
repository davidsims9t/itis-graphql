from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Vernacular(Base):
    __tablename__ = 'vernaculars'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    vernacular_name = Column(String(80), nullable=False)
    language = Column(String(15), nullable=False)
    approved_ind = Column(String(1), nullable=True)
    update_date = Column(Date, nullable=False)
    vern_id = Column(Integer, primary_key=True, nullable=False)
