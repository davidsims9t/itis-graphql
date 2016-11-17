from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.nodc_id import NodcId as NodcIdModel

class NodcId(SQLAlchemyObjectType):
    class Meta:
        model = NodcIdModel
        interfaces = (relay.Node, )
