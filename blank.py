#! /usr/bin/python

import re

# Fetch data

myfile = open("input", 'r')
contents = list()
for line in myfile: contents.append(line.rstrip())
myfile.close()

