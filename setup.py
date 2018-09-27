from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

def extract_version():
    version = None
    fnme = os.path.join(here, 'lib', 'env_scanner', '__init__.py')
    with open(fnme) as fd:
        for line in fd:
            if (line.startswith('__version__')):
                _, version = line.split('=')
                version = version.strip()[1:-1]  # Remove quotation characters
                break
    return version

pypi_name = 'scitools-iris'

with open(os.path.join(here, 'README.md'), 'r') as fh:
    long_description = ''.join(fh.readlines())

setup(
    name='env_scanner',  # Required
    version=extract_version(),  # Required
    description='A command-line tool for searching through local Scientific '
                'Software Stack installations',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/boss-corinne/env_scanner',  # Optional
    author='UK Met Office',  # Optional
    author_email='corinne.bosley@metoffice.gov.uk',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # # install_requires=['argparse'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={
        'test': ['pytest', 'subprocess'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports and Issues':
            'https://github.com/boss-corinne/env_scanner/issues',
        'Source': 'https://github.com/boss-corinne/env_scanner',
    },
)
