from agent import assistant


@assistant.intent('start')
def start(agent):
    agent.ask('start')
    agent.suggest('animals')
