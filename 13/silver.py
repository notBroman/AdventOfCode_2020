# notBroman

import fileinput
import re
import string

def main():
    bus = list(fileinput.input())
    for i in range(len(bus)):
        bus[i] = bus[i].replace('\n','')
        bus[i] = bus[i].split(',')

    estimatedTime = int(bus[0][0])
    del bus[0]

    workingBus = []
    for i in range(1):
        for j in range(len(bus[i])):
            if bus[i][j].isnumeric():
                workingBus.append(int(bus[i][j]))

    busses = sorted(workingBus)
    diff = []
    for i in range(len(busses)):
        x = estimatedTime // busses[i]
        if x * busses[i] <= estimatedTime:
            x += 1
        x *= busses[i]
        d = x - estimatedTime
        diff.append(d)

    print(estimatedTime)
    print(busses)
    idx = diff.index(min(diff))
    answer = diff[idx]*busses[idx]
    print(answer)

main()
