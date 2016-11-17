from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.vernacular import Vernacular as VernacularModel

class Vernacular(SQLAlchemyObjectType):
    class Meta:
        model = VernacularModel
        interfaces = (relay.Node, )
