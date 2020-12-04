# Roman Berger
# program that checks if a dataset is valid and counts how many there are 
# all necassary fields need to be provided in a dataset
# datasets are separated by '\n\n' 
# necassary fields: 
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)

def get_data(fileName):
    with open(fileName, 'r') as f:
        data =f.read().split('\n\n')

    for i in range(len(data)):
        data[i] = data[i].replace('\n',' ')
        data[i] = data[i].split(' ')
        for j in range(len(data[i])):
            data[i][j] = data[i][j].split(':')

    return data

def check_dataset(myList):
    shortenedList = []
    count = 0
    countLenTen = 0
    for i in range(len(myList)):
        if(len(myList[i]) == 7):
            shortenedList.append(myList[i])

            for j in range(7):
                if(myList[i][j][0] == 'cid'):
                    count += 1
                else:
                    pass

        elif(len(myList[i]) == 8):
            countLenTen += 1
            pass

    return [len(shortenedList), count, countLenTen]

def main_program():
    name = 'day4_input.txt'
    data = get_data(name)


    results = (check_dataset(data))
    total = results[2] + results[0] - results[1]
    print(results)
    print(total)

main_program()
