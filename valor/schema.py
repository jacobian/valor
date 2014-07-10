import json
import jsonpointer

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
        if not ref.startswith('#'):
            raise ValueError("non-fragment references are not supported (got: %s)" % ref)
        return jsonpointer.resolve_pointer(self, ref.lstrip('#'))
