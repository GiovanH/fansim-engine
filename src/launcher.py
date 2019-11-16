from sys import version_info

try:
    assert version_info.major >= 3
    assert version_info.minor >= 6
except (AssertionError, AttributeError):
    print("Running python version", version_info)
    print("ERROR: This script requires Python 3.6 or newer.")
    print("Press enter to exit.")
    raw_input()
    exit()

from patcher import *  # never do this
from stream import std_redirected

with std_redirected("latest.log", tee=True):
    main()
