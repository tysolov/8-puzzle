import a_star
import re

answerKey = {'1': (1, 1), '2': (1, 2), '3': (1, 3), '4': (2, 1), '5': (2, 2), '6': (2, 3), '7': (3, 1), '8': (3, 2), '0': (3, 3)}


customPuzzle = []

class node:
    def __init__(self, row, col, num):
        self.r = row
        self.c = col
        self.val = num

    def __repr__(self):
        return str(self.val)

    def misplaced(self):
        if
        if answerKey[str(self.val)]==(self.r, self.c):
            return 0
        else: return 1

    def manhattan(self):
        goal = answerKey[str(self.val)]
        return abs(self.r-goal[0]) + abs(self.c-goal[1])

def doSearch(x):
    if x == 1: return a_star.ucs(customPuzzle)
    elif x==2: return a_star.asmth(customPuzzle)
    elif x==3: return a_star.asmdh(customPuzzle)
    else:
        print "incorrect input"
        return getAlg()

def makePuzzle():
    print "    Enter your puzzle, use a zero to represent the blank"
    get = raw_input('    Enter the first row, use space or tabs between numbers ')
    temp = map(int, re.split(', | ', get))
    temp2 = []
    i = 1
    j = 1
    for num in temp:
            x = node(i, j, num)
            temp2.append(x)
            i += 1
    i = 1
    j = 2
    customPuzzle.append(temp2)
    get = raw_input('    Enter the first row, use space or tabs between numbers ')
    temp = map(int, re.split(', | ', get))
    temp2 = []
    for num in temp:
            x = node(i, j, num)
            temp2.append(x)
            i += 1
    i = 1
    j = 3
    customPuzzle.append(temp2)
    get = raw_input('    Enter the third row, use space or tabs between numbers ')
    temp = map(int, re.split(', | ', get))
    temp2 = []
    for num in temp:
            x = node(i, j, num)
            temp2.append(x)
            i += 1
    customPuzzle.append(temp2)
    return customPuzzle

def getPuzzle():
    print "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."
    y = input()
    if y == 1: return defaultPuzzle
    elif y == 2: return makePuzzle()
    else:
        print "incorrect input"
        return getPuzzle()


def getAlg():
    print "     Enter your choice of algorithm"
    print "         1. Uniform Cost Search"
    print "         2. A* with the Misplaced Tile heuristic."
    print "         3. A* with the Manhattan distance heuristic.\n"
    return doSearch(input('         '))

defaultPuzzle = [[node(1,1,1),node(1,2,2),node(1, 3,3)],
                 [node(2,1,4),node(2,2,8),node(2,3,0)],
                 [node(3,1,7),node(3,2,6),node(3,3,5)]]

def main():
    print "Welcome to Tyson Loveless' 8-puzzle solver."
    thePuzzle = getPuzzle()
    for row in thePuzzle:
        print row
    print getAlg()

main()