import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import SQLAlchemyNode, SQLAlchemyConnectionField
from models import db_session, Hierarchy as HierarchyModel

schema = graphene.Schema()

@schema.register
class Hierarchy(SQLAlchemyNode):
    class Meta:
        model = HierarchyModel

class Query(graphene.ObjectType):
    node = relay.NodeField()
    all_hierarchy = SQLAlchemyConnectionField(Hierarchy)

schema.query = Query
