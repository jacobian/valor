import pytest
from valor import model
from .fixtures import schema

def test_model_factory(schema):
    App = model.model_factory('App', schema, schema['definitions']['app'])
    assert App.__name__ == 'App'
    assert App.schema == schema

def test_model_getattr(schema):
    App = model.model_factory('App', schema, schema['definitions']['app'])
    a = App(name='my-app')
    assert a.name == 'my-app'
    with pytest.raises(AttributeError):
        a.foobar

def test_model_setattr(schema):
    App = model.model_factory('App', schema, schema['definitions']['app'])
    a = App(name='my-app')
    a.name = 'changed'
    assert a.name == 'changed'
