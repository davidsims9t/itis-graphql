from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.publication import Publication as PublicationModel

class Publication(SQLAlchemyObjectType):
    class Meta:
        model = PublicationModel
        interfaces = (relay.Node, )
