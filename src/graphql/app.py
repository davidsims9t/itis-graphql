from flask import Flask
from flask_graphql import GraphQLView
import os

from models import db_session
from schema import (
    schema,
    Hierarchy,
    Comment,
    Expert,
    Longname,
    NodcIds,
    OtherSources,
    Publications,
    ReferenceLinks,
    StrippedAuthor,
    SynonymLinks,
    TaxonAuthorsLkp,
    TaxonUnitTypes,
    TaxonomicUnits,
    TuCommentsLinks,
    VernRefLinks,
    Vernaculars
)

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT')))
