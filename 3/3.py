#! /usr/bin/python

import re

# Fetch data

myfile = open("input", 'r')
contents = list()
for line in myfile: contents.append(line.rstrip())
myfile.close()

# Build master grid

fabric = [0 for x in range(0,1000), 0 for y in range(0,1000)]

# Populate fabric with planned cuts

for x in range(0, len(contents)):
    print contents[x]
