# Roman Berger
# program that checks if a dataset is valid and counts how many there are 
# all necassary fields need to be provided in a dataset
# datasets are separated by '\n\n' 
# necassary fields: 
#    byr (Birth Year): 1920 - 2002
#    iyr (Issue Year): 2010 - 2020
#    eyr (Expiration Year): 2020 - 2030
#    hgt (Height): 150 -193 cm or 59 -76 in
#    hcl (Hair Color): '#' followed by six digits '0-9' and 'a-f'
#    ecl (Eye Color): amb, blu, brn, gry, grn, hzl, oth
#    pid (Passport ID): nine digits with leading zeroes
#    cid (Country ID): dont matter

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
    checkList = [['byr', False], ['iyr', False], ['eyr', False], ['hgt', False], ['hcl', False], ['ecl', False], ['pid', False], ['cid',True]]
    
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
