from webapp2_extras.routes import RedirectRoute as Route

from handlers import AssistantWebhook


def prepare(pairs):
    for pair in pairs:
        for name, route in pair[1].iteritems():
            route.name = pair[0] + '.' + name
            route.strict_slash = True


public = {
    'webhook.assistant': Route(
        r'/webhooks/assistant',
        AssistantWebhook)
}

cron = {}

api = {}

manage = {}

prepare([('manage', manage), ('api', api), ('cron', cron), ('public', public)])
