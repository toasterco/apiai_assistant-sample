import json

from handlers import base
from agent import assistant


class AssistantWebhook(base.BaseAjaxHandler):

    def post(self):
        agent = assistant.process(
            json.loads(self.request.body),
            headers=self.request.headers
        )

        self.render_json(agent.response.to_dict())
