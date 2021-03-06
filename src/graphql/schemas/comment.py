from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.comment import Comment as CommentModel

class Comment(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel
        interfaces = (relay.Node, )
