import os
import pytest
from valor.schema import Schema
from valor.service import Service, Resource

@pytest.fixture
def schema():
    return Schema.from_file(os.path.join(os.path.dirname(__file__), 'schema.json'))

@pytest.fixture
def session():
    # FIXME!
    return None

# This is a bad test.
def test_resource(schema, session):
    r = Resource(schema, session, 'app')
    assert r._defn == schema['definitions']['app']

# This, also, is a bad test.
def test_links(schema, session):
    r = Resource(schema, session, 'app')
    assert r.instances._url == 'https://api.heroku.com/apps'

# In fact, turns out all of these are bad tests.
def test_service_getattr(schema, session):
    s = Service(schema, session)
    assert type(s.app) == Resource
