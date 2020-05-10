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

from webapp2_extras import jinja2
from webapp2_extras.users import users
import model.user as usr_mgt
import model.comment as comment_mgt
import time


class AddCommentHandler(webapp2.RequestHandler):

    def post(self):
        usr = users.get_current_user()
        user = usr_mgt.retrieve(usr)

        if usr and user:
            keyMovie = self.request.GET["idMovie"]
            content = self.request.get("commentMovie")
            comment = comment_mgt.create_empty_comment()
            comment.content = content
            comment.movie =  keyMovie
            comment.user = user.email

            final_comment = comment_mgt.create(comment)
            comment_mgt.update(final_comment)
            time.sleep(1)
            return self.redirect("/showMovie/"+keyMovie)

        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/addComment', AddCommentHandler)
], debug=True)
