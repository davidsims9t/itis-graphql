from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class StrippedAuthor(Base):
    __tablename__ = 'strippedauthor'
    metadata = MetaData(schema='public')
    taxon_author_id = Column(Integer, primary_key=True, nullable=False)
    shortauthor = Column(String(100), nullable=False)
