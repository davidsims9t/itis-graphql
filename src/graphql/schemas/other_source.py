from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.other_source import OtherSource as OtherSourceModel

class OtherSource(SQLAlchemyObjectType):
    class Meta:
        model = OtherSourceModel
        interfaces = (relay.Node, )
