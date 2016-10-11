import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import SQLAlchemyNode, SQLAlchemyConnectionField
from models import (
    db_session,
    Expert as ExpertModel,
    Hierarchy as HierarchyModel,
    Comment as CommentModel,
    Kingdom as KingdomModel
)

schema = graphene.Schema()

@schema.register
class Comment(SQLAlchemyNode):
    class Meta:
        model = CommentModel

@schema.register
class Expert(SQLAlchemyNode):
    class Meta:
        model = ExpertModel

@schema.register
class Hierarchy(SQLAlchemyNode):
    class Meta:
        model = HierarchyModel

@schema.register
class Kingdom(SQLAlchemyNode):
    class Meta:
        model = KingdomModel

class Query(graphene.ObjectType):
    node = relay.NodeField()
    all_hierarchy = SQLAlchemyConnectionField(Hierarchy)
    all_comments = SQLAlchemyConnectionField(Comment)
    all_kingdoms = SQLAlchemyConnectionField(Kingdom)
    all_experts = SQLAlchemyConnectionField(Expert)

schema.query = Query
