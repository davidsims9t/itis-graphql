import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import SQLAlchemyNode, SQLAlchemyConnectionField
from models import (
    db_session,
    Expert as ExpertModel,
    Hierarchy as HierarchyModel,
    Comment as CommentModel,
    Kingdom as KingdomModel,
    Longnames as LongnameModel,
    NodcIds as NodcIdsModel,
    OtherSources as OtherSourcesModel,
    Publications as PublicationsModel,
    ReferenceLinks as ReferenceLinksModel,
    StrippedAuthor as StrippedAuthorModel,
    SynonymLinks as SynonymLinksModel,
    TaxonAuthorsLkp as TaxonAuthorsLkpModel,
    TaxonUnitTypes as TaxonUnitTypesModel,
    TaxonomicUnits as TaxonomicUnitsModel,
    TuCommentsLinks as TuCommentsLinksModel,
    VernRefLinks as VernRefLinksModel,
    Vernaculars as VernacularsModel
)

schema = graphene.Schema()

@schema.register
class Comment(SQLAlchemyNode):
    class Meta:
        model = CommentModel

@schema.register
class Expert(SQLAlchemyNode):
    class Meta:
        model = ExpertModel

@schema.register
class Hierarchy(SQLAlchemyNode):
    class Meta:
        model = HierarchyModel

@schema.register
class Kingdom(SQLAlchemyNode):
    class Meta:
        model = KingdomModel

@schema.register
class Longname(SQLAlchemyNode):
    class Meta:
        model = LongnameModel

@schema.register
class NodcIds(SQLAlchemyNode):
    class Meta:
        model = NodcIdsModel

@schema.register
class OtherSources(SQLAlchemyNode):
    class Meta:
        model = OtherSourcesModel

@schema.register
class Publications(SQLAlchemyNode):
    class Meta:
        model = PublicationsModel

@schema.register
class ReferenceLinks(SQLAlchemyNode):
    class Meta:
        model = ReferenceLinksModel

@schema.register
class StrippedAuthor(SQLAlchemyNode):
    class Meta:
        model = StrippedAuthorModel

@schema.register
class SynonymLinks(SQLAlchemyNode):
    class Meta:
        model = SynonymLinksModel

@schema.register
class TaxonAuthorsLkp(SQLAlchemyNode):
    class Meta:
        model = TaxonAuthorsLkpModel

@schema.register
class TaxonUnitTypes(SQLAlchemyNode):
    class Meta:
        model = TaxonUnitTypesModel

@schema.register
class TaxonomicUnits(SQLAlchemyNode):
    class Meta:
        model = TaxonomicUnitsModel

@schema.register
class TuCommentsLinks(SQLAlchemyNode):
    class Meta:
        model = TuCommentsLinksModel

@schema.register
class VernRefLinks(SQLAlchemyNode):
    class Meta:
        model = VernRefLinksModel

@schema.register
class Vernaculars(SQLAlchemyNode):
    class Meta:
        model = VernacularsModel

class Query(graphene.ObjectType):
    node = relay.NodeField()
    all_hierarchy = SQLAlchemyConnectionField(Hierarchy)
    all_comments = SQLAlchemyConnectionField(Comment)
    all_kingdoms = SQLAlchemyConnectionField(Kingdom)
    all_experts = SQLAlchemyConnectionField(Expert)
    all_longnames = SQLAlchemyConnectionField(Longname)
    all_nodc_ids = SQLAlchemyConnectionField(NodcIds)
    all_other_sources = SQLAlchemyConnectionField(OtherSources)
    all_publications = SQLAlchemyConnectionField(Publications)
    all_reference_links = SQLAlchemyConnectionField(ReferenceLinks)

schema.query = Query
