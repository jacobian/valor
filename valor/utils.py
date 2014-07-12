import re

def is_ref(prop):
    """
    Returns True if prop is a reference.
    """
    return list(prop.keys()) == ['$ref']

def python_attr(name):
    """
    Convert `name` into something suitable for a Python attribute name.
    """
    return re.sub(r'[^\w]+', '_', name).lower()
