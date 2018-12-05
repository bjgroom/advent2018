#! /usr/bin/python

import re

# Fetch data

myfile = open("input", 'r')
contents = list()
for line in myfile: contents.append(line.rstrip())
myfile.close()

# Create necessary data structures
guards = list()

# Find Guard ID of sleepiest guard
for line in range(0, len(contents)):
    if re.search('Guard', contents[line]):
	guards.append([re.search('#\d+', contents[line]).group(0)], [re.search]) # FIXME don't care when the guard starts - only search for sleep and wake to build log of sleep time

for line in range(0,len(guards)):
	print guards[line]

# Find this guard's sleepiest minute
