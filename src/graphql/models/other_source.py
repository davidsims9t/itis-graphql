from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class OtherSource(Base):
    __tablename__ = 'other_sources'
    metadata = MetaData(schema='public')
    source_id_prefix = Column(String(3), primary_key=True, nullable=False)
    source_id = Column(Integer, primary_key=True, nullable=False)
    source_type = Column(String(10), nullable=False)
    source = Column(String(64), nullable=False)
    version = Column(String(10), nullable=False)
    acquisition_date = Column(Date, nullable=False)
    source_comment = Column(String(500), nullable=True)
    update_date = Column(Date, nullable=False)
