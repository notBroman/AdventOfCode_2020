# notBroman
# there is a customs declaration sheet with 26 questions (a-z)
# you note down the questions groups answer yes to
# for each group a question counts once at most and only if everyone picked it
# groups are split by '\n\n'
# people in those groups are split by '\n'
# find the total number of questions that were answered yes by the whole group

def get_data(fileName):
    with open(fileName, 'r') as f:
        data = f.read().split('\n\n')
        data[(len(data)-1)] = data[(len(data)-1)].replace('\n','')

    for i in range(len(data)):
        data[i] = data[i].replace('\n','-')
    
    return data

def erase_duplicates(myList):
    for i in range(len(myList)):
        myList[i] = ''.join(set(myList[i]))

def get_amount(myList):
    total = 0

    for i in range(len(myList)):
        total += len(myList[i])
    return total

def get_collective_yes(myList):
    for i in range(len(myList)):
        if('-' in myList[i]):
            j = 0
            newItem = ''
            while (j < myList[i].index('-')):
                if(myList[i].count(myList[i][j]) > (myList[i].count('-'))):
                    newItem += myList[i][j]
                j += 1
            myList[i] = newItem

def main_program():
    name = 'input_day6.txt'
    test = 'test.txt'

    answers = get_data(name)
    print(len(answers))
    get_collective_yes(answers)
    print(len(answers))
    amount = get_amount(answers)
    print(amount)

main_program()

