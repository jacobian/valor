import requests
import netrc
import valor

session = requests.Session()
session.auth = ('', netrc.netrc().hosts['api.heroku.com'][2])
session.headers['Accept'] = "application/vnd.heroku+json; version=3"

schema = valor.Schema.from_file('tests/schema.json')
heroku = valor.Service(schema=schema, session=session)
