# notBroman
# there is a map of seats . -> floor, L -> empty, # -> taken
# rules for seating:
#    if seat is empty and no adjacent seat is taken it becomes taken
#    if the seat is taken and 4 or more adjacent seas are taken it becomes empty
#    otherwise the seats state doesnt change

def get_seats(fileName):
    with open(fileName, 'r') as f:
        data = f.read().split('\n')
        data.pop(len(data)-1)

    for i in range(len(data)):
        data[i] = list(data[i])

    return data

def print_seats(myList):
    for i in range(len(myList)):
        print(myList[i])

    print('\n')

def adjacent_seats(myList,row,seat):
    count = 0

    for n in range(-1,2):
        for m in range(-1,2):

            r = row+n
            s = seat+m
            if r < 0 or r >= len(myList) or s < 0 or s >= len(myList[row]):
                count += 0
            elif n == 0 and m == 0:
                count += 0
            else:
                currentSeat = myList[r][s]
                if currentSeat == '#':
                    if n == 0 and m == 0:
                        count += 0
                    else:
                        count +=1
                else:
                        count += 0

    return count

def check_seats(myList):
    temp_b = list()
    for i in range(len(myList)):
        temp_b.append(list())
        for j in range(len(myList[i])):
            currentSeat = myList[i][j]
           
            if(currentSeat == 'L' and adjacent_seats(myList,i,j) == 0):
                temp_b[i].append('#')
            elif(currentSeat == '#' and adjacent_seats(myList,i,j) > 3):
                temp_b[i].append('L')
            else:
                temp_b[i].append(currentSeat)

    return temp_b

def count_full_seats(myList):
    total = 0
    for i in range(len(myList)):
        total += myList[i].count('#')

    return total

def main():
    test = 'test.txt'
    name = 'input_day11.txt'

    seats = get_seats(name)
    print_seats(seats)

    seats = check_seats(seats)
    print_seats(seats)

    for i in range(1000):
        seats = check_seats(seats)
        print_seats(seats)

    print(count_full_seats(seats))

main()
