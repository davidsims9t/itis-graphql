from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Kingdom(Base):
    __tablename__ = 'kingdoms'
    metadata = MetaData(schema='public')
    id = Column(Integer, nullable=True)
    kingdom_id = Column(Integer, primary_key=True, nullable=False)
    kingdom_name = Column(String(10), nullable=False)
    tsn = Column(Integer, nullable=True)
    update_date = Column(Date, nullable=False)
