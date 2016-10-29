#puzzle.py defines nodes, rules, and functions for the eight-puzzle game
# functions are defined in a way to easily expand to a 15, 25, or larger puzzle
# all functions are written and conceptualized by Tyson Loveless
from math import sqrt
# helper function for updating state

#update this to change puzzle type
size = 9
edge = int(sqrt(size))

#answer is generated based on size of puzzle
answer = []
for i in range(1, size, 1):
    answer.append(i)
answer.append(0)
def swap(self, x, y):
    self[x], self[y] = self[y], self[x]


# this function checks for solvability using the rules found at
# https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
def checkSolvable(puzzle):
    inversions = 0
    check = list(puzzle)
    check.remove(0)
    for i in range(0, check.__len__(), 1):
        for j in range(i, check.__len__(), 1):
            if check[i] > check[j]:
                inversions += 1
    if edge % 2 == 1: #odd edge size
        return not(inversions % 2) #solvable if even
    else:   # even edge size
        zeroPosition = puzzle.index(0)
        # check if in even row
        for i in range(0, edge*edge, edge*2):
            for j in range(0, edge, 1):
                if zeroPosition == i+j:
                    return inversions % 2 # solvable if odd
        else: # in odd row
            return not(inversions % 2) #solvable if even


# calculates total misplaced tiles
def misplaced(state):
    num = 0
    for i in range(0, size, 1):
        if state[i] is 0:
            continue
        if state[i] != answer[i]:
            #simply increments whenever the tiles are out of place
            num += 1
    return num


# calculates total manhattan distance
def manhattan(state):
    dist = 0
    for i in range(1, size, 1):
        val = state.index(i)
        ans = answer.index(i)
        if val == ans:  #manhattan distance for tile = 0
            continue
        #for each else branch below, first the vertical displacement is checked
        # then the horizontal displacement is found
        elif val in range(0, edge, 1):
            if ans in range(0, edge, 1):
                dist += abs(val - ans)
            elif ans in range(edge, edge*2, 1):
                val += edge
                dist += abs(val - ans) + 1
            else:
                val += edge*2
                dist += abs(val - ans) + 2
        elif val in range(edge, edge*2, 1):
            if ans in range(edge, edge*2, 1):
                dist += abs(val - ans)
            elif ans in range(0, edge, 1):
                val -= edge
                dist += abs(val - ans) + 1
            else:
                val += edge
                dist += abs(val - ans) + 1
        elif val in range(edge*2, edge*3, 1):
            if ans in range(edge*2, edge*3, 1):
                dist += abs(val - ans)
            elif ans in range(edge, edge*2, 1):
                val -= edge
                dist += abs(val - ans) + 1
            else:
                val -= edge*2
                dist += abs(val - ans) + 2
    return dist


# The node class defines the structure that holds the current state and all relevant information
#  about the state, including heuristics and current depth from the root node
class node:
    # nodes are initialized with state, heuristic values, and current depth
    def __init__(self, state, parent=None):
        self.STATE = state
        self.MISPLACED = None
        self.MANHATTAN = None
        # a parent will be at depth 0
        if parent is None:
            self.PARENT = None
            self.DEPTH = 0
        # all other nodes will be at 1 greater depth than wherever they were traversed from
        else:
            self.STATE = state
            self.PARENT = parent #list
            self.DEPTH = self.PARENT.DEPTH+1

    def __getitem__(self, item):
        return self.STATE[item]

    def mis(self):
        if self.MISPLACED is None:
            self.MISPLACED = misplaced(self.STATE)
        return self.MISPLACED

    def man(self):
        if self.MANHATTAN is None:
            self.MANHATTAN = manhattan(self.STATE)
        return self.MANHATTAN

    def __index__(self, item):
        return self.STATE.index(item)

    def swap(self, x, y):
        self.STATE[x], self.STATE[y] = self.STATE[y], self.STATE[x]


# the following functions define the allowable operations for the game
# each of these functions are applied to the blank (0) tile
# for each function, the legality of the move is first checked, then if legal the move is performed
def move_left(state, pos):
    if pos in range(0, edge*(edge-1)+1, edge):
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos-1)
        return child


def move_right(state, pos):
    if pos in range(edge-1, edge*edge, edge):
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos+1)
        return child


def move_up(state, pos):
    if pos in range(0, edge, 1):
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos-edge)
        return child


def move_down(state, pos):
    if pos in range(edge*(edge-1), edge*edge, 1):
        return 0
    else:
        child = node(list(state), state)
        child.swap(pos, pos+edge)
        return child


# this function simply tests if the current state is a goal state
def test_goal(state):
    if state == answer:
        return 1
    else:
        return 0


# the structure of the puzzle: the root node, legal operators, and goal are all defined to define our problem scope
class Puzzle:
    def __init__(self, initialState):
        self.INITIAL_STATE = node(initialState)
        self.OPERATORS = [move_left, move_right, move_up, move_down]
        self.GOAL_TEST = test_goal