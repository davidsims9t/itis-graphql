from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.longname import Longname as LongnameModel

class Longname(SQLAlchemyObjectType):
    class Meta:
        model = LongnameModel
        interfaces = (relay.Node, )
