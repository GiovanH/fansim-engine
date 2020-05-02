import logging
from sys import argv
import shutil
import os


def makeLogHandler(base, level, format_string):
    h = base
    h.setLevel(level)  
    h.setFormatter(logging.Formatter(format_string, "%Y-%m-%d %H:%M:%S"))
    return h


active_log_handlers = {}


def getLogger(__name, stream=True, file=True, debug=True):
    global active_log_handlers
    
    logger = logging.getLogger(__name)
    logger.setLevel(logging.DEBUG)

    filepath_normal = f"{argv[0].replace('.py', '')}_latest.log"
    filepath_debug = f"{argv[0].replace('.py', '')}_latest_debug.log"

    if stream:
        if not active_log_handlers.get("stream"):
            active_log_handlers["stream"] = makeLogHandler(logging.StreamHandler(), logging.INFO, '[%(name)s] %(levelname)s: %(message)s')
        logger.addHandler(active_log_handlers["stream"])
    
    if file:
        if not active_log_handlers.get("file"):
            if os.path.isfile(filepath_normal):
                shutil.move(filepath_normal, filepath_normal + ".bak")
            active_log_handlers["file"] = makeLogHandler(logging.FileHandler(filepath_normal, mode="w"), logging.INFO, '%(asctime)s [%(name)s] %(levelname)s: %(message)s')
        logger.addHandler(active_log_handlers["file"])

    if debug:
        if not active_log_handlers.get("file_debug"):
            if os.path.isfile(filepath_debug):
                shutil.move(filepath_debug, filepath_debug + ".bak")
            active_log_handlers["file_debug"] = makeLogHandler(logging.FileHandler(filepath_debug, mode="w", encoding="utf-8"), logging.DEBUG, '%(asctime)s [%(name)s] %(levelname)s: %(message)s')
        logger.addHandler(active_log_handlers["file_debug"])

    return logger

if __name__ == "__main__":
    logger = getLogger(__name__)
    logger.info("Hello")