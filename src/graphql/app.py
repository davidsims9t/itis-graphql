from flask import Flask
from flask_graphql import GraphQLView
import os

from database import db_session, init_db
import schema

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
    init_db()
    app.run(host='127.0.0.1',port=int(os.environ.get('PORT')))
