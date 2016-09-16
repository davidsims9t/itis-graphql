from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres:///ITIS', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

class Hierarchy(Base):
    __tablename__ = 'hierarchy'
    hierarchy_string = Column(String, primary_key=True)
    tsn = Column(Integer)
    parent_tsn = Column(Integer)
    level = Column(Integer)
    childrencount = Column(Integer)
