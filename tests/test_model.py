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

def test_model_identity_not_id(schema):
    App = model.model_factory('App', schema, schema['definitions']['app'])
    a = App(id='1234', name='my-app')
    assert a.identity() == 'my-app'

def test_model_identity_only_id(schema):
    AppSetup = model.model_factory('AppSetup', schema, schema['definitions']['app-setup'])
    a = AppSetup(id='1234')
    assert a.identity() == '1234'

def test_model_repr(schema):
    App = model.model_factory('App', schema, schema['definitions']['app'])
    a = App(id='1234', name='my-app')
    assert repr(a) == '<App: my-app>'
