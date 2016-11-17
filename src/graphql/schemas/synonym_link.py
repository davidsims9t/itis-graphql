from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.synonym_link import SynonymLink as SynonymLinkModel
from .taxonomic_unit import TaxonomicUnit

class SynonymLink(SQLAlchemyObjectType):
    class Meta:
        model = SynonymLinkModel
        interfaces = (relay.Node, )

    taxonomic_unit = SQLAlchemyConnectionField(TaxonomicUnit)

    def resolve_taxonomic_unit(self, args, context, info):
        return TaxonomicUnitModel.query.filter(TaxonomicUnitModel.tsn == self.tsn).all()
