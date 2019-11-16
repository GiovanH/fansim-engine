# Streams

from contextlib import contextmanager


@contextmanager
def std_redirected(outfile, errfile=None, tee=False):
    """Summary

    Args:
        outfile (TYPE): Description
        errfile (None, optional): Description

    Yields:
        TYPE: Description
    """
    import sys  # Must import basename for naming to bind globally
    if errfile is None:
        errfile = outfile

    # Save file handle
    _stdout = sys.stdout
    _stderr = sys.stderr

    sys.stdout = open(outfile, 'w')
    sys.stderr = open(errfile, 'w') if outfile != errfile else sys.stdout

    if tee:
        sys.stdout = stream_tee(sys.stdout, _stdout)
        sys.stderr = stream_tee(sys.stderr, _stderr)

    try:
        yield None
    finally:
        sys.stdout.close()
        sys.stderr.close()  # Safe to use even if stdout == stderr
        sys.stdout = _stdout
        sys.stderr = _stderr


class stream_tee(object):
    # Based on https://gist.github.com/327585 by Anand Kunal
    def __init__(self, stream1, stream2):
        self.stream1 = stream1
        self.stream2 = stream2
        self.__missing_method_name = None  # Hack!

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        self.__missing_method_name = name  # Could also be a property
        return getattr(self, '__methodmissing__')

    def __methodmissing__(self, *args, **kwargs):
        # Emit method call to the log copy
        callable2 = getattr(self.stream2, self.__missing_method_name)
        callable2(*args, **kwargs)

        # Emit method call to stdout (stream 1)
        callable1 = getattr(self.stream1, self.__missing_method_name)
        return callable1(*args, **kwargs)
