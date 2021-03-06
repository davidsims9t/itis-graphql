from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class Comment(Base):
    __tablename__ = 'comments'
    metadata = MetaData(schema='public')
    comment_id = Column(Integer, primary_key=True, nullable=False)
    commentator = Column(String(100), nullable=True)
    comment_detail = Column(String, nullable=False)
    comment_time_stamp = Column(DateTime, nullable=False)
    update_date = Column(Date, nullable=False)
