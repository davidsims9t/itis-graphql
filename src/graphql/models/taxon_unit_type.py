from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class TaxonUnitType(Base):
    __tablename__ = 'taxon_unit_types'
    metadata = MetaData(schema='public')
    kingdom_id = Column(Integer, primary_key=True, nullable=False)
    rank_id = Column(Integer, primary_key=True, nullable=False)
    id = Column(String(50), nullable=True)
    rank_name = Column(String(15), nullable=False)
    dir_parent_rank_id = Column(Integer, nullable=False)
    req_parent_rank_id = Column(Integer, nullable=False)
    update_date = Column(Date, nullable=False)
