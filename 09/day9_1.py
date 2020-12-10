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

def main():
    name = 'input_day9.txt'
    test = 'test.txt'

    data = get_numbers(test)
    print(data)

main()
