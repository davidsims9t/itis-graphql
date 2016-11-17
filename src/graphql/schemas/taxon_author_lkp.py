from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.taxon_author_lkp import TaxonAuthorLkp as TaxonAuthorLkpModel

class TaxonAuthorLkp(SQLAlchemyObjectType):
    class Meta:
        model = TaxonAuthorLkpModel
        interfaces = (relay.Node, )
