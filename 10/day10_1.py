# notBroman
# count the differences between the elements of the list after it is sorted
# how many differences are 1, 2 and 3
# return the profuct of the amuont of differences that are 1 and 3

def get_jolts(fileName):
    with open(fileName, 'r') as f:
        data = f.read().split('\n')
        data.pop(len(data)-1)


    for i in range(len(data)):
        data[i] = int(data[i])

    return sorted(data)

def get_diffs(myList):
    diff1 = 1
    diff2 = 0
    diff3 = 1

    for i in range(1,len(myList)):
        diff = myList[i]-myList[i-1]
        if(diff == 1):
            diff1 += 1
        elif(diff == 2):
            diff2 += 1
        elif(diff == 3):
            diff3 += 1
    return {'diff1':diff1, 'diff2':diff2, 'diff3':diff3}

def main():
    test = 'test.txt'
    name = 'input_day10.txt'

    jolts = get_jolts(test)
    print(jolts)
    jolt_diff = get_diffs(jolts)
    print(jolt_diff)

main()
