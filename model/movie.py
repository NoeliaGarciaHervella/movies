from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty(indexed=True)
    director = ndb.StringProperty(indexed=True)
    genre = ndb.StringProperty(indexed=True)
    synopsis = ndb.StringProperty(indexed=True)
    year = ndb.IntegerProperty(indexed=True)