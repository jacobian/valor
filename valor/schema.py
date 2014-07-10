import json

class Schema(dict):
    """
    Lightweight encapsulation of a JSON Schema.
    """

    @classmethod
    def from_file(cls, path_or_stream):
        """
        Create a schema from a file name or stream.
        """
        if hasattr(path_or_stream, 'read'):
            return cls(json.load(path_or_stream))
        else:
            with open(path_or_stream) as fp:
                return cls(json.load(fp))

    def resolve_ref(self, ref):
        return Reference(ref).resolve(self)

class Reference(object):
    def __init__(self, ref):
        if not ref.startswith('#'):
            raise ValueError("non-fragment references are not supported (got: %s)" % ref)
        self.ref = ref

    def resolve(self, schema):
        # Very overly simplisitic - doesn't handle array indexes, etc. However,
        # works with Heroku's schema, so good enough for a prototype.
        node = schema
        for bit in self.ref.split('/')[1:]:
            node = node[bit]
        return node
