from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from .taxon_unit_type import TaxonUnitType
from models.taxonomic_unit import TaxonomicUnit as TaxonomicUnitModel
from models.taxon_unit_type import TaxonUnitType as TaxonUnitTypeModel

from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class TaxonomicUnit(SQLAlchemyObjectType):
    class Meta:
        model = TaxonomicUnitModel
        interfaces = (relay.Node, )

    taxon_unit_type = SQLAlchemyConnectionField(TaxonUnitType)

    def resolve_taxon_unit_type(self, args, context, info):
        return TaxonUnitTypeModel.query.filter(\
            TaxonUnitTypeModel.rank_id == self.rank_id,\
            TaxonUnitTypeModel.kingdom_id == self.kingdom_id\
        ).all()
