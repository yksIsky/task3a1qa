import string
import random
from Utility.logging import logger


def random_name():
    logger.info(f'generating new random string')
    string.ascii_letters
    return "".join([random.choice(string.ascii_letters) for i in range(7)])
