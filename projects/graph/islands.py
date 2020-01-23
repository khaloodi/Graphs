'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''

'''
Graphs problem solving steps:
1. translate the problem into graphs terminology
2. build your graph
3. traverse your graph
'''
from util import Stack, Queue

'''
ex:
graph_matrix[2][2]

north 
graph_matrix[1][2]

south
graph_matrix[3][2]

east
graph_matrix[2][3]

west
graph_matrix[2][1]
'''

def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # check north
    if y > 0 and graph_matrix[y-1][x] == 1: # y>0 goes first here b/c we're in the first or 0th row, and if it's not first we get an out of range/index error b/c we're checking the -1th row in matrix
        neighbors.append((x, y-1))
    # check south
    if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    # check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # check west
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors

def bft(x, y, matrix, visited):
    """
    Print each vertex in breadth-first order
    beginning from starting_vertex.
    """
    # Create an empty queue and enqueue the starting node/vertex
    q = Queue()
    q.enqueue((x, y))
    # Create an empty Set to store visited vertices
    # visited = set() # removed this line b/c apparently we're passing in our visited array
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first vertex
        v = q.dequeue()
        x = v[0] # think I could do x,y = v
        y = v[1]
        # If that vertext has not been visited...
        if not visited[y][x]:
            # Mark it as visited
            visited[y][x] = True
            # Then add all of its neighbors to the back of the queue
            for neighbor in get_neighbors((x, y), matrix): # STUB
                q.enqueue(neighbor)
    return visited


def island_counter(matrix):
    ### we're probably going to loop through the islands,
    ### do bfs on them and count how many times that bft occurs
    # create a visited matrix, gotta keep track b/c it's a cyclic graph
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0])) # creates 5 arrays of 5 falses each
    # create a counter, initialize to 0
    island_counter = 0
    # walk through each cell in the original matrix (we're gonna duplicate it)
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if it has not been visited...
            if not visited[y][x]: # note why these are switched to be (r, c) of matrix
            # if you reach a 1... 
                if matrix[y][x] == 1:
                    # do a BFT and mark each 1 as visited
                    visited = bft(x, y, matrix, visited)
                    # increment counter by 1
                    island_counter += 1
    return island_counter


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))
