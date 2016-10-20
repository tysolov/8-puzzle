import general_search
import re
answer = [1, 2, 3, 4, 5, 6, 7, 8, 0]
customPuzzle = []


def swap(self, x, y):
    self[x], self[y] = self[y], self[x]


def misplaced(state):
    num = 0
    for i in range(0, 8, 1):
        if state[i] != answer[i]:
            num += 1
    return num


def manhattan(state):
    dist = 0
    for i in range(0, 8, 1):
        val = state.index(i)
        ans = answer.index(i)
        if val == ans:
            continue
        elif val in [0, 1, 2]:
            if ans in [0, 1, 2]:
                dist += abs(val - ans)
            elif ans in [3, 4, 5]:
                val += 3
                dist += abs(val - ans) + 3
            else:
                val += 6
                dist += abs(val - ans) + 6
        elif val in [3, 4, 5]:
            if ans in [3, 4, 5]:
                dist += abs(val - ans)
            elif ans in [0, 1, 2]:
                val -= 3
                dist += abs(val - ans) + 3
            else:
                val += 6
                dist += abs(val - ans) + 6
        elif val in [6, 7, 8]:
            if ans in [6, 7, 8]:
                dist += abs(val - ans)
            elif ans in [3, 4, 5]:
                val -= 3
                dist += abs(val - ans) + 3
            else:
                val -= 6
                dist += abs(val - ans) + 6
    return dist


class node:
    def __init__(self, state, parent=None):
        self.STATE = state
        self.MISPLACED = misplaced(state)
        self.MANHATTAN = manhattan(state)
        if parent is None:
            self.PARENT = None
            self.DEPTH = 0
        else:
            self.STATE = state
            self.PARENT = parent #list
            self.DEPTH = self.PARENT.DEPTH+1

    def __getitem__(self, item):
        return self.STATE[item]

    def __index__(self, item):
        return self.STATE.index(item)

    def swap(self, x, y):
        self.STATE[x], self.STATE[y] = self.STATE[y], self.STATE[x]


def move_left(state, pos):
    if pos in [0, 3, 6]:
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos-1)
        return child


def move_right(state, pos):
    if pos in [2, 5, 8]:
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos+1)
        return child


def move_up(state, pos):
    if pos in [0, 1, 2]:
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos-3)
        return child


def move_down(state, pos):
    if pos in [6, 7, 8]:
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos+3)
        return child


def test_goal(state):
    if state == answer:
        return 1
    else:
        return 0


class Puzzle:
    def __init__(self, initialState):
        self.INITIAL_STATE = node(initialState)
        self.OPERATORS = [move_left, move_right, move_up, move_down]
        self.GOAL_TEST = test_goal


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
    return Puzzle(customPuzzle)


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


def getAlg(thePuzzle):
    print "     Enter your choice of algorithm"
    print "         1. Uniform Cost Search"
    print "         2. A* with the Misplaced Tile heuristic."
    print "         3. A* with the Manhattan distance heuristic.\n"
    option = input('         ')
    if not(option > 3) and not(option < 1):
        return general_search.search(thePuzzle, option)
    else:
        print "incorrect input"
        return getAlg()

default = Puzzle([1, 2, 3,
                  4, 8, 0,
                  7, 6, 5])

def main():
    print "Welcome to Tyson Loveless' 8-puzzle solver."
    thePuzzle = getPuzzle()
    result, total, max = getAlg(thePuzzle)
    if result is 0:
        print "Failure!  No solution to this problem"
    else:
        print "\n\nGoal!!"
        print "\nTo solve this problem the search algorithm expanded a total number of %d nodes." % total
        print "The maximum number of nodes in the queue at any one time was %i" % max
        print "The depth of the goal node was %d" %result.DEPTH

main()