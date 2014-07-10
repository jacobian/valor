from valor.service import Service
from valor.resource import Resource
from .fixtures import schema, session

def test_service_getattr(schema, session):
    s = Service(schema, session)
    assert type(s.app) == Resource
