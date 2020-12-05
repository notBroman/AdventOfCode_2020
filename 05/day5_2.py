# Roman Berger
# a program that finds my seat on a plane by scanning all the other tickets
# ticket format : 1-7 F(ront) or B(ack) describes the 128 rows: 0-127
#                 8-10 L(eft) or R(ight) describes 8 colums: 0-7

# convert seats into binaty number -> convert into decimal
# f=0 b=1 && l=0 r=1

def get_data(fileName):
    with open(fileName, 'r') as f:
        data = f.read().splitlines()

    return data

def to_binary(myList):
    
    for i in range(len(myList)):
            myList[i] = myList[i].replace('F','0')
            myList[i] = myList[i].replace('B','1')

            myList[i] = myList[i].replace('L','0')
            myList[i] = myList[i].replace('R','1')

def get_ticket_id(myString):

    row = (int(myString[:7], 2))
    column =(int(myString[-3:], 2))

    return row *8 + column

def find_max(myList):
    highSeat = 0

    for i in range(len(myList)):
        if(highSeat < get_ticket_id(myList[i])):
            highSeat = get_ticket_id(myList[i])

    return highSeat

def find_my_seat(myList):
    total = 0
    for i in range(51,833):
        total += i

    for i in range(len(myList)):
        total -= get_ticket_id(myList[i])

    return total

def main_program():
    name = 'input_day5.txt'

    seats = get_data(name)
    to_binary(seats)
    print(find_my_seat(seats))

main_program()

