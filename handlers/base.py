# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
"""
BaseAjaxHandler taken from Google's GAE Secure Scaffold
https://github.com/google/gae-secure-scaffold-python
"""

import json
import webapp2
import datetime

# This prefix is returned on GET requests to any Ajax-like handler.
# It is used to prevent JSON-like responses that may contain non-public
# information from being included in malicious domains, e.g. evil.com
# inserting a tag like: <script src="http://example.com/ajax/foo"></script>.
# evil.com cannot strip this prefix before parsing the result, unlike
# same-origin requests.  See https://google-gruyere.appspot.com/part3
# for more information.  It is not necessary for POST requests because
# there is no way to force the browser to make a cross-domain POST request
# and interpret the response as Javascript without use of other mechanisms
# like Cross-Origin-Resource-Sharing, which is disabled by default.
_XSSI_PREFIX = ')]}\',\n'


def json_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


class BaseAjaxHandler(webapp2.RequestHandler):
    """
    Base handler for servicing unauthenticated AJAX requests.

    Responses to GET requests will be prefixed by _XSSI_PREFIX.  Requests
    using other HTTP verbs will not include such a prefix.
    """

    def __init__(self, request, response):
        self.initialize(request, response)

    def _SetAjaxResponseHeaders(self):
        self.response.headers.update(
            {
                'Content-Disposition': 'attachment; filename=json',
                'Content-Type': 'application/json; charset=utf-8'
            })

    def dispatch(self):
        self._SetAjaxResponseHeaders()
        if self.request.method.lower() == 'get':
            self.response.out.write(_XSSI_PREFIX)
        super(BaseAjaxHandler, self).dispatch()

    def render_json(self, obj):
        self.response.out.write(json.dumps(obj, default=json_default))
