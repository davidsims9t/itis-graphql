from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.kingdom import Kingdom as KingdomModel

class Kingdom(SQLAlchemyObjectType):
    class Meta:
        model = KingdomModel
        interfaces = (relay.Node, )
