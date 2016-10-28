from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres:///ITIS', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Comment(Base):
    __tablename__ = 'comments'
    metadata=MetaData(schema='public')
    comment_id = Column(Integer, primary_key=True)
    commentator = Column(String)
    comment_detail = Column(String)
    comment_time_stamp = Column(String)
    update_date = Column(String)

class GeographicDiv(Base):
    __tablename__ = 'geographic_div'
    metadata=MetaData(schema='public')
    tsn = Column(Integer, primary_key=True)
    geographic_value = Column(String, primary_key=True)
    update_date = Column(Date)

class Expert(Base):
    __tablename__ = 'experts'
    metadata=MetaData(schema='public')
    expert_id_prefix = Column(String)
    expert_id = Column(Integer, primary_key=True)
    expert = Column(String)
    exp_comment = Column(String)
    update_date = Column(String)

class Hierarchy(Base):
    __tablename__ = 'hierarchy'
    metadata=MetaData(schema='public')
    hierarchy_string = Column(String, primary_key=True)
    tsn = Column(Integer)
    parent_tsn = Column(Integer)
    level = Column(Integer)
    childrencount = Column(Integer)

class Kingdom(Base):
    __tablename__ = 'kingdoms'
    metadata=MetaData(schema='public')
    kingdom_id = Column(Integer, primary_key=True)
    kingdom_name = Column(String)
    update_date = Column(String)

class Longnames(Base):
    __tablename__ = 'longnames'
    metadata=MetaData(schema='public')
    tsn = Column(Integer, primary_key=True)
    completename = Column(String)

class NodcIds(Base):
    __tablename__ = 'nodc_ids'
    metadata=MetaData(schema='public')
    nodc_id = Column(Integer, primary_key=True)
    update_date = Column(String)
    tsn = Column(String)
