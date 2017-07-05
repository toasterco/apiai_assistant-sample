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
Main application entry point, taken from Google's GAE Secure Scaffold
https://github.com/google/gae-secure-scaffold-python
"""

import webapp2
import routes

_UNAUTHENTICATED_ROUTES = routes.public.values()

_UNAUTHENTICATED_AJAX_ROUTES = routes.api.values()

_USER_ROUTES = routes.manage.values()
_AJAX_ROUTES = []

_ADMIN_ROUTES = []

_ADMIN_AJAX_ROUTES = []

_CRON_ROUTES = routes.cron.values()

_TASK_ROUTES = []

_CONFIG = {
    'webapp2_extras.i18n': {
        'default_locale': 'en_US'
    }
}

#################################
# DO NOT MODIFY BELOW THIS LINE #
#################################

app = webapp2.WSGIApplication(
    routes=(_UNAUTHENTICATED_ROUTES + _UNAUTHENTICATED_AJAX_ROUTES +
            _USER_ROUTES + _AJAX_ROUTES + _ADMIN_ROUTES + _ADMIN_AJAX_ROUTES +
            _CRON_ROUTES + _TASK_ROUTES),
    config=_CONFIG,
    debug=True)
