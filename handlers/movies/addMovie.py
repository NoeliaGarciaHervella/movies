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




class AddMovieHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()
        user = usr_mgt.retrieve(usr)

        if usr and user:
            url_usr = users.create_logout_url("/")

            valores_plantilla = {
                "usr": usr,
                "url_usr": url_usr
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("add_movie.html", **valores_plantilla))
        else:
            return self.redirect("/")


    def post(self):
        usr = users.get_current_user()
        user = usr_mgt.retrieve(usr)

        if usr and user:
            title = self.request.get("title")
            exit_movie = movie_mgt.get_movie(title)

            if exit_movie is None:


                movie = movie_mgt.create_empty_movie()
                movie.title = self.request.get("title").strip()
                movie.director = self.request.get("director").strip()
                genre = self.request.get("genre").strip()
                movie.synopsis = self.request.get("synopsis").strip()
                year = self.request.get("year").strip()
                image_file = self.request.get("noe", None)
                movie.image_bin = images.resize(image_file,300,300)

                try:
                    movie.year = int(year)
                    genre = int(genre)
                except ValueError:
                    movie.year = 0

                final_movie = movie_mgt.create(movie,genre)

                final_movie = movie_mgt.update(final_movie)
                time.sleep(2)
                self.response.write(final_movie.get().key.urlsafe())

                mymovie = mymovie_mgt.create_empty_movie()
                mymovie.movie = final_movie.get().key.urlsafe()
                mymovie.user = user.email
                final_mymovie = mymovie_mgt.create(mymovie)
                mymovie_mgt.update(final_mymovie)
                time.sleep(2)

                return self.redirect("/movies")
            else:
                message = "Ya existe una pelicula con ese nombre debes crear otra pelicula o buscar la que desees"
                self.redirect("/error?message="+message)


        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/addMovie', AddMovieHandler)
], debug=True)
