from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class VernRefLink(Base):
    __tablename__ = 'vern_ref_links'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    doc_id_prefix = Column(String(3), primary_key=True, nullable=False)
    documentation_id = Column(Integer, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
    vern_id = Column(Integer, primary_key=True, nullable=False)
