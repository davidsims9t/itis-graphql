# ITIS GraphQL API using Graphene

This is a sample API built with Graphene and SQLAlchemy. Data contained
in this API comes from the official [ITIS](https://www.itis.gov/) website.

## Structure

All GraphQL code is contained within the /graphql directory. React and Relay code is contained
within the components directory.

## Deploying

To deploy this example you run the code below:

Note: In order to run the example, you will need to use Python 3.

```
git clone

# Install GraphQL dependencies.
pip install

# Install React/Relay dependencies.
npm install

# Start GraphQL server
python graphql/app.py

# Start WebPack
npm start
```
