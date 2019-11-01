# File handling


def easySlug(string, repl="-", directory=False):
    import re
    if directory:
        return re.sub("^\.|\.+$", "", easySlug(string, directory=False))
    else:
        return re.sub("[\\\\/:*?\"<>\|]|\ $", repl, string)


def userProfile(subdir=""):
    import os
    user_profile = os.environ.get("userprofile") or os.path.expanduser("~")
    return os.path.join(user_profile, subdir)


def renameFileOnly(source, destination, clobber=False, quiet=False, preserve_extension=True):
    """Renames file `source` to file `destination`.

    Args:
        source (str): Source path
        destination (str): Destination FILENAME
        clobber (bool, optional): Error instead of overwriting existing files.
        quiet (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    from os import path
    old_dir, old_name = path.split(source)
    new_dir, new_name = path.split(destination)

    assert (new_dir == "" or new_dir == old_dir), "Destination should not be a new path!"

    if preserve_extension:
        old_name_base, old_ext = path.splitext(old_name)
        new_name_base, new_ext = path.splitext(new_name)

        if not (new_ext == "" or new_ext == old_ext):
            print("WARNING: New name should not have a new extension while preserve_extension is True!")

        new_name = new_name_base + new_ext + old_ext

    real_destination = path.join(old_dir, new_name)
    return opFileToFile(shutil.move, source, real_destination, clobber, quiet)


def opFileToDir(op, source, destination, clobber, quiet):
    from os import path
    if not clobber:
        (srcdir, srcfile) = path.split(source)
        new_file_name = path.join(destination, srcfile)
        nfiles = [new_file_name]
    else:
        nfiles = []
    yfiles = [source]
    yfolders = [destination]
    _safetyChecks(yfiles=yfiles, yfolders=yfolders, nfiles=nfiles)
    return _doFileOp(op, source, destination, quiet)


def opFileToFile(op, source, destination, clobber, quiet):
    assert source != destination, "Paths are the same! " + source
    nfiles = [destination] if not clobber else []
    yfiles = [source]
    _safetyChecks(yfiles=yfiles, nfiles=nfiles)
    return _doFileOp(op, source, destination, quiet)


def opDirToParent(op, source, destination, clobber, quiet):
    _safetyChecks(yfolders=[source, destination])
    return _doFileOp(op, source, destination, quiet)


def opDirWithMerge(op, source, destination, clobber, quiet):
    nfolders = [destination] if not clobber else []
    _safetyChecks(yfolders=[source], nfolders=nfolders)
    return _doFileOp(op, source, destination, quiet)


def _safetyChecks(yfiles=[], yfolders=[], nfiles=[], nfolders=[]):
    from os import path
    for file in yfiles:
        if not path.isfile(file):
            raise FileNotFoundError(file)
    for folder in yfolders:
        if not path.isdir(folder):
            raise FileNotFoundError(folder)
    for file in nfiles:
        if path.isfile(file):
            raise FileExistsError(file)
    for folder in nfolders:
        if path.isdir(folder):
            raise FileExistsError(folder)


def _doFileOp(op, source, destination, quiet):
    try:
        result = op(source, destination)
        if not quiet:
            print("{} --> {}".format(source, destination))
        return result
    except Exception as e:
        if not quiet:
            print("{} -x> {}".format(source, destination))
        raise


def copyFileToDir(source, destination, clobber=False, quiet=False):
    """Copies file `source` to folder `destination`.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        print (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    return opFileToDir(shutil.copy2, source, destination, clobber, quiet)


def copyFileToFile(source, destination, clobber=False, quiet=False):
    """Copies file `source` to file `destination`.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        print (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    return opFileToFile(shutil.copy2, source, destination, clobber, quiet)


def copyDirToParent(source, destination, clobber=False, quiet=False):
    """Copies directory `source` to `destination`. `source` will become a subfolder of `destination`.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        print (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    return opDirToParent(shutil.copy2, source, destination, clobber, quiet)


def copyDirWithMerge(source, destination, clobber=False, quiet=False):
    """Copies directory `source` to `destination`. If `destination` is a directory, the two are merged.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        print (bool, optional): Print progress to screen

    Returns:
        list: Destination paths
    """
    from distutils.dir_util import copy_tree
    return opDirWithMerge(copy_tree, source, destination, clobber, quiet)


def _copyTreeAndRemove(source, destination):
    """Summary

    Args:
        source (TYPE): Description
        destination (TYPE): Description
    """
    from distutils.dir_util import copy_tree
    import os
    result = copy_tree(source, destination)
    os.unlink(source)
    return result


def moveFileToDir(source, destination, clobber=False, quiet=False):
    """Moves file `source` to folder `destination`.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        quiet (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    return opFileToDir(shutil.move, source, destination, clobber, quiet)


def moveFileToFile(source, destination, clobber=False, quiet=False):
    """Moves file `source` to file `destination`.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        quiet (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    return opFileToFile(shutil.move, source, destination, clobber, quiet)


def moveDirToParent(source, destination, clobber=False, quiet=False):
    """Moves directory `source` to `destination`. `source` will become a subfolder of `destination`.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        quiet (bool, optional): Print progress to screen

    Returns:
        str: Destination path
    """
    import shutil
    return opDirToParent(shutil.move, source, destination, clobber, quiet)


def moveDirWithMerge(source, destination, clobber=False, quiet=False):
    """Moves directory `source` to `destination`. If `destination` is a directory, the two are merged.

    Args:
        source (str): Source path
        destination (str): Destination path
        clobber (bool, optional): Error instead of overwriting existing files.
        quiet (bool, optional): Print progress to screen

    Returns:
        list: Destination paths
    """
    return opDirWithMerge(_copyTreeAndRemove, source, destination, clobber, quiet)

