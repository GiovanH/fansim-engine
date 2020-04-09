import os
import shutil

import _logging
logger = _logging.getLogger(__name__)


def isSameFile(source, target):
    from stat import ST_MTIME, ST_CTIME, ST_SIZE

    s1, s2 = os.stat(source), os.stat(target)

    if s1[ST_MTIME] != s2[ST_MTIME]:
        return False

    if s1[ST_SIZE] != s2[ST_SIZE]:
        return False

    if s1[ST_CTIME] != s2[ST_CTIME]:
        return False

    return True  # Hopefully!


def copyLazy(src, dst, **kwargs):
    if not (os.path.isfile(src) and os.path.isfile(dst) and isSameFile(src, dst)):
        logger.debug(f"{src} --> {dst}")
        try:
            return shutil.copy2(src, dst, **kwargs)
        except PermissionError:
            logger.error(f"{dst} in use!")
    # else:
    #     logger.debug(f"{src} === {dst}")


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
