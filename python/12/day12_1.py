# notBroman
# there are instructions for a ship
# N: North for given distance
# S: South for given distance
# E: East for given distance
# W: West for given distance
# L: Turn left the given number of degrees
# R: Turn right the given number of degrees
# F: Forward in the facing direction
# the ship is facing east in the start and doesnt turn when it moves

def get_instructions(fileName):
    with open(fileName, 'r') as f:
        data = f.read().split('\n')
        data.pop(len(data)-1)

    return data

def main():
    name = 'input_day12.txt'
    test = 'test.txt'

    instructions = get_instructions(test)
    print(instructions)

main()

