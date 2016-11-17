from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.stripped_author import StrippedAuthor as StrippedAuthorModel

class StrippedAuthor(SQLAlchemyObjectType):
    class Meta:
        model = StrippedAuthorModel
        interfaces = (relay.Node, )
