import os
import shutil

import _logging
logger = _logging.getLogger(__name__)


def isSameFile(source, target):
    from stat import ST_MTIME
    mtime1 = os.stat(source)[ST_MTIME]
    mtime2 = os.stat(target)[ST_MTIME]

    return mtime1 == mtime2


def copyLazy(src, dst, **kwargs):
    if not (os.path.isfile(src) and os.path.isfile(dst) and isSameFile(src, dst)):
        logger.debug(f"{src} --> {dst}")
        return shutil.copy2(src, dst, **kwargs)


def copyTreeLazy(src, dst, **kwargs):
    # https://stackoverflow.com/questions/22588225/how-do-you-merge-two-directories-or-move-with-replace-from-the-windows-command
    '''
    Updates destenation root, overwrites existing files.
    :param src: Root folder from wehere to copy the files
    :param dst: Destination folder where new folders and files are created and new files are added
    :return: !=0 in case of errors
    '''
    logger.info(f"Patching '{src}' to '{dst}'")
    if not os.path.exists(src):
        return 1
    ok = 0
    for path, dirs, files in os.walk(src):
        relPath = os.path.relpath(path, src)
        destPath = os.path.join(dst, relPath)
        if not os.path.exists(destPath):
            os.makedirs(destPath)
        for file in files:
            destFile = os.path.join(destPath, file)
            srcFile = os.path.join(path, file)
            copyLazy(srcFile, destFile)  # performs copy&overwrite
    return ok
