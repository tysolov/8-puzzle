#eight_puzzle.py implements the text UI and runs the puzzle game
# format for text UI taken from project promp
import general_search
import re
import puzzle

# default puzzle
default = puzzle.Puzzle([1, 2, 3, 4, 0, 6, 7, 5, 8])
                         #4, 1, 2, 7, 5, 3, 8, 6, 0])
                         #4, 2, 8, 6, 0, 3, 7, 5, 1])
                         #0, 8, 7, 6, 5, 4, 3, 2, 1])
                         #8, 6, 7, 2, 5, 4, 3, 0, 1])


#answer is automatically generated
answer = []
for i in range(1, puzzle.size, 1):
    answer.append(i)
answer.append(0)
customPuzzle = []


# the following are helper functions for a text-based UI
# makePuzzle receives input from the user to make a customized 8-puzzle, no error checking is currently in place
def makePuzzle():
    print "    Enter your puzzle, use a zero to represent the blank"
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
    return puzzle.Puzzle(customPuzzle)


# getPuzzle gets a default or user-entered puzzle from the user
def getPuzzle():
    print "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."
    y = input()
    if y == 1:
        return default
    elif y == 2:
        return makePuzzle()
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
    if not  puzzle.checkSolvable(thePuzzle.INITIAL_STATE.STATE):
        print "This puzzle is not solvable!"
        exit(0)
    if not(option > 3) and not(option < 1):
        return general_search.search(thePuzzle, option)
    else:
        print "incorrect input"
        return getAlg()



# entry point of program
print "Welcome to Tyson Loveless' 8-puzzle solver."
thePuzzle = getPuzzle()
print "Here is the chosen puzzle: "

general_search.printPuzzle(thePuzzle.INITIAL_STATE)
result, total, maxSize = getAlg(thePuzzle)
if result is 0:
    print "You have discovered a bug - please report this to tlove004@ucr.edu!"
    print "Please include the exact puzzle used to recreate the bug and the search method used"
else:
    print "\n\nGoal!!"
    print "\nTo solve this problem the search algorithm expanded a total number of %d nodes." % total
    print "The maximum number of nodes in the queue at any one time was %i" % maxSize
    print "The depth of the goal node was %d" % result.DEPTH

x = raw_input(' Print Trace? ')
if x:
    if x[0]=='y' or 'Y':
        trace = []
        trace.append(result.STATE)
        node = result.PARENT
        while node.PARENT is not None:
            trace.append(node.STATE)
            node = node.PARENT
        trace.append(node.STATE)
        trace.reverse()
        for state in trace:
            general_search.printPuzzle(state)
            print ''

print '   Done'
