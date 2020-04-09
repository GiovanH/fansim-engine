import logging
from sys import argv


def getLogger(__name):
    logger = logging.getLogger(__name)

    loghandler_file = logging.FileHandler(" ".join([argv[0], __name, "latest.log"]))
    loghandler_file.setLevel(logging.DEBUG)
    loghandler_file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(loghandler_file)

    return logger
