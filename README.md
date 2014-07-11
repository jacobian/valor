# Valor

Python HTTP clients for APIs represented by JSON Schema.

**This is still super-early days yet, many things probably don't work. Use at your own risk.**

Among most other things, docs aren't done, but check this out:

```bash
$ heroku auth:whoami
jacob@heroku.com
$ heroku apps
ancient-thicket-4976
arcane-reef-4005
...

$ python -i heroku.py
>>> heroku.account.self().email
u'jacob@heroku.com'
>>> [app.name for app in heroku.app.instances()]
[u'ancient-thicket-4976', u'arcane-reef-4005', ...]
```

![](http://img4.wikia.nocookie.net/__cb20130412040940/cso/images/1/19/Notbad.jpg)
