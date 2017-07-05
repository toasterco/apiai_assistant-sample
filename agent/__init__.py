from common import constants
from apiaiassistant import Assistant


assistant = Assistant(
    corpus='corpora/animal_wiki_corpus.json',
    magic_key=constants.MAGIC_KEY
)

from actions import *  # NOQA
