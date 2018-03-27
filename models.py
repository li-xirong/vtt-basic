from __future__ import print_function

import logging
import random
from constant import ROOT_PATH

logger = logging.getLogger(__file__)
logging.basicConfig(
        format="[%(asctime)s - %(filename)s:line %(lineno)s] %(message)s",
        datefmt='%d %b %H:%M:%S')
logger.setLevel(logging.INFO)


class RandomGuess:
    def __init__(self, videoCollection, sentSet):
        logger.info(self.__class__.__name__)

    def score(self, video_id, sentence_id):
        return random.random()



NAME_TO_MODEL = {'random': RandomGuess}


def get_model(name):
    if name not in NAME_TO_MODEL:
        raise Exception('unsupported model')
    return NAME_TO_MODEL[name]


if __name__ == '__main__':
    scorer = get_model('random')(None, None)
    for video_id in range(2):
        for sent_id in range(3):
            print (video_id, sent_id, scorer.score(video_id, sent_id))

    
