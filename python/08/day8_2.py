# notBroman
# there is a list instuctions that create a loop
# run the program until an instuction is executed twice
# possible instuctions:
#   nop: no operation
#   acc: raise a variable by the number following it can be pos or neg
#   jmp: jump relative to the command to the current line

def get_data(fileName):
    with open(fileName, 'r') as f:
        data = f.read().split('\n')
        del data[len(data)-1]

    for i in range(len(data)):
        data[i] = data[i].split(' ')
        data[i][1] = int(data[i][1])

    return data

def execute(myList):
    i = 0
    count = 0
    executedLines = []

    while(i < len(myList)-1):
        if(i in executedLines):
            return {'success':False, 'accumulator':count, 'executedLines':executedLines}
        elif(myList[i][0] == 'acc'):
            count += myList[i][1]
            executedLines.append(i)
            i += 1
        elif(myList[i][0] == 'jmp'):
            executedLines.append(i)
            i += myList[i][1]
        else:
            executedLines.append(i)
            i += 1

    return {'success':True, 'accumulator':count, 'executedLines':executedLines}

def change_operation(myList, indexOfChange):
    if(myList[indexOfChange][0] == 'nop'):
        myList[indexOfChange][0] = 'jmp'
    elif(myList[indexOfChange][0] == 'jmp'):
        myList[indexOfChange][0] = 'nop'
    else:
        print('Error')

def main():
    name = 'input_day8.txt'
    test = 'test.txt'

    instructions = get_data(name)
    commands = execute(instructions)
    
    i=0
    while(i < len(commands['executedLines'])-1):
        change_operation(instructions,commands['executedLines'][i])
        result = execute(instructions)
        if(result['success'] == False):
            change_operation(instructions,commands['executedLines'][i])
            i+=1
        else:
            i = len(commands['executedLines'])+1
    
    print(result['accumulator'])

main()
