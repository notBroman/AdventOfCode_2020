# notBroman
# there is a list of bags containing bags
# how many bags does 1 shiny gold bag contain

import string
import re

class bag:
    qty = []
    child = []
    containShinyGold = False

    def __init__(self,str):
        self.qty = []
        self.child = []
        self.colour = str[0]

        for b in str[1:len(str)]:
            if(re.search('no other', b) != None):
                break;
            self.qty.append(int(b[0]))
            self.child.append((b[2:len(b)]))

    def contains(self, collection, topLevel):

        out = 1;
        if(topLevel):
            out = 0;
        if(len(self.qty) == 0):
            return 1
        for i in range(len(self.qty)):
            for b in collection:
                if(b.colour == self.child[i]):
                    out += self.qty[i] * b.contains(collection,False)
                    break

        return out

    def define(self):
        print(self.colour)
        print('->')
        print(len(self.child))

        for i in range(len(self.qty)):
            print(self.child[i])



