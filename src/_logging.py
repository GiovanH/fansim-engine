import logging


def makeLogHandler(base, level, format_string):
    h = base
    h.setLevel(level)  
    h.setFormatter(logging.Formatter(format_string))
    return h


handlers = {}


def getLogger(__name):
    global handlers
    
    logger = logging.getLogger(__name)
    logger.setLevel(logging.DEBUG)

    if not handlers.get("stream"):
        handlers["stream"] = makeLogHandler(logging.StreamHandler(), logging.INFO, '[%(name)s] %(levelname)s: %(message)s')
    logger.addHandler(handlers["stream"])
    
    if not handlers.get("file"):
        handlers["file"] = makeLogHandler(logging.FileHandler("latest.log", mode="w"), logging.INFO, '%(asctime)s [%(name)s] %(levelname)s: %(message)s')
    logger.addHandler(handlers["file"])

    if not handlers.get("file_debug"):
        handlers["file_debug"] = makeLogHandler(logging.FileHandler("latest_debug.log", mode="w"), logging.DEBUG, '%(asctime)s [%(name)s] %(levelname)s: %(message)s')
    logger.addHandler(handlers["file_debug"])

    return logger
