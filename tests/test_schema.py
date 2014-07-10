from valor.schema import Schema
from .fixtures import schema_fname

def test_schema_from_file_name(schema_fname):
    s = Schema.from_file(schema_fname)
    assert s['title'] == 'Heroku Platform API'

def test_schema_from_stream(schema_fname):
    with open(schema_fname) as fp:
        s = Schema.from_file(fp)
        assert s['title'] == 'Heroku Platform API'

def test_schema_resolve(schema_fname):
    s = Schema.from_file(schema_fname)
    assert s.resolve_ref(s['properties']['app']['$ref']) == s['definitions']['app']
