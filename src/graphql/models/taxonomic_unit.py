from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class TaxonomicUnit(Base):
    __tablename__ = 'taxonomic_units'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    id = Column(String(100), nullable=True)
    unit_ind1 = Column(String(1), nullable=True)
    unit_name1 = Column(String(35), nullable=False)
    unit_ind2 = Column(String(1), nullable=True)
    unit_name2 = Column(String(35), nullable=True)
    unit_ind3 = Column(String(7), nullable=True)
    unit_name3 = Column(String(35), nullable=True)
    unit_ind4 = Column(String(7), nullable=True)
    unit_name4 = Column(String(35), nullable=True)
    unnamed_taxon_ind = Column(String(1), nullable=True)
    name_usage = Column(String(12), nullable=False)
    unaccept_reason = Column(String(50), nullable=True)
    credibility_rtng = Column(String(40), nullable=False)
    completeness_rtng = Column(String(10), nullable=True)
    currency_rating = Column(String(7), nullable=True)
    phylo_sort_seq = Column(Integer, nullable=True)
    initial_time_stamp = Column(DateTime, nullable=False)
    parent_tsn = Column(Integer, nullable=True)
    taxon_author_id = Column(Integer, nullable=True)
    hybrid_author_id = Column(Integer, nullable=True)
    kingdom_id = Column(Integer, nullable=False)
    rank_id = Column(Integer, nullable=False)
    update_date = Column(Date, nullable=False)
    uncertain_prnt_ind = Column(String(3), nullable=True)
    n_usage = Column(String, nullable=True)
    complete_name = Column(String, nullable=False)
