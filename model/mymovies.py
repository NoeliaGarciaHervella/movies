from google.appengine.ext import ndb


class Mymovies(ndb.Model):
    movie = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)

def get_mymovie_user(keyMovie,user):
    return Mymovies.query(Mymovies.movie == keyMovie and Mymovies.user == user).get()

def get_mymovies(user):
    return Mymovies.query(Mymovies.user == user).order()


def create(mov):

    movie = Mymovies()
    movie.movie = mov.movie
    movie.user = mov.user

    return movie


def create_empty_movie():

    movie = Mymovies()
    movie.movie = ""
    movie.user = ""

    return movie

def create_query_delete_one(movie):
    return movie.key.delete()



@ndb.transactional
def update(movie):
    return movie.put()

