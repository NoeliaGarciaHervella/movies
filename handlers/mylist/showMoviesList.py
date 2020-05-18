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




class showMoviesListHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()
        user = usr_mgt.retrieve(usr)
        mov_list = False

        if usr and user:
            url_usr = users.create_logout_url("/")
            mymovies = mymovie_mgt.get_mymovies(user.email)
            movies = movie_mgt.all_movies()
            key_mymovie = list()

            if mymovies.count() > 0 :
                for mymovie in mymovies:
                    key_mymovie.append(mymovie.movie)

                mov_list =True
            valores_plantilla = {
                "movies": movies,
                "key_mymovie": key_mymovie,
                "mov_list": mov_list,
                "usr": usr,
                "user": user,
                "url_usr": url_usr
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("list_movies.html", **valores_plantilla))
        else:
            return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/showMoviesList', showMoviesListHandler)
], debug=True)
