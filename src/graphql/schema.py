import graphene
import json
from graphene import relay
from graphene.relay import ConnectionField
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from schemas.comment import Comment
from schemas.hierarchy import Hierarchy
from schemas.expert import Expert
from schemas.kingdom import Kingdom
from schemas.longname import Longname
from schemas.nodc_id import NodcId
from schemas.other_source import OtherSource
from schemas.publication import Publication
from schemas.reference_link import ReferenceLink
from schemas.stripped_author import StrippedAuthor
from schemas.synonym_link import SynonymLink
from schemas.taxon_author_lkp import TaxonAuthorLkp
from schemas.taxon_unit_type import TaxonUnitType
from schemas.taxonomic_unit import TaxonomicUnit
from schemas.tu_comment_link import TuCommentLink
from schemas.vern_ref_link import VernRefLink
from schemas.vernacular import Vernacular

from models.hierarchy import Hierarchy as HierarchyModel

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    viewer = graphene.Field(lambda: Query)

    all_hierarchy = SQLAlchemyConnectionField(Hierarchy, tsn=graphene.Int())

    def resolve_all_hierarchy(self, args, context, info):
        tsn = args.get('tsn')
        return HierarchyModel.query.filter(HierarchyModel.tsn == tsn).all()

    all_comments = SQLAlchemyConnectionField(Comment)
    all_kingdoms = SQLAlchemyConnectionField(Kingdom)
    all_experts = SQLAlchemyConnectionField(Expert)
    all_longnames = SQLAlchemyConnectionField(Longname)
    all_nodc_ids = SQLAlchemyConnectionField(NodcId)
    all_other_sources = SQLAlchemyConnectionField(OtherSource)
    all_publications = SQLAlchemyConnectionField(Publication)
    all_reference_links = SQLAlchemyConnectionField(ReferenceLink)
    all_stripped_author = SQLAlchemyConnectionField(StrippedAuthor)
    all_synonym_links = SQLAlchemyConnectionField(SynonymLink)
    all_taxon_authors_lkp = SQLAlchemyConnectionField(TaxonAuthorLkp)
    all_taxon_unit_types = SQLAlchemyConnectionField(TaxonUnitType)
    all_taxonomic_units = SQLAlchemyConnectionField(TaxonomicUnit)
    all_tu_comments_links = SQLAlchemyConnectionField(TuCommentLink)
    all_vern_ref_links = SQLAlchemyConnectionField(VernRefLink)
    all_vernaculars = SQLAlchemyConnectionField(Vernacular)

    def resolve_viewer(self, *args, **kwargs):
        return Query

schema = graphene.Schema(query=Query)
introspection_dict = schema.introspect()

with open('data/schema.json', 'w') as fp:
    json.dump(introspection_dict, fp, ensure_ascii=False)
