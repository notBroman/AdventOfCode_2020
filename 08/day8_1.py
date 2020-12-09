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


def main():
    name = 'input_day8.txt'
    test = 'test.txt'

    instructions = get_data(test)
    print(instructions)

main()
