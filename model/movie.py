from google.appengine.ext import ndb
from model.enum import Enum

class Movie(ndb.Model):

    Genre = Enum([
        "Accion",
        "Aventuras",
        "Comedia",
        "Drama",
        "Terror",
        "Musical",
        "Ciencia ficcion",
        "Guerra o belica",
        "Del oeste",
        "Crimen",
        "Dibujos animados"
    ], start=0, default=0)
    title = ndb.StringProperty(indexed=True, required=True)
    director = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(required=True)
    synopsis = ndb.StringProperty(required=True)
    year = ndb.IntegerProperty(required=True)


def all_movies():
    return Movie.query()

def get_movie(title):
    return Movie.query(Movie.title == title).get()


def create(mov,genre):

    movie = Movie()
    movie.title = mov.title
    movie.director = mov.director
    movie.genre = Movie.Genre.values[genre]
    movie.synopsis = mov.synopsis
    movie.year = mov.year

    return movie


def create_empty_movie():
    movie = Movie()
    movie.title = ""
    movie.director = ""
    movie.genre = ""
    movie.synopsis = ""
    movie.year = 0

    return movie

@ndb.transactional
def update(movie):
    return movie.put()