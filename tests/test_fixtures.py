"""
Tests for test fixtures. Such meta. Very testing. Wow.
"""

from .fixtures import session

def test_session_fixture(session):
    session.requests_mock.register_uri('GET', 'http://httpbin.org/status/418', status_code=200)
    resp = session.get('http://httpbin.org/status/418')

    # If the mocking is working right, then we get our fake 200 instead of
    # httpbin's real 418.
    assert resp.status_code == 200

    # Check that we can retrieve info about the last request.
    assert session.requests_mock.last_request.url == 'http://httpbin.org/status/418'
