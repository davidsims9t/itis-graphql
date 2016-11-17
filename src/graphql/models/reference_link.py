from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class ReferenceLink(Base):
    __tablename__ = 'reference_links'
    metadata = MetaData(schema='public')
    tsn = Column(String, primary_key=True, nullable=False)
    doc_id_prefix = Column(String, primary_key=True, nullable=False)
    documentation_id = Column(Integer, primary_key=True, nullable=False)
    original_desc_ind = Column(String(1), nullable=True)
    init_itis_desc_ind = Column(String(1), nullable=True)
    change_track_id = Column(Integer, nullable=True)
    vernacular_name = Column(String(80), nullable=True)
    update_date = Column(Date, nullable=False)
