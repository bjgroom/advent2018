#! /usr/bin/python

import re
from itertools import product
# Fetch data

myfile = open("input", 'r')
contents = list()
for line in myfile: contents.append(line.rstrip())
myfile.close()

# Build master grid

fabric = [0 for x in range(0,1000), 0 for y in range(0,1000)]

# Populate fabric with planned cuts

for x in range(0, len(contents)):

    # Put dimensions in variables

    nums = re.split('(\d+)', contents[x], maxsplit=5)
    xmax = int(nums[3]) + int(nums[7])
    xmin = int(nums[3])
    ymax = int(nums[5]) + int(nums[9])
    ymin = int(nums[5])

    # Mark dimensions on fabric

    	
