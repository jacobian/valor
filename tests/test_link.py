import json
import pytest
from valor import Service
from .fixtures import schema, session

def test_link_interpolate_args(schema, session):
    link = Service(schema, session).app.delete
    assert link.interpolate_args(['my-app']) == 'https://api.heroku.com/apps/my-app'

def test_link_interpolate_args_too_few(schema, session):
    link = Service(schema, session).app.delete
    with pytest.raises(TypeError):
        link.interpolate_args([])

def test_link_interpolate_args_too_many(schema, session):
    link = Service(schema, session).app.delete
    with pytest.raises(TypeError):
        link.interpolate_args(['foo', 'bar'])

def test_link_construct_body(schema, session):
    link = Service(schema, session).app.create
    body = link.construct_body({'stack': 'cedar'})
    assert json.loads(body) == {'stack': 'cedar'}

def test_link_construct_body_no_body(schema, session):
    link = Service(schema, session).app.delete
    assert link.construct_body({}) is None
    with pytest.raises(TypeError):
        link.construct_body({'bad': 'arg'})

def test_link_construct_body_unexpected_arg(schema, session):
    link = Service(schema, session).app.create
    with pytest.raises(TypeError):
        link.construct_body({'stack': 'cedar', 'bad': 'arg'})

def test_link_construct_body_missing_required_arg(schema, session):
    link = Service(schema, session).app.create
    link._link['schema']['required'] = ['stack']
    with pytest.raises(TypeError):
        link.construct_body({})

def test_link_construct_body_patternProperties(schema, session):
    link = Service(schema, session).config_var.update
    body = link.construct_body({'PIZZA_CRUST': 'thin'})
    assert json.loads(body) == {'PIZZA_CRUST': 'thin'}

def test_link_call(schema, session):
    # This doesn't mock out the *entire* app response, which means if we ever
    # start doing any sort of validation/coercion based on schema, this'll start
    # failing.
    session.requests_mock.register_uri(
        'GET', 'https://api.heroku.com/apps',
        json=[{'name': 'my-cool-app', 'stack': 'cedar'},
              {'name': 'my-uncool-app', 'stack': 'bamboo'}]
    )

    service = Service(schema, session)
    app_list = service.app.list()
    assert type(app_list) == list
    assert len(app_list) == 2
    assert app_list[0].__class__.__name__ == 'App'
    assert app_list[0].name == 'my-cool-app'
    assert app_list[1].stack == 'bamboo'

def test_link_response_patternProperties(schema, session):
    session.requests_mock.register_uri(
        'GET', 'https://api.heroku.com/apps/my-app/config-vars',
        json={'PIZZA_CRUST': 'thick', 'PIZZA_TOPPINGS': 'sausage,onions'}
    )

    service = Service(schema, session)
    config = service.config_var.info('my-app')
    assert config['PIZZA_CRUST'] == 'thick'

def test_link_pagination(schema, session):
    def response_callback(request, context):
        assert request.method == 'GET'
        context.status_code = 206
        context.headers['content-type'] = 'application/json'

        FAKE_RANGE = ']fake..'
        if 'Range' in request.headers:
            assert request.headers['Range'] == FAKE_RANGE
            return [{'name': 'app3'}, {'name': 'app4'}]
        else:
            context.headers['next-range'] = FAKE_RANGE
            return [{'name': 'app1'}, {'name': 'app2'}]

    session.requests_mock.register_uri(
        'GET', 'https://api.heroku.com/apps',
        json = response_callback
    )

    service = Service(schema, session)
    apps = service.app.list()
    assert [a.name for a in apps] == ['app1', 'app2', 'app3', 'app4']
