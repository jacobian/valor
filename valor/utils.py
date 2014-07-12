def is_ref(prop):
    """
    Returns True if prop is a reference.
    """
    return list(prop.keys()) == ['$ref']
