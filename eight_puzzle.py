import a_star
import re

defaultPuzzle = [[1,2,3],[4,8,0],[7,6,5]]
customPuzzle = []

def doSearch(x):
    return {
        1 : a_star.ucs(customPuzzle),
        2 : a_star.asmth(customPuzzle),
        3 : a_star.asmdh(customPuzzle)
    }.get(x, 'incorrect input')

def getPuzzle(y):
    if y == 1:
        return defaultPuzzle
    else:
        print "    Enter your puzzle, use a zero to represent the blank"
        get = raw_input('    Enter the first row, use space or tabs between numbers ')
        temp = map(int, re.split(', | ', get))
        customPuzzle.append(temp)
        get = raw_input('    Enter the first row, use space or tabs between numbers ')
        temp = map(int, re.split(', | ', get))
        customPuzzle.append(temp)
        get = raw_input('    Enter the third row, use space or tabs between numbers ')
        temp = map(int, re.split(', | ', get))
        customPuzzle.append(temp)
        return customPuzzle

def getAlg():
    print "     Enter your choice of algorithm"
    print "         1. Uniform Cost Search"
    print "         2. A* with the Misplaced Tile heuristic."
    print "         3. A* with the Manhattan distance heuristic.\n"
    return doSearch(input('         '))

def main():
    print "Welcome to Tyson Loveless' 8-puzzle solver."
    print "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."
    puzzle = input()
    thePuzzle = getPuzzle(puzzle)
    for row in thePuzzle:
        print row
    print getAlg()


main()