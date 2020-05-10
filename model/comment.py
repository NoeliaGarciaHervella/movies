from google.appengine.ext import ndb


class Comment(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    content = ndb.TextProperty(required=True)
    movie = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)

def get_comment_movie(keyMovie):
    return Comment.query(Comment.movie == keyMovie).order(Comment.added)


def create(comt):

    comment = Comment()
    comment.content = comt.content
    comment.movie = comt.movie
    comment.user = comt.user

    return comment


def create_empty_comment():

    comment = Comment()
    comment.content = ""
    comment.movie = ""
    comment.user = ""

    return comment


@ndb.transactional
def update(comment):
    return comment.put()