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
import caesarc
import cgi
page_header="""
<!DOCTYPE html>
<html>
    <head>
        <title>
        ROT13 encryption!
        </title>
    </head>
    <body>
        <h1>The ROT13 encryption!</h1>

"""
page_footer="""
</body>

</html>

"""
def build_page(page_content):
    edit_header="""
        <h1>Enter a number and word to encrypt below!</h1>

    """
    textarea="<textarea name='word'>"+page_content+"</textarea>"
    message_label="<label> Enter message to encrypt</label>"
    rot_label="<label> Rotate by: </label>"
    rotation_input="<input type='number' name='rotation'/>"

    submit= "<p><input type='submit' value='Encrypt It'!/></p>"

    encrypt_form= "<form method= 'post'>" +rot_label + rotation_input +"<br>"+message_label+ textarea + "<br>" +submit + "</form>"

    content=page_header+edit_header+encrypt_form+page_footer
    return(content)



class Index(webapp2.RequestHandler):
    def get(self):
        content=build_page("")
        self.response.write(content)


    def post(self):
        new_encryption=self.request.get("word")
        rotation=int(self.request.get('rotation'))
        new_encrypt_element=caesarc.encrypt(new_encryption,rotation)
        escaped_message=cgi.escape(new_encrypt_element)

        content= build_page(escaped_message)

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
