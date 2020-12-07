# notBroman
# there is a list of bags that contain other bags
# you have a shiny gold bag
# how many other bags can contain this bag

import string

def get_rules(fileName):
    with open(fileName, 'r') as inputFile:
        rules = inputFile.readlines()

    for i in range(len(rules)):
        rules[i] = rules[i].replace('\n','')
        rules[i] = rules[i].split(' contain ')

    return rules

def get_bags(listOfRules, newList):
    length = len(newList)

    for i in range(len(listOfRules)):
        for j in range(len(newList)):
            if(newList[j] in listOfRules[i][1] and listOfRules[i][0][:-5] not in newList):
                newList.append(listOfRules[i][0][:-5])

    if(len(newList) > length):
        get_bags(listOfRules, newList)

def get_bags_inside(listOfRules):
    pass

def main():

    name = 'input_day7.txt'
    test = 'test.txt'
    listOfBags = ['shiny gold']

    regulations = get_rules(test)
    get_bags(regulations, listOfBags)

    print(regulations)
#    print(listOfBags)
#    print(len(listOfBags)-1)

if __name__ == '__main__':
    main()

