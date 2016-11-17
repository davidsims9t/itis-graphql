from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class TuCommentLink(Base):
    __tablename__ = 'tu_comments_links'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    comment_id = Column(Integer, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
