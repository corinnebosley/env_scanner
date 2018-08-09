"""
This toy python script is a proof-of-concept of the Package Finder.

The purpose of this is to provide a command-line utility to allow users to
do two things:
1. Search for a package and see what environments contain it
2. List the contents of individual environments in a human-readable form

It should also be very easy to do a third thing, which is to search for an
environment containing a specific version of a package i.e. iris 2.0
"""
import argparse
import os
import glob

ROOT = '/opt/scitools/environments'


def pkg_list(env):
    """
    Compile dictionary of package names and versions in specified environment.

    :param env: environment descriptor-label (i.e. default-next) to scan.
    :return: dictionary of package names and versions.
    """
    package_list = os.listdir(os.path.join(env, 'conda-meta'))

    # Make the list human-readable by splitting each package name up into useful
    # components (package name, version number, and remove the '.json')
    pkg_dict = {}
    for pkg in package_list:
        parts_of_name = pkg[:-5].split('-')[:-2]
        name = ''.join(parts_of_name)
        version = pkg[:-5].split('-')[-2]
        pkg_dict[name] = [version]
    return pkg_dict


def list_envs(immutables=False):
    """
    Compile list of environments available at runtime
    from /opt/scitools/environments

    :return: list of environment names
    """
    all_the_envs = []
    descriptors = glob.glob(ROOT + '/*')

    # Compile list of all environments currently available:
    for desc in descriptors:
        desc_labels = glob.glob(desc + '/*')
        for label in desc_labels:
            # Get list of absolutely all environment names
            all_the_envs.append(os.path.join(desc, label))

            # Use full list if immutables are included
            if immutables:
                available_envs = all_the_envs
            else:
                # Immutable environments have a date label as their directory
                # name, so if the last part of the environment name starts with
                # '20', do not include it in the search list.
                available_envs = []
                for env in all_the_envs:
                    if not env.split('/')[-1].startswith('20'):
                        available_envs.append(env)

    return available_envs


def list_content(environment):
    """
    Print names and versions of all packages available in the user-specified
    environment.

    :param desc: environment descriptor (i.e. default).
    :param label: label adjoining descriptor (i.e. current) (optional).
    :param immutables: boolean representing whether to include immutable
    environments in the list of those available.
    """
    desc = environment.split('-')[0]
    label = environment.split('-')[1]
    env = os.path.join(ROOT, desc, label)

    # Gather and print out list of packages in specified environment:
    packages = pkg_list(env)
    print('Contents of {} environment:\n'.format(env))
    for key in packages.keys():
        pkg = key
        vsn = packages[key][0]
        print(pkg + '   ' + vsn)


def find_pkg(package=None, version=None, immutables=False):
    """
    Print out a list of available environments, or those which contain the
    user-specified package.

    :param package: Name of package to search for.
    :param version: version of specified package to search for.
    """
    # Prepare some lists for later use:
    pkg_match = []
    pkg_version_match = []
    all_envs = list_envs(immutables)

    # Search each available environment to find any matches with the
    # specified package
    # TODO investigate filter function or other matching function
    if package:
        for env in all_envs:
            pkg_dict = pkg_list(env)
            if package in pkg_dict:
                pkg_match.append(env)
                # Search for matching name AND version, add to separate list.
                if version and pkg_dict[package][0][:len(version)] == \
                        [version][0]:
                    pkg_version_match.append(env)

    # Print names of all environments, or those containing user's requirement.
    if package:
        if version:
            print("Package {} version {} is available in the following "
                  "environment(s): \n".format(package, version))
            for env in pkg_version_match:
                print(env)
        else:
            print("Package {} is available in the following "
                  "environment(s): ".format(package))
            for env in pkg_match:
                print(env)
    else:
        print("The following environments are available for use on this "
              "machine:")
        for env in all_envs:
            print(env)


def main():
    parser = argparse.ArgumentParser()
    list_content = parser.add_argument_group(title="Listing environment "
                                                   "contents")
    list_content.add_argument("list_content",
                              help="List names and version numbers of all "
                                   "packages in specified environment.")
    list_content.add_argument("-env", "--environment",
                              help="Name for environment(s) to list contents "
                                   "of, i.e. 'default-next', "
                                   "'experimental_legacy-current', etc.")

    list_envs = parser.add_argument_group(title="Listing available "
                                                "environment names")
    list_envs.add_argument("list_envs",
                           help="List all available Scientific Software Stack "
                                "environments, or use optional arguments to "
                                "list environments containing specific "
                                "packages.")

    list_envs.add_argument("-p", "--package", dest="package",
                           help="Only list environments containing the "
                                "specified package")
    list_envs.add_argument("-v", "--version",
                           help="Only list environments containing the "
                                "matching version of specified package (must "
                                "be used in conjunction with '--package'")
    list_envs.add_argument("-i", "--immutables", default=False,
                           action="store_true",
                           help="Extend search to include immutable "
                                "environments")

    args = parser.parse_args()
    if args.list_envs:
        find_pkg(args.package, args.version, args.immutables)
    elif args.list_content:
        list_content(args.environment)
    else:
        print("I'm afraid there has been a problem, please "
              "use 'python env_browser.py --help' to check the arguments you "
              "have given me.")


if __name__ == '__main__':
    main()
