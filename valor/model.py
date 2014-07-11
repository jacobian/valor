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
