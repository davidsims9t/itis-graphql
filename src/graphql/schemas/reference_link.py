from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.reference_link import ReferenceLink as ReferenceLinkModel

class ReferenceLink(SQLAlchemyObjectType):
    class Meta:
        model = ReferenceLinkModel
        interfaces = (relay.Node, )
