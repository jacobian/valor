from valor.resource import Resource
from .fixtures import schema, session

# This is a bad test.
def test_resource(schema, session):
    r = Resource(schema, session, 'app')
    assert r._defn == schema['definitions']['app']

# This, also, is a bad test.
def test_resource_links(schema, session):
    r = Resource(schema, session, 'app')
    assert r.instances._url == 'https://api.heroku.com/apps'
