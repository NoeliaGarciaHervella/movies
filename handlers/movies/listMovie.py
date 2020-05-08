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
from webapp2_extras.users import users
from webapp2_extras import jinja2
import model.user as user_mgt
import model.movie as movie_mgt

class MoviesHandler(webapp2.RequestHandler):
    def get(self):


        usr = users.get_current_user()
        user = user_mgt.retrieve(usr)

        if usr and user:
            url_usr = users.create_logout_url("/")

            movies = movie_mgt.all_movies()

            valores_plantilla = {
                "movies": movies,
                "usr": usr,
                "user":user,
                "url_usr": url_usr
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("list_movies.html", **valores_plantilla))
        else:
            return self.redirect("/")






app = webapp2.WSGIApplication([
    ('/movies', MoviesHandler)
], debug=True)
