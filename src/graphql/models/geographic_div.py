from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class GeographicDiv(Base):
    __tablename__ = 'geographic_div'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    geographic_value = Column(String, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
