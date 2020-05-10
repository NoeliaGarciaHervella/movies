#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.api import images
import model.user as usr_mgt
import model.movie as movie_mgt
import model.mymovies as mymovie_mgt
import time




class AddMovieListHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()
        user = usr_mgt.retrieve(usr)

        if usr and user:
            url_usr = users.create_logout_url("/")
            idMovie= self.request.GET["idMovie"]

            mymovie = mymovie_mgt.get_mymovie_user(idMovie, user.email)

            if mymovie:
                mymovie_mgt.create_query_delete_one(mymovie)
                time.sleep(2)
                return self.redirect("/showMovie/" + idMovie)
            else:
                mymovie = mymovie_mgt.create_empty_movie()
                mymovie.movie = idMovie
                mymovie.user = user.email
                final_mymovie = mymovie_mgt.create(mymovie)
                mymovie_mgt.update(final_mymovie)
                time.sleep(2)

                return self.redirect("/showMovie/" + idMovie)
        else:
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/addMovieList', AddMovieListHandler)
], debug=True)
