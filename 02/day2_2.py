# Author: Roman Berger
# format of input: "minNum-maxNum letter: password"
# find num of valid passswords 

def read_data(fileName):

    myFile = open(fileName, 'r')
    a = myFile.read().splitlines()
    myFile.close()

    for i in range(len(a)):
        # make each string into a list [minNum-maxNum,letter:,password]
        a[i] = a[i].split(" ")
    
        # make the first element of the list a list of 2 int [[minNum,maxNum],letter:,password]
        a[i][0] = a[i][0].split("-")
        a[i][0][0] = int(a[i][0][0])
        a[i][0][1] = int(a[i][0][1])

        # get rid of the colon after the letter
        a[i][1] = a[i][1].replace(':','')

    return a

def is_valid(myList):
    status = False 
    pos1 = myList[0][0]
    pos2 = myList[0][1]
    letter = myList[1]

    if(myList[2][pos1-1] == letter and myList[2][pos2-1] != letter):
        status = True
    elif(myList[2][pos1-1] != letter and myList[2][pos2-1] == letter):
        status = True
    else:
        status = False

    return status

def main_program():

    name = 'input_day2.txt'
    data = read_data(name)

    count = 0

    for i in range(len(data)):
        if(is_valid(data[i]) == True):
            count += 1
        else:
            pass

    print(count)


main_program()

