from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class TaxonAuthorLkp(Base):
    __tablename__ = 'taxon_authors_lkp'
    metadata = MetaData(schema='public')
    taxon_author_id = Column(Integer, primary_key=True, nullable=False)
    taxon_author = Column(String(100), nullable=False)
    update_date = Column(Date, nullable=False)
    kingdom_id = Column(Integer, primary_key=True, nullable=False)
    short_author = Column(String, nullable=True)
