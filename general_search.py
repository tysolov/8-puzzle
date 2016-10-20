from heapq import heappush, heappop

global MAX_QUEUE_SIZE
global TOTAL_EXPANDED

def printPuzzle(state):
    j = 0
    for i in range(0, 3):
        print '      ',
        while j < 3:
            print state[j + 3 * i],
            j += 1
        print ""
        j = 0


def expand(node, operators):
    nodes = []
    pos = node.STATE.index(0)
    for op in operators:         #operators is list of functions
        child = op(node, pos)          #gets child from position using operator, if illegal child = 0
        if child:                # if operator was legal move
            nodes.append(child)
    return nodes

def search(problem, function):
    TOTAL_EXPANDED = 0
    MAX_QUEUE_SIZE = 0
    nodes = []
    closed = []
    root = [problem.INITIAL_STATE.DEPTH, problem.INITIAL_STATE]
    print "Root state: "
    printPuzzle(root[1].STATE)
    closed.append(root[1].STATE)
    for state in expand(root[1], problem.OPERATORS):
        if state.STATE not in closed:
            if function is 1:
                print "The best state to traverse to with a g(n) = %d and h(n) = %d is..." % (state.DEPTH, 0)
                printPuzzle(state.STATE)
                print '          Traversing this node...'
                heappush(nodes, [state.DEPTH, state])
            elif function is 2:
                print "The best state to traverse to with a g(n) = %d and h(n) = %d is..." % (state.DEPTH, state.MISPLACED)
                printPuzzle(state.STATE)
                print '          Traversing this node...'
                heappush(nodes, [state.MISPLACED, state])
            else:
                print "The best state to traverse to with a g(n) = %d and h(n) = %d is..." % (state.DEPTH, state.MANHATTAN)
                printPuzzle(state.STATE)
                print '          Traversing this node...'
                heappush(nodes, [state.MANHATTAN, state])
            TOTAL_EXPANDED += 1
            MAX_QUEUE_SIZE += 1
        if problem.GOAL_TEST(state.STATE):
            # print 'depth is ' + str(node.DEPTH)
            return state, TOTAL_EXPANDED, MAX_QUEUE_SIZE

    while True:
        if not nodes: #nodes is empty
            return 0
        #heapsort(nodes)
        cost, node = heappop(nodes)
        MAX_QUEUE_SIZE -= 1
        #print '               Expanding this node...'
        closed.append(node.STATE)
        for state in expand(node, problem.OPERATORS):
            if state.STATE not in closed:
                if function is 1:
                    print "The best state to traverse to with a g(n) = %d and h(n) = %d is..." % (state.DEPTH, 0)
                    printPuzzle(state.STATE)
                    print '          Traversing to this node...'
                    heappush(nodes, [state.DEPTH, state])
                elif function is 2:
                    print "The best state to traverse to with a g(n) = %d and h(n) = %d is..." % (state.DEPTH, state.MISPLACED)
                    printPuzzle(state.STATE)
                    print '          Traversing to this node...'
                    heappush(nodes, [state.MISPLACED + state.DEPTH, state])
                else:
                    print "The best state to traverse to with a g(n) = %d and h(n) = %d is..." % (state.DEPTH, state.MANHATTAN)
                    printPuzzle(state.STATE)
                    print '          Traversing to this node...'
                    heappush(nodes, [state.MANHATTAN + state.DEPTH, state])
                TOTAL_EXPANDED += 1
                MAX_QUEUE_SIZE += 1
            if problem.GOAL_TEST(state.STATE):
               # print 'depth is ' + str(node.DEPTH)
                return state, TOTAL_EXPANDED, MAX_QUEUE_SIZE
