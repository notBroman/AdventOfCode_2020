# notBroman

import fileinput
import re

lines = list(fileinput.input())
t0 = int(lines[0])
B1 = [int(x) for x in lines[1].strip().split(',') if x != 'x']
best = None
for b in B1:
    t=t0
    while t%b != 0:
        t += 1
    waitTime = t-t0
    if best is None or waitTime < best[0]:
        best = (waitTime, b)

print(best[0]*best[1])

# to solve part 2 use chinese remainder theorem
