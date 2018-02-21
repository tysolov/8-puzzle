# eight_puzzle.py implements the text UI and runs the puzzle game
# format for text UI taken from project prompt
import general_search
import re
import puzzle

ninepuzzle = [[1, 2, 3, 4, 5, 6, 7, 8, 0],  # 0 - trivial
              [1, 2, 3, 4, 5, 6, 8, 7, 0],  # 1 - impossible
              [1, 2, 3, 4, 5, 6, 7, 0, 8],  # 2 - very easy
              [1, 2, 0, 4, 5, 3, 7, 8, 6],  # 3 - easy
              [1, 2, 3, 4, 0, 6, 7, 5, 8],  # 4 - requested for report  (test1)
              [1, 2, 3, 4, 5, 7, 8, 0, 6],  # 5 - test2
              [4, 2, 8, 6, 0, 3, 7, 5, 1],  # 6 - test3
              [0, 1, 2, 4, 5, 3, 7, 8, 6],  # 7 - doable
              [8, 7, 1, 6, 0, 2, 5, 4, 3],  # 8 - oh boy
              [0, 8, 7, 6, 5, 4, 3, 2, 1],  # 9 - test4
              [6, 4, 7, 8, 5, 0, 3, 2, 1],  # 10 - 31
              [8, 6, 7, 2, 5, 4, 3, 0, 1]]  # 11 - 31 #2

fifteenpuzzle = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15],  # easy
                 [8, 6, 7, 5, 10, 0, 3, 1, 2, 14, 11, 13, 15, 9, 4, 12],  # solvable, deep
                 [6, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 12, 13, 3],  # solvable, but deep
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]]  # impossible

twentyfourpuzzle = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 0, 23, 24],    # easy
                    [7, 24, 22, 18, 4, 0, 23, 16, 3, 6, 1,
                                9, 8, 14, 12, 10, 20, 17, 19, 15, 5, 11, 21, 13, 2],   # solvable
                    [1, 13, 5, 18, 14, 20, 15, 11, 8, 21,
                                19, 24, 7, 6, 4, 16, 0, 23, 17, 3, 10, 2, 12, 9, 22],  # deep
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 23, 0]]    # impossible

# default puzzle
def getDefault():
    if puzzle.size == 9:
        y = input("Please select a puzzle difficulty between 0 and 11: ")
        if y in range(0, 12):
            default = puzzle.Puzzle(ninepuzzle[y])
        else:
            print "incorrect input"
            return getDefault()
    elif puzzle.size == 16:
        y = input("Please select a puzzle difficulty between 0 and 3: ")
        if y in range(0, 4):
            default = puzzle.Puzzle(fifteenpuzzle[y])
        else:
            print "incorrect input"
            return getDefault()
    elif puzzle.size == 25:
        y = input("Please select a puzzle difficulty between 0 and 3: ")
        if y in range(0, 4):
            default = puzzle.Puzzle(twentyfourpuzzle[y])
        else:
            print "incorrect input"
            return getDefault()
    return default


# the following are helper functions for a text-based UI
# makePuzzle receives input from the user to make a customized 8-puzzle, no error checking is currently in place
def makePuzzle(x):
    customPuzzle = []
    print "    Enter your " + str(x) + ", use a zero to represent the blank"
    get = raw_input('    Enter the first row, use space or tabs between numbers ')
    temp = map(int, re.split(', | ', get))
    for num in temp:
            customPuzzle.append(num)

    get = raw_input('    Enter the second row, use space or tabs between numbers ')
    temp = map(int, re.split(', | ', get))
    for num in temp:
            customPuzzle.append(num)
    get = raw_input('    Enter the third row, use space or tabs between numbers ')
    temp = map(int, re.split(', | ', get))
    for num in temp:
            customPuzzle.append(num)
    if puzzle.edge > 3:
        get = raw_input('    Enter the fourth row, use space or tabs between numbers ')
        temp = map(int, re.split(', | ', get))
        for num in temp:
            customPuzzle.append(num)
    if puzzle.edge > 4:
        get = raw_input('    Enter the fifth row, use space or tabs between numbers ')
        temp = map(int, re.split(', | ', get))
        for num in temp:
            customPuzzle.append(num)
    if x is "goal":
        return puzzle.makeAnswer(customPuzzle)
    else:
        return puzzle.Puzzle(customPuzzle)


# getPuzzle gets a default or user-entered puzzle from the user
def getPuzzle():
    print "Type \"1\" to use a default puzzle, \"2\" to enter your own puzzle, or \"3\" to change the puzzle size: ",
    y = input('')
    if y == 1:
        return getDefault()
    elif y == 2:
        return makePuzzle("puzzle")
    elif y == 3:
        return changeSize()
    else:
        print "incorrect input"
        return getPuzzle()


def changeSize():
    print "Type \"1\" for an 8-puzzle, \"2\" for a 15-puzzle, or \"3\" for a 25-puzzle: ",
    size = input('')
    if size == 1:
        puzzle.setup(9)
    elif size == 2:
        puzzle.setup(16)
    elif size == 3:
        puzzle.setup(25)
    else:
        print "incorrect input"
        return changeSize()
    general_search.setDiameter()
    return getPuzzle()



# getAlg gets the search choice from the user and calls the corresponding search function in general_search.py
def getAlg(thePuzzle):
    print "     Enter your choice of algorithm"
    print "         1. Uniform Cost Search"
    print "         2. A* with the Misplaced Tile heuristic."
    print "         3. A* with the Manhattan distance heuristic.\n"
    option = input('         ')
    if goalState is 1:
        if not puzzle.checkSolvable(thePuzzle.INITIAL_STATE.STATE):
            print "This puzzle is not solvable!"
            exit(0)
    if not(option > 3) and not(option < 1):
        return option
    else:
        print "incorrect input"
        return getAlg(thePuzzle)

def goal():
    global goalState
    print "\nEnter \"1\" for the standard goal state or \"2\" to search for a specific goal: ",
    goalState = input('')
    if goalState is 1:
        return puzzle.makeAnswer()
    elif goalState is 2:
        return makePuzzle("goal")
    else:
        return goal()



# entry point of program
print "Welcome to Tyson Loveless' 8-puzzle solver."
thePuzzle = getPuzzle()
print "Here is the chosen puzzle: "

general_search.printPuzzle(thePuzzle.INITIAL_STATE)

answer = goal()
print "We are looking for this goal: "

general_search.printPuzzle(answer)

option = getAlg(thePuzzle)
result, total, maxSize = general_search.search(thePuzzle, option)
if result is 0:
    print "Your goal is unreachable from the starting position!"
else:
    print "\n\nGoal!!"
    print "\nTo solve this problem the search algorithm expanded a total number of %d nodes." % total
    print "The maximum number of nodes in the queue at any one time was %i" % maxSize
    print "The depth of the goal node was %d" % result.DEPTH
if result.DEPTH:
    x = raw_input(' Print Solution Trace? ')
else:
    x = 0
if x:
    if x[0] == 'y' or x[0] == 'Y':
        trace = []
        trace.append(result)
        node = result.PARENT
        while node.PARENT is not None:
            trace.append(node)
            node = node.PARENT
        trace.append(node)
        trace.reverse()
        for node in trace[:len(trace)-1]:
            print "Expanding node with g(n) = %d and h(n) = " % node.DEPTH,
            if option == 1:
                print "0"
            elif option == 2:
                print "%d" % node.MISPLACED
            else:
                print "%d" % node.MANHATTAN
            general_search.printPuzzle(node.STATE)
            print '...'
        general_search.printPuzzle(trace[len(trace)-1].STATE)
        print "\n\nGoal!!"
        print "\nTo solve this problem the search algorithm expanded a total number of %d nodes." % total
        print "The maximum number of nodes in the queue at any one time was %i" % maxSize
        print "The depth of the goal node was %d" % result.DEPTH

print '   Done'
