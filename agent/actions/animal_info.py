from apiaiassistant import widgets

from agent import assistant
from common import constants


def build_animal_card(info):
    read_more_button = widgets.Button(
        title='Read more',
        weblink=info.get('more_url'))

    image = widgets.Image(
        url=info.get('image_url'),
        alt=info.get('title'))

    return widgets.ImageCardWidget(
        text=info.get('text'),
        title=info.get('title'),
        image=image,
        button=read_more_button)


@assistant.intent('animal-info')
def animal_info(agent):
    animal = agent.parser.get('animal')

    if not animal:
        agent.ask('repeat-please')
        agent.suggest('animals')
        return

    animal = animal.lower()
    animal_info = constants.ANIMALS.get(animal)
    if not animal_info:
        agent.tell('animal-unknown', context={'animal': animal})
        return

    speech = animal_info.get('text')
    agent.tell_raw(speech, None)

    card = build_animal_card(animal_info)
    agent.show(card)
