# notBroman
# count the differences between the elements of the list after it is sorted
# how many differences are 1, 2 and 3
# return the profuct of the amuont of differences that are 1 and 3

import fileinput

def get_jolts():
    data = list(fileinput.input())

    for i in range(len(data)):
        data[i] = data[i][:-1]
        data[i] = int(data[i])
    
    data.append(0)
    data.append(max(data)+3)
    return sorted(data)

def get_diffs(myList):
    n1 = 0
    n3 = 0
    for i in range(1,len(myList)):
        diff = myList[i]-myList[i-1]
        if(diff == 1):
            n1 += 1
        elif(diff == 3):
            n3 += 1
    return {'n1':n1, 'n3':n3}

DP = {}
def dp(i, myList):
    if i == len(myList)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(myList)):
        if myList[j]-myList[i] <= 3:
            ans += dp(j, myList)
    DP[i] = ans
    return ans

def main():
    jolts = get_jolts()
    jolt_diff = get_diffs(jolts)
    print(jolt_diff)

    print(dp(0, jolts))

main()
