def is_ref(prop):
    """
    Returns True if prop is a reference.
    """
    return prop.keys() == ['$ref']
