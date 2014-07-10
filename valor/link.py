import re
import json

PARAMETER_REGEX = re.compile(r'\{\([%\/a-zA-Z0-9_-]*\)\}')

class Link(object):

    def __init__(self, session, url, link_schema):
        self._session = session
        self._url = url
        self._link = link_schema
        self._name = link_schema['rel']

    def __call__(self, *args, **kwargs):
        response = self._session.request(
            method = self._link['method'],
            url = self.interpolate_args(args),
            data = self.construct_body(kwargs)
        )

        # Clearly more work is needed here...
        return response.json()

    def interpolate_args(self, args):
        """
        Interpolate arguments into the link's URL.
        """
        # This doesn't really validate the definition refs embedded in the URL
        # patterns, but in practice that doesn't seem to matter much.
        num_expected_args = len(PARAMETER_REGEX.findall(self._url))
        if num_expected_args != len(args):
            raise TypeError("%s() takes exactly %s arguments (%s given)" % (self._name, num_expected_args, len(args)))

        # I can't figure out how to get the match number in a re.sub() callback,
        # so sub one at a time. This feels inelegant, but I can't find a better
        # option, so (shrug).
        url = self._url
        for i, arg in enumerate(args):
            url = PARAMETER_REGEX.sub(format_path_parameter(arg), url, count=1)

        return url

    def construct_body(self, kwargs):
        """
        Construct a request body based on given arguments.
        """
        # This does do some light validation on the *keys* of the body params,
        # but doesn't validate the contents of the body. I'm not sure if this
        # will prove to matter in practice or not.
        if 'schema' not in self._link:
            if kwargs:
                raise TypeError("%s() got unexpected keyword arguments: %s" % (self._name, kwargs.keys()))
            return None

        # FIXME: doesn't handle patternProperties
        given_keys = set(kwargs.keys())
        possible_keys = set(self._link['schema']['properties'].keys())
        required_keys = set(self._link['schema'].get('required', []))

        if required_keys - given_keys:
            raise TypeError("%s() missing required arguments: %s")

        if given_keys - possible_keys:
            raise TypeError("%s() got unepected keyword arguments: %s" % (self._name, list(given_keys - possible_keys)))

        # Is that really all?
        return json.dumps(kwargs)

def format_path_parameter(val):
    """
    Format a path paramater.

    Basically: convert to string, with a special rule for datetime objects.
    """
    # Blah this shouldn't be str(), it should be unicode, but path encoding
    # confuses me to much to worry about right now.
    return val.strftime('%Y-%m-%dT%H:%M:%SZ') if hasattr(val, 'strftime') else str(val)
