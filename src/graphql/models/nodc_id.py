from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class NodcId(Base):
    __tablename__ = 'nodc_ids'
    metadata = MetaData(schema='public')
    nodc_id = Column(String(12), primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
    tsn = Column(Integer, primary_key=True, nullable=False)
