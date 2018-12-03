#! /usr/bin/python

import re

# Fetch data

myfile = open("input", 'r')
contents = myfile.readlines()
myfile.close()

# Cleanup data to give top-left corner, and dimensions, in a list of two-element lists. W x H

for x in range(0, len(contents)):
    contents[x] = (contents[x].split("@"))[1].rstrip().split(":")
    print contents[x]

# Build master grid

fabric = [0 for x in range(0,1000), 0 for y in range(0,1000)]

print fabric
    
