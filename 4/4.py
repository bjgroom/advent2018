#! /usr/bin/python

import re

# Fetch data

myfile = open("input", 'r')
contents = list()
for line in myfile: contents.append(line.rstrip())
myfile.close()

# Create necessary data structures
guards = list()
hour = dict.fromkeys(range(0,60))
print hour

# Find Guard ID of sleepiest guard
for line in range(0, len(contents)):
    if re.search('Guard', contents[line]):
        print re.search(':\d\d]', contents[line]).group(0).lstrip(':').strip(']')
	

# Find this guard's sleepiest minute
