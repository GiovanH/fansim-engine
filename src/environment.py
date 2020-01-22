import _logging
import os

logger = _logging.getLogger(__name__)


platform = os.name


def isWindows():
    return (platform == "nt")


def isPosix():
    return (platform == "posix")


def getGamedirRoot():
    if isWindows():
        gamedir_root = "C:/Program Files (x86)/Steam/steamapps/common/Homestuck Pesterquest"
    elif isPosix():
        # If you're on linux, change this path to your steam install directory.
        gamedir_root = os.environ["HOME"] + "/Library/Application Support" + "/Steam/steamapps/common/Homestuck Pesterquest"
    else:
        raise Exception("Unknown platform " + platform)
    return gamedir_root


def getExecutableName():
    if isWindows():
        executable = "pesterquest.exe"
    elif isPosix():
        executable = "pesterquest"
    else:
        raise Exception("Unknown platform " + platform)
    return executable
