# Roman Berger
# there is a pattern that repeats to the right
# it consists of open space '.' and trees '#'
# you can only move 1 to the right and 2 down
# mark the spaces you land on: 'O' -> open space , 'X' -> tree
# how many trees do you encounter

def read_data(fileName):
    
    f = open(fileName, 'r')
    data = f.read().splitlines()
    f.close()
    
    for i in range(len(data)):
        data[i] = list(data[i])
    return data
   
def mark_spaces(myList):
    spot = 0

    i = 0
    while(i < (len(myList))):
        if(spot > (len(myList[0])-1)):
            spot -= (len(myList[0]))
        else:
            pass

        if(myList[i][spot] == '.'):
            myList[i][spot] = 'O'
        elif(myList[i][spot] == '#'):
            myList[i][spot] = 'X'
        else:
            pass

        spot += 1
        i += 2

def count_trees(myList):
    count = 0

    for i in range(len(myList)):
        count += myList[i].count('X')
    return count

def display_data(myList):
    for i in range(len(myList)):
        print(myList[i],'\n')

def main_program():
    name = 'day3_input.txt'

    data = read_data(name)
    mark_spaces(data)
    display_data(data)
    result = count_trees(data)
    print(result)

main_program()
