import requests
from .resource import Resource

class Service(object):
    def __init__(self, schema, session=None):
        self._schema = schema
        self._session = session or requests.Session()
        self._session.headers.setdefault('content-type', 'application/json')

    def __getattr__(self, attr):
        for a in (attr, attr.replace('_', '-')):
            if a in self._schema['properties']:
                return Resource(self._schema, self._session, a)
        raise AttributeError(a)

    def __dir__(self):
        return [a.replace('-', '_') for a in self._schema['properties']]
