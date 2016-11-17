from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.vern_ref_link import VernRefLink as VernRefLinkModel

class VernRefLink(SQLAlchemyObjectType):
    class Meta:
        model = VernRefLinkModel
        interfaces = (relay.Node, )
