from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Longname(Base):
    __tablename__ = 'longnames'
    metadata = MetaData(schema='public')
    id = Column(Integer, nullable=True)
    tsn = Column(Integer, primary_key=True, nullable=False)
    completename = Column(String(300), nullable=False)
