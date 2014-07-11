# Valor

![](https://travis-ci.org/jacobian/valor.svg?branch=master)

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

Then see [heroku.py](https://github.com/jacobian/valor/blob/master/heroku.py) as an example of how this works.

![](http://img4.wikia.nocookie.net/__cb20130412040940/cso/images/1/19/Notbad.jpg)

----

<small>What's with the name? The Ruby version of the same thing is [Heroics](https://github.com/interagent/heroics). Heroics. Valor. See what I did there?</small>
