import json

import apiaiassistant

from handlers import base
from agent import assistant


class AssistantWebhook(base.BaseAjaxHandler):

    def apiai_error(self):
        self.render_json({'error': '400'})
        return

    def post(self):
        agent = assistant.process(
            json.loads(self.request.body),
            headers=self.request.headers
        )

        if agent.code != apiaiassistant.agent.Status.OK:
            return self.apiai_error()

        self.render_json(agent.response.to_dict())
