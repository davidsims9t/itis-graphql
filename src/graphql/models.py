from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(os.environ.get('DATABASE_URL'), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Comment(Base):
    __tablename__ = 'comments'
    metadata = MetaData(schema='public')
    comment_id = Column(Integer, primary_key=True, nullable=False)
    commentator = Column(String(100), nullable=True)
    comment_detail = Column(String, nullable=False)
    comment_time_stamp = Column(DateTime, nullable=False)
    update_date = Column(Date, nullable=False)

class GeographicDiv(Base):
    __tablename__ = 'geographic_div'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    geographic_value = Column(String, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)

class Expert(Base):
    __tablename__ = 'experts'
    metadata = MetaData(schema='public')
    expert_id_prefix = Column(String, primary_key=True, nullable=False)
    expert_id = Column(Integer, primary_key=True, nullable=False)
    expert = Column(String(100), nullable=False)
    exp_comment = Column(String(500), nullable=True)
    update_date = Column(Date, nullable=False)

class Hierarchy(Base):
    __tablename__ = 'hierarchy'
    metadata = MetaData(schema='public')
    id = Column(String(300), nullable=True)
    hierarchy_string = Column(String(300), primary_key=True, nullable=False)
    tsn = Column(Integer, nullable=False)
    parent_tsn = Column(Integer, nullable=True)
    level = Column(Integer, nullable=False)
    childrencount = Column(Integer, nullable=False)

class Kingdom(Base):
    __tablename__ = 'kingdoms'
    metadata = MetaData(schema='public')
    id = Column(Integer, nullable=True)
    kingdom_id = Column(Integer, primary_key=True, nullable=False)
    kingdom_name = Column(String(10), nullable=False)
    update_date = Column(Date, nullable=False)

class Longnames(Base):
    __tablename__ = 'longnames'
    metadata = MetaData(schema='public')
    id = Column(Integer, nullable=True)
    tsn = Column(Integer, primary_key=True, nullable=False)
    completename = Column(String(300), nullable=False)

class NodcIds(Base):
    __tablename__ = 'nodc_ids'
    metadata = MetaData(schema='public')
    nodc_id = Column(String(12), primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
    tsn = Column(Integer, primary_key=True, nullable=False)

class OtherSources(Base):
    __tablename__ = 'other_sources'
    metadata = MetaData(schema='public')
    source_id_prefix = Column(String(3), primary_key=True, nullable=False)
    source_id = Column(Integer, primary_key=True, nullable=False)
    source_type = Column(String(10), nullable=False)
    source = Column(String(64), nullable=False)
    version = Column(String(10), nullable=False)
    acquisition_date = Column(Date, nullable=False)
    source_comment = Column(String(500), nullable=True)
    update_date = Column(Date, nullable=False)

class Publications(Base):
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

class ReferenceLinks(Base):
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

class StrippedAuthor(Base):
    __tablename__ = 'strippedauthor'
    metadata = MetaData(schema='public')
    taxon_author_id = Column(Integer, primary_key=True, nullable=False)
    shortauthor = Column(String(100), nullable=False)

class SynonymLinks(Base):
    __tablename__ = 'synonym_links'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    tsn_accepted = Column(Integer, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)

class TaxonAuthorsLkp(Base):
    __tablename__ = 'taxon_authors_lkp'
    metadata = MetaData(schema='public')
    taxon_author_id = Column(Integer, primary_key=True, nullable=False)
    taxon_author = Column(String(100), nullable=False)
    update_date = Column(Date, nullable=False)
    kingdom_id = Column(Integer, primary_key=True, nullable=False)
    short_author = Column(String, nullable=True)

class TaxonUnitTypes(Base):
    __tablename__ = 'taxon_unit_types'
    metadata = MetaData(schema='public')
    kingdom_id = Column(Integer, primary_key=True, nullable=False)
    rank_id = Column(Integer, primary_key=True, nullable=False)
    id = Column(String(50), nullable=True)
    rank_name = Column(String(15), nullable=False)
    dir_parent_rank_id = Column(Integer, nullable=False)
    req_parent_rank_id = Column(Integer, nullable=False)
    update_date = Column(Date, nullable=False)

class TaxonomicUnits(Base):
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

class TuCommentsLinks(Base):
    __tablename__ = 'tu_comments_links'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    comment_id = Column(Integer, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)

class VernRefLinks(Base):
    __tablename__ = 'vern_ref_links'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    doc_id_prefix = Column(String(3), primary_key=True, nullable=False)
    documentation_id = Column(Integer, primary_key=True, nullable=False)
    update_date = Column(Date, nullable=False)
    vern_id = Column(Integer, primary_key=True, nullable=False)

class Vernaculars(Base):
    __tablename__ = 'vernaculars'
    metadata = MetaData(schema='public')
    tsn = Column(Integer, primary_key=True, nullable=False)
    vernacular_name = Column(String(80), nullable=False)
    language = Column(String(15), nullable=False)
    approved_ind = Column(String(1), nullable=True)
    update_date = Column(Date, nullable=False)
    vern_id = Column(Integer, primary_key=True, nullable=False)
