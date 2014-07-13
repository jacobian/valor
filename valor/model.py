from .utils import is_ref

def model_factory(name, schema, model_schema):
    return type(name, (Model,), {'schema': schema, 'model': model_schema})

class Model(object):
    def __init__(self, **kwargs):
        self.__dict__['_dict'] = kwargs

    def __getattr__(self, attr):
        try:
            return self._dict[attr]
        except KeyError:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        self._dict[attr] = value

    def __repr__(self):
        identity = self.identity()
        if identity:
            return '<%s: %s>' % (self.__class__.__name__, identity)
        else:
            return object.__repr__(self)

    def __dir__(self):
        return self._dict.keys()

    def identity(self):
        """
        Return the "identity" of this object -- e.g. its ID, name, etc.

        This is used in URIs identifying the object (e.g. /app/the-app-name),
        and also for the model's __repr__ and such.

        Most models will have both an ID (UUID) identity *and* something more
        human-readable like a name, email, etc. If possible, try to use the
        thing-that's-not-an-ID, since the human-readbale names read better.
        """
        model_defs = self.__class__.model['definitions']

        # Look for multiple identity options
        if 'identity' in model_defs:
            if 'anyOf' in model_defs['identity']:
                idschemas = model_defs['identity']['anyOf']
            else:
                idschemas = [model_defs['identity']]
        else:
            idschemas = []

        # Poke through the identities, trying to find one we like. Identities
        # have to be refs -- because they point to other fields, and aren't
        # fields in their own right -- so we can just assume that the field name
        # is the last part of the ref. We're looking for something that's not
        # `id`, so build up a list of field names, shuffling anything that looks
        # like an ID to the back. We'll use the first item in this list once we
        # get through the loop.
        candidates = []
        for candidate in idschemas:
            # Skip anything that's not a ref. Hm. Is this OK?
            if not is_ref(candidate):
                continue

            field_name = candidate['$ref'].split('/')[-1]
            if field_name == 'id':
                candidates.append(field_name)
            else:
                candidates.insert(0, field_name)

        # If we don't have any candidates now, try and 'id' field as a
        # last-ditch effort.
        cfield = candidates[0] if candidates else 'id'
        return getattr(self, cfield, None)

