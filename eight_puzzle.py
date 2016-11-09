#eight_puzzle.py implements the text UI and runs the puzzle game
# format for text UI taken from project promp
import general_search
import re
import puzzle

# default puzzle
default = puzzle.Puzzle([#1, 2, 3, 4, 0, 6, 7, 5, 8])
                         #4, 1, 2, 7, 5, 3, 8, 6, 0])
                         #4, 2, 8, 6, 0, 3, 7, 5, 1])
                         #1, 2, 3, 4, 5, 7, 8, 0, 6])
                         #0, 8, 7, 6, 5, 4, 3, 2, 1])
                         8, 6, 7, 2, 5, 4, 3, 0, 1])  #31


goalState = 0


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
    if x is "goal":
        return puzzle.makeAnswer(customPuzzle)
    else:
        return puzzle.Puzzle(customPuzzle)


# getPuzzle gets a default or user-entered puzzle from the user
def getPuzzle():
    print "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."
    y = input()
    if y == 1:
        return default
    elif y == 2:
        return makePuzzle("puzzle")
    else:
        print "incorrect input"
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
print "We are looking for this goaL: "

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

x = raw_input(' Print Solution Trace? ')
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
