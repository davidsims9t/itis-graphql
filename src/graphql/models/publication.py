from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Publication(Base):
    __tablename__ = 'publications'
    metadata = MetaData(schema='public')
    pub_id_prefix = Column(String(3), primary_key=True, nullable=False)
    publication_id = Column(Integer, primary_key=True, nullable=False)
    reference_author = Column(String(100), nullable=False)
    title = Column(String, nullable=True)
    publication_name = Column(String, nullable=False)
    listed_pub_date = Column(Date, nullable=True)
    actual_pub_date = Column(Date, nullable=True)
    publisher = Column(String(80), nullable=True)
    pub_place = Column(String(40), nullable=True)
    isbn = Column(String(16), nullable=True)
    issn = Column(String(16), nullable=True)
    pages = Column(String(15), nullable=True)
    pub_comment = Column(String(500), nullable=True)
    update_date = Column(Date, nullable=True)
