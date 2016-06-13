#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hello

Usage:
  main.py <configuration_file> get <path> <name> 
  main.py <configuration_file> set <path> <name> <value>

Options:
  -h --help     Show this screen.
"""
import configparser
from docopt import docopt
arguments = docopt(__doc__)
file_path = arguments['<configuration_file>']
path = arguments['<path>']
name = arguments['<name>']
value = arguments['<value>']
config = configparser.ConfigParser()
config.read(file_path)

if arguments['get']:
    print(config[path][name])
elif arguments['set']:
    config[path][name] = value
    with open(file_path, 'w') as configfile:
        config.write(configfile)
