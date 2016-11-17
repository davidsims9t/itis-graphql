from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Hierarchy(Base):
    __tablename__ = 'hierarchy'
    metadata = MetaData(schema='public')
    id = Column(String(300), nullable=True)
    hierarchy_string = Column(String(300), primary_key=True, nullable=False)
    tsn = Column(Integer, nullable=False)
    parent_tsn = Column(Integer, nullable=True)
    level = Column(Integer, nullable=False)
    childrencount = Column(Integer, nullable=False)
