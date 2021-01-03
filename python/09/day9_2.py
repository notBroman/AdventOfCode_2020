# notBroman
# a number has to be the sum of two numbers that are in the 25 numbers before it
# return the first number that does not fit the requirements

def get_numbers(fileName):
    with open(fileName, 'r') as f:
        numbers = f.read().split('\n')
        numbers.pop(len(numbers)-1)
        
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    return numbers

def is_valid(myList, value):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i):
            if(value == (myList[i] + myList[i+j])):
                return {'Success':True, 'Element': value}
    return {'Success':False, 'Element':value}

def find_set(myList, value):
    
    for i in range(len(myList)):
        total = 0
        j = i+1
        while total < value:
            total = sum(myList[i:j])
#            print(myList[i:j], total)
            if(total == value):
                return myList[i:j]
            else:
                j+=1

def main():
    name = 'input_day9.txt'
    test = 'test.txt'

    data = get_numbers(name)
    preamble = 25
    for i in range(preamble, len(data)):
        result = is_valid(data[i-preamble:i],data[i])
        if(result['Success'] == False):
            answer = result['Element']

    print(answer)

    answer2 = find_set(data,answer)
    answer2.sort()
    print(answer2[0]+answer2[len(answer2)-1])

main()
