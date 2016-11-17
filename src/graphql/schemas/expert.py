from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.expert import Expert as ExpertModel

class Expert(SQLAlchemyObjectType):
    class Meta:
        model = ExpertModel
        interfaces = (relay.Node, )
