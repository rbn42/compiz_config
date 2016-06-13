#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hello

Usage:
  main.py <configuration_file> get <path> <name>
  main.py <configuration_file> set <path> <name> <value>
  main.py <configuration_file> submit

Options:
  -h --help     Show this screen.
"""
import configparser
import shutil
import os.path
from docopt import docopt
arguments = docopt(__doc__)
file_path = arguments['<configuration_file>']
beforesubmit = file_path + '.beforesubmit'
path = arguments['<path>']
name = arguments['<name>']
value = arguments['<value>']
config = configparser.ConfigParser()

if os.path.exists(beforesubmit):
    config.read(beforesubmit)
else:
    config.read(file_path)

if arguments['get']:
    print(config[path][name])

elif arguments['set']:
    config[path][name] = value
    with open(beforesubmit, 'w') as configfile:
        config.write(configfile)

elif arguments['submit']:
    if os.path.exists(beforesubmit):
        os.system('cat %s > %s; rm %s;' %
                  (beforesubmit, file_path, beforesubmit))
        #shutil.move(beforesubmit, file_path)
