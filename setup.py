#! /usr/bin/env python
#! -*- coding: utf-8 *-*-

from setuptools import setup, find_packages

readme = open('README.md', 'r').read()
setup(
    name='gists.cli.py3',
    version='0.351',
    url='https://github.com/RPing/gists.cli',
    license='GPLv2',
    author='rping',
    author_email='g1222888@gmail.com',
    description='A CLI to create, edit, view and list your GitHub Gists, forked from https://github.com/jiahut/gists.cli',
    include_package_data=True,
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests','texttable'],
    entry_points={
        'console_scripts': [
            'gists = gists_cli.gists:main',
        ]
    },
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    )
