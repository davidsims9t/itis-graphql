import graphene
import json
from graphene import relay
from graphene.contrib.sqlalchemy import SQLAlchemyNode, SQLAlchemyObjectType, SQLAlchemyConnectionField
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
class Longname(SQLAlchemyNode):
    class Meta:
        model = LongnameModel

@schema.register
class Kingdom(SQLAlchemyNode):
    class Meta:
        model = KingdomModel

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

    taxon_unit_type = SQLAlchemyConnectionField(TaxonUnitTypes)

    def resolve_taxon_unit_type(self, args, info):
        return TaxonUnitTypesModel.query.filter(TaxonUnitTypesModel.rank_id.in_([self.rank_id]), TaxonUnitTypesModel.kingdom_id.in_([self.kingdom_id])).all()

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

class HierarchyBase(SQLAlchemyNode):
    class Meta:
        model = HierarchyModel

    taxonomic_unit = SQLAlchemyConnectionField(Longname)

    def resolve_longname(self, args, info):
        return TaxonomicUnitsModel.query.filter(TaxonomicUnitsModel.tsn.in_([self.tsn])).all()

@schema.register
class Hierarchy(SQLAlchemyNode):
    class Meta:
        model = HierarchyModel

    taxonomic_unit = SQLAlchemyConnectionField(TaxonomicUnits)
    children = SQLAlchemyConnectionField(HierarchyBase)

    def resolve_children(self, args, info):
        return HierarchyModel.query.filter(HierarchyModel.parent_tsn.in_([self.tsn])).all()

    def resolve_taxonomic_unit(self, args, info):
        return TaxonomicUnitsModel.query.filter(TaxonomicUnitsModel.tsn.in_([self.tsn])).all()

class Viewer(graphene.ObjectType):
    all_hierarchy = SQLAlchemyConnectionField(Hierarchy, tsn=graphene.Int())

    def resolve_all_hierarchy(self, args, info):
        tsn = args.get('tsn')
        return HierarchyModel.query.filter(HierarchyModel.tsn.in_([tsn])).all()

    all_comments = SQLAlchemyConnectionField(Comment)
    all_kingdoms = SQLAlchemyConnectionField(Kingdom)
    all_experts = SQLAlchemyConnectionField(Expert)
    all_longnames = SQLAlchemyConnectionField(Longname)
    all_nodc_ids = SQLAlchemyConnectionField(NodcIds)
    all_other_sources = SQLAlchemyConnectionField(OtherSources)
    all_publications = SQLAlchemyConnectionField(Publications)
    all_reference_links = SQLAlchemyConnectionField(ReferenceLinks)
    all_stripped_author = SQLAlchemyConnectionField(StrippedAuthor)
    all_synonym_links = SQLAlchemyConnectionField(SynonymLinks)
    all_taxon_authors_lkp = SQLAlchemyConnectionField(TaxonAuthorsLkp)
    all_taxon_unit_types = SQLAlchemyConnectionField(TaxonUnitTypes)
    all_taxonomic_units = SQLAlchemyConnectionField(TaxonomicUnits)
    all_tu_comments_links = SQLAlchemyConnectionField(TuCommentsLinks)
    all_vern_ref_links = SQLAlchemyConnectionField(VernRefLinks)
    all_vernaculars = SQLAlchemyConnectionField(Vernaculars)

class Query(graphene.ObjectType):
    node = relay.NodeField()
    viewer = graphene.Field(Viewer)

    def resolve_viewer(self, *args, **kwargs):
        return self

schema.query = Query

introspection_dict = schema.introspect()

with open('data/schema.json', 'w') as fp:
    json.dump(introspection_dict, fp, ensure_ascii=False)
