from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.taxon_unit_type import TaxonUnitType as TaxonUnitTypeModel

class TaxonUnitType(SQLAlchemyObjectType):
    class Meta:
        model = TaxonUnitTypeModel
        interfaces = (relay.Node, )
