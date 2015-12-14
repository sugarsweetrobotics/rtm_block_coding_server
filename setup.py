from setuptools import setup
from distutils.command.install_data import install_data
from distutils.command.install import INSTALL_SCHEMES
import os
import sys
import subprocess


"""
Requirements
------------
* Python 2.7

Features
--------
* Repository and Package Management
* Semi-automated Build in Command Line
* Automatical Launch Configuration
* Automatic Launch, Configuration, Connection, and Activation of the RT-System


Setup
-----
::
pip install rtm_block_coding_server


History
-------
1.0.0b (2015-7-30)
~~~~~~~~~~~~~~~~~~
* first release

"""
version = '0.0.1'
packages = ['rtm_block_coding']
scripts = ['rtm_block_coding/bin/rbc_server.py']
cmdclasses = {}
#if sys.platform == 'win32':
#    scripts.append('wasanbon/bin/wasanbon-cd.bat')

setup(
    name = 'rtm_block_coding_server',
    version = version,
    url = 'http://ogata-lab.jp',
    author = 'ysuga',
    author_email = 'ysuga@ysuga.net',
    description = 'RTM Block Coding Server', 
    download_url = 'https://github.com/sugarsweetrobotics/rtm_block_coding_server.git',
    packages = packages,
    cmdclass = cmdclasses,
    data_files = [],
    scripts = scripts,
    license = 'GPLv3',
    install_requires = [
        'psutil', 
        'nevow',
        'twisted',
        ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Desktop Environment',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development',
   ],
)








