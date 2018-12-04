#/usr/bin/python

from collections import Counter

myfile = open('input2', 'r')
boxes = myfile.read().strip().splitlines()
myfile.close()

two = 0
three = 0

for box in boxes:
	chars = [count for box, count in Counter(box).most_common()]
	if 3 in chars:
		three += 1
	if 2 in chars:
		two += 1

print two * three

for i in boxes:
        for j in boxes:
            diffs = 0
            for idx, ch in enumerate(i):
                if ch != j[idx]:
                    diffs += 1
            if diffs == 1:
                ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
                print("Part Two:", ''.join(ans))

