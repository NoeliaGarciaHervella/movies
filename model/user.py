from google.appengine.ext import ndb

class User(ndb.Model):
    id = ndb.IntegerProerty(auto_now_add=True, indexed=True)
    nick = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=True)