from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Expert(Base):
    __tablename__ = 'experts'
    metadata = MetaData(schema='public')
    expert_id_prefix = Column(String, primary_key=True, nullable=False)
    expert_id = Column(Integer, primary_key=True, nullable=False)
    expert = Column(String(100), nullable=False)
    exp_comment = Column(String(500), nullable=True)
    update_date = Column(Date, nullable=False)
