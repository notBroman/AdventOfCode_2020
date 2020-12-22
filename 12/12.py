# notBroman
# there are instructions for a ship
# N: North for given distance
# S: South for given distance
# E: East for given distance
# W: West for given distance
# L: Turn left the given number of degrees
# R: Turn right the given number of degrees
# F: Forward in the facing direction
# the ship is facing east (90) in the start and doesnt turn when it moves

import fileinput
import re

#def get_instructions(fileName):
#    with open(fileName, 'r') as f:
#        data = f.read().split('\n')
#        data.pop(len(data)-1)
#
#    return data

class Ship:
    def __init__(self, x, y, direction, waypointX, waypointY):
        self.x = x
        self.y = y
        self.wayX = waypointX
        self.wayY = waypointY
        self.direction = direction

    def move(self, instr):
        part1 = instr[:1]
        part2 = int(instr[1:])

        relX = self.wayX - self.x
        relY = self.wayY - self.y

        if part1 == 'F':
            self.x += (part2*relX)
            self.y += (part2*relY)
        elif part1 == 'N':
            self.wayY += part2
        elif part1 == 'E':
            self.wayX += part2
        elif part1 == 'S':
            self.wayY -= part2
        elif part1 == 'W':
            self.wayX -= part2
        
        elif part1 == 'R':
            self.direction += part2

        elif part1 == 'L':
            self.direction = self.direction - part2 + 360
        if self.direction >= 360:
            self.direction %= 360

def main():
    instructions = list(fileinput.input())
    for i in range(len(instructions)):
        instructions[i] = instructions[i][:-1]
        
    print(instructions)

    ship = Ship(0,0,90,10,1)

    for i in range(len(instructions)):
        ship.move(instructions[i])

    print('x:', ship.x, 'y:', ship.y)


main()

