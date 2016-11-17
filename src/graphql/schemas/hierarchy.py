import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .taxonomic_unit import TaxonomicUnit
from .synonym_link import SynonymLink

from models.hierarchy import Hierarchy as HierarchyModel
from models.taxonomic_unit import TaxonomicUnit as TaxonomicUnitModel
from models.synonym_link import SynonymLink as SynonymLinkModel

class Hierarchy(SQLAlchemyObjectType):
    class Meta:
        model = HierarchyModel
        interfaces = (relay.Node, )

    taxonomic_unit = SQLAlchemyConnectionField(TaxonomicUnit)
    synonym_links = SQLAlchemyConnectionField(SynonymLink)
    children = SQLAlchemyConnectionField(lambda: Hierarchy, level=graphene.Int())

    def resolve_synonym_links(self, args, context, info):
        return SynonymLinkModel.query.filter(SynonymLinkModel.tsn_accepted == self.tsn).all()

    def resolve_taxonomic_unit(self, args, context, info):
        return TaxonomicUnitModel.query.filter(TaxonomicUnitModel.tsn == self.tsn).all()

    def resolve_children(self, args, context, info):
        return HierarchyModel.query\
            .filter(HierarchyModel.parent_tsn == self.tsn)\
            .filter(HierarchyModel.level <= args['level']).all()
