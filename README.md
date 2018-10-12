# env scanner

A command-line tool used to search the Scientific Software Stack

Currently a WIP.  Structure needs some work.

You can:

List all environments available to you on the machine you are working from:

    `$ env_scanner --list_envs`

List all environments containing a specific package

    `$ env_scanner --list_envs -p iris`

List environments containing a specific package at a specific version
(as precise as you like; the scanner will match the version number to the
same length as the input value)

    `$ env_scanner --list_envs -p iris -v 2`

    `$ env_scanner --list_envs -p iris -v 2.2.0`

List the entire contents of a single specified environment.

    `$ env_scanner --list_content -env scitools/default-next`

You can also add the flag `-i` to include immutable environments in your search.
