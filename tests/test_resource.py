from valor.resource import Resource
from .fixtures import schema, session

def test_resource_dir(schema, session):
    r = Resource(schema, session, 'config-var')
    assert dir(r) == ['info', 'update']
