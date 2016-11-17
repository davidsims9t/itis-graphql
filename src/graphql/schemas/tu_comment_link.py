from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.tu_comment_link import TuCommentLink as TuCommentLinkModel

class TuCommentLink(SQLAlchemyObjectType):
    class Meta:
        model = TuCommentLinkModel
        interfaces = (relay.Node, )
