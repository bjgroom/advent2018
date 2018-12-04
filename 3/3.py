#! /usr/bin/python

import re
from itertools import product
# Fetch data

myfile = open("input", 'r')
contents = list()
for line in myfile: contents.append(line.rstrip())
myfile.close()

# Build master grid in 2D list

fabric = []
for x in range(0,1000):
    fabric.append([])
    for y in range(0,1000):
	fabric[x].append(0)

# Populate fabric with planned cuts

for x in range(0, len(contents)):

    # Put dimensions in variables

    nums = re.split('(\d+)', contents[x], maxsplit=5)
    xmax = int(nums[3]) + int(nums[7])
    xmin = int(nums[3])
    ymax = int(nums[5]) + int(nums[9])
    ymin = int(nums[5])

    # Mark dimensions on fabric

    for v in range(ymin, ymax):
	for h in range(xmin, xmax):
	    fabric[h][v] += 1

# TASK 3.1 ## Scan and count fabric for collisions (spaces with > 1 claim)

bang = 0

for v in range(0, 1000):
    for h in range(0, 1000):
	if fabric[h][v] > 1:
	    bang += 1
print bang

# TASK 3.2 ## Re-scan fabric claim-by-claim to find ID with 0 collisions


for x in range(0, len(contents)):

    # Put dimensions in variables

    nums = re.split('(\d+)', contents[x], maxsplit=5)
    xmax = int(nums[3]) + int(nums[7])
    xmin = int(nums[3])
    ymax = int(nums[5]) + int(nums[9])
    ymin = int(nums[5])

    # Mark dimensions on fabric

    flag = False

    for v in range(ymin, ymax):
	for h in range(xmin, xmax):
	    if fabric[h][v] > 1:
		flag = True

    if flag == False:
	print nums[1]
	break

