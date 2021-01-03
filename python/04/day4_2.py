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


# right answer is 186, i am off by one the mistake happens when i check for hgt, ecl or pid

import string

def get_data(fileName):
    with open(fileName, 'r') as f:
        data =f.read().split('\n\n')

    for i in range(len(data)):
        data[i] = data[i].replace('\n',' ')
        data[i] = data[i].split(' ')
        for j in range(len(data[i])):
            data[i][j] = data[i][j].split(':')
   
    data[len(data)-1].pop(len(data[len(data)-1])-1)

    return data

def check_passport(myList):
    #    checkList = [['byr', False], ['iyr', False], ['eyr', False], ['hgt', False], ['hcl', False], ['ecl', False], ['pid', False], ['cid',True]]
    
    passportLen7 = []
    passportLen8 = []
    for i in range(len(myList)):
        if(len(myList[i]) == 7):
            noCid = True

            for j in range(7):
                if(myList[i][j][0] == 'cid'):
                    noCid = False
            if(noCid == True):
                passportLen7.append(myList[i])

        elif(len(myList[i]) == 8):
            passportLen8.append(myList[i])

    return passportLen7 + passportLen8

def is_hex(s):
    for c in s:
        if c not in string.hexdigits:
            return False

    return True

def verify_passport(myList):
    colours = ['amb','blu','brn','gry','grn','hzl','oth']

    for i in range(len(myList)):
        if(myList[i][0] == 'byr'):
            if not(int(myList[i][1]) <= 2002 and int(myList[i][1]) >= 1920):
                return False

        elif(myList[i][0] == 'iyr'):
            if not(int(myList[i][1]) <= 2020 and int(myList[i][1]) >= 2010):
                return False

        elif(myList[i][0] == 'eyr'):
            if not(int(myList[i][1]) <= 2030 and int(myList[i][1]) >= 2020):
                return False

        elif(myList[i][0] == 'hgt'):
            try:
                if(myList[i][1][-2:] == 'in' and not(int(myList[i][1][:2]) <= 76 and int(myList[i][1][:2]) >= 59)):
                    return False
                elif(myList[i][1][-2:] == 'cm' and not(int(myList[i][1][:3]) <= 193 and int(myList[i][1][:3]) >= 150)):
                    return False

            except Exception:
                return False
        
        elif(myList[i][0] == 'hcl'):
            if not (len(myList[i][1]) == 7 and myList[i][1][:-6] == '#' and is_hex(myList[i][1][1:])):
                return False

        elif(myList[i][0] == 'ecl' and (myList[i][1] not in colours)):
            return False

        elif(myList[i][0] == 'pid'):
            if(len(myList[i][1]) != 9 and myList[i][1][:2] != '00'):
                print(myList[0])
                return False

    return True

def main_program():
    name = 'day4_input.txt'
    data = get_data(name)

    count = 0
    results = (check_passport(data))

#    print(results)

    for i in range(len(results)):
#        print(verify_passport(results[i]))
        if(verify_passport(results[i]) == True):
            count += 1
    print(count)
main_program()
