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

    for i in range(len(data)):
        data[i] = data[i].replace('\n','')
    
    return data

def no_duplicates(myList):
    for i in range(len(myList)):
        myList[i] = ''.join(set(myList[i]))

def get_amount(myList):
    total = 0

    for i in range(len(myList)):
        total += len(myList[i])

    return total

def main_program():
    name = 'input_day6.txt'
    test = 'test.txt'

    answers = get_data(name)
    no_duplicates(answers)
    print(answers)

    amount = get_amount(answers)
    print(amount)

main_program()

