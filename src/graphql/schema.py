import graphene
import json
from graphene import relay
from graphene.relay import ConnectionField
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import (
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

class Comment(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel
        interfaces = (relay.Node, )

class Expert(SQLAlchemyObjectType):
    class Meta:
        model = ExpertModel
        interfaces = (relay.Node, )

class Longname(SQLAlchemyObjectType):
    class Meta:
        model = LongnameModel
        interfaces = (relay.Node, )

class Kingdom(SQLAlchemyObjectType):
    class Meta:
        model = KingdomModel
        interfaces = (relay.Node, )

class NodcIds(SQLAlchemyObjectType):
    class Meta:
        model = NodcIdsModel
        interfaces = (relay.Node, )

class OtherSources(SQLAlchemyObjectType):
    class Meta:
        model = OtherSourcesModel
        interfaces = (relay.Node, )

class Publications(SQLAlchemyObjectType):
    class Meta:
        model = PublicationsModel
        interfaces = (relay.Node, )

class ReferenceLinks(SQLAlchemyObjectType):
    class Meta:
        model = ReferenceLinksModel
        interfaces = (relay.Node, )

class StrippedAuthor(SQLAlchemyObjectType):
    class Meta:
        model = StrippedAuthorModel
        interfaces = (relay.Node, )

class TaxonAuthorsLkp(SQLAlchemyObjectType):
    class Meta:
        model = TaxonAuthorsLkpModel
        interfaces = (relay.Node, )

class TaxonUnitTypes(SQLAlchemyObjectType):
    class Meta:
        model = TaxonUnitTypesModel
        interfaces = (relay.Node, )

class TaxonomicUnits(SQLAlchemyObjectType):
    class Meta:
        model = TaxonomicUnitsModel
        interfaces = (relay.Node, )

    taxon_unit_type = SQLAlchemyConnectionField(TaxonUnitTypes)

    def resolve_taxon_unit_type(self, args, context, info):
        return TaxonUnitTypesModel.query.filter(TaxonUnitTypesModel.rank_id.in_([self.rank_id]), TaxonUnitTypesModel.kingdom_id.in_([self.kingdom_id])).all()

class SynonymLinks(SQLAlchemyObjectType):
    class Meta:
        model = SynonymLinksModel
        interfaces = (relay.Node, )

    taxonomic_unit = SQLAlchemyConnectionField(TaxonomicUnits)

    def resolve_taxonomic_unit(self, args, context, info):
        return TaxonomicUnitsModel.query.filter(TaxonomicUnitsModel.tsn == self.tsn).all()

class TuCommentsLinks(SQLAlchemyObjectType):
    class Meta:
        model = TuCommentsLinksModel
        interfaces = (relay.Node, )

class VernRefLinks(SQLAlchemyObjectType):
    class Meta:
        model = VernRefLinksModel
        interfaces = (relay.Node, )

class Vernaculars(SQLAlchemyObjectType):
    class Meta:
        model = VernacularsModel
        interfaces = (relay.Node, )

class Hierarchy(SQLAlchemyObjectType):
    class Meta:
        model = HierarchyModel
        interfaces = (relay.Node, )

    taxonomic_unit = SQLAlchemyConnectionField(TaxonomicUnits)
    synonym_links = SQLAlchemyConnectionField(SynonymLinks)
    children = SQLAlchemyConnectionField(lambda: Hierarchy, level=graphene.Int())

    def resolve_synonym_links(self, args, context, info):
        return SynonymLinksModel.query.filter(SynonymLinksModel.tsn_accepted == self.tsn).all()

    def resolve_taxonomic_unit(self, args, context, info):
        return TaxonomicUnitsModel.query.filter(TaxonomicUnitsModel.tsn == self.tsn).all()

    def resolve_children(self, args, context, info):
        return HierarchyModel.query\
            .filter(HierarchyModel.parent_tsn == self.tsn)\
            .filter(HierarchyModel.level <= args['level']).all()

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    viewer = graphene.Field(lambda: Query)

    all_hierarchy = SQLAlchemyConnectionField(Hierarchy, tsn=graphene.Int())

    def resolve_all_hierarchy(self, args, context, info):
        tsn = args.get('tsn')
        return HierarchyModel.query.filter(HierarchyModel.tsn == tsn).all()

    all_comments = graphene.List(Comment)
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

    def resolve_viewer(self, *args, **kwargs):
        return Query

schema = graphene.Schema(query=Query, types=[Hierarchy, Kingdom])
introspection_dict = schema.introspect()

with open('data/schema.json', 'w') as fp:
    json.dump(introspection_dict, fp, ensure_ascii=False)
