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
import cgi
import datetime
import webapp2
import logging

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import urlfetch

import os
import jinja2
import urllib, hashlib
import json

TEMPLATEFOLDER = '_build/html/'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__).split('/')[:-1])),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)

def setTemplate(self, template_values, templateFile, _templateFolder=TEMPLATEFOLDER):
    # add Defaults
    template_values['_templateFolder'] = _templateFolder
    template_values['_year'] = str(datetime.datetime.now().year)
    path = os.path.normpath(_templateFolder+templateFile)
    template = JINJA_ENVIRONMENT.get_template(path)
    self.response.write(template.render(template_values))

class Images(webapp2.RequestHandler):
    def get(self):
        self.redirect('http://em.geosci.xyz'+self.request.path)

class MainPage(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {"indexPage":True}, 'index.html')

app = webapp2.WSGIApplication([
    ('/_images/.*', Images),
    ('/', MainPage),
], debug=True)

