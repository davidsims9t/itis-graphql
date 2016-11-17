from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class SynonymLink(Base):
    __tablename__ = 'synonym_links'
    metadata = MetaData(schema='public')
    id = Column(String(50), nullable=True)
    tsn = Column(Integer, primary_key=True, nullable=False)
    tsn_accepted = Column(Integer, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
