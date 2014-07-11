from .link import Link
from .utils import is_ref

class Resource(object):
    def __init__(self, schema, session, resource_name):
        self._links = {}
        self._name = resource_name
        self._defn = schema['properties'][resource_name]
        if is_ref(self._defn):
            self._defn = schema.resolve_ref(self._defn['$ref'])

        root_url = next(l['href'] for l in schema['links'] if l['rel'] == 'self')
        for link in self._defn['links']:
            url = root_url + link['href']
            self._links[link['rel']] = Link(schema, session, url, link)

    def __getattr__(self, attr):
        try:
            return self._links[attr]
        except KeyError:
            raise AttributeError(attr)

    def __dir__(self):
        return self._links.keys()
