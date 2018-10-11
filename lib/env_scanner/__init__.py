"""
# env scanner

A command-line tool used to search the Scientific Software Stack

Currently a WIP.  Structure needs some work.

You can:

    List all environments available to you on the machine you are working from:
    `$ python env_scanner.py --list_envs`

    List all environments containing a specific package
    `$ python env_scanner.py --list_envs -p iris`

    List environments containing a specific package at a specific version
    (as precise as you like; the scanner will match the version number to the
    same length as the input value)
    `$ python env_scanner.py --list_envs -p iris -v 2`

    List the entire contents of a single specified environment.
    `$ python env_scanner.py --list_content -env default-next`

You can also add the flag `-i` to include immutable environments in your search.

This is also runnable as a shell script, using `env_browser.sh` instead of `python env_scanner.py`; for example:

    `$ env_browser.sh --list_envs`

"""
from six.moves import (filter, input, map, range, zip)  # noqa
import six

__version__ = '0.0.1dev0'
