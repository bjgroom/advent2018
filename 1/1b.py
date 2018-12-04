#!/usr/bin/python

import itertools

freq_chg = [int(x) for x in open("input1", 'r').readlines()]

freq_cur = 0
freq_hist = {0}
for freq in itertools.cycle(freq_chg):
    freq_cur += freq
    if freq_cur in freq_hist:
        print "Found it: " + str(freq_cur); break
    freq_hist.add(freq_cur)

