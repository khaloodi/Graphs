from room import Room
from player import Player
from world import World
from graph import Graph

import random
from collections import deque
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#############################################################


def find_all_rooms(room_graph, starting_room):
    # # Initialize graph
    g = Graph()

    # Get verteces (rooms) from room_graph and add to our new graph
    verteces = [room for room in room_graph]
    for vertex in verteces:
        g.add_vertex(vertex)

    # Get edges (room connections) from room_graph and add to our new graph
    edges = [(room, room_graph[room][1]) for room in room_graph]
    print("edges: ", edges)
    for edge in edges:
        # print("edge: ", edge)
        for direction in ['n', 's', 'e', 'w']:
            if direction in edge[1]:
                # # print(edge[direction])
                g.add_edge(edge[0], edge[1][direction])
                # edge[1][direction] = '?'

    print("new graph: ", g.vertices)
    print("len(g.vertices): ", len(g.vertices))
    for i in range(len(g.vertices)):

        # print("g[i]: ", len(g.vertices[i]))
        # print("room_graph[i]: ", len(room_graph[i][1]))
        if len(g.vertices[i]) != len(room_graph[i][1]):
            print("I::::: ", i)
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # print("new edges: ", edges)
    print("len(room_graph): ", len(room_graph))
    print("room_graph: ", room_graph)
    # print(g.dft(0))
    # print(g.get_path(0))

    # def opposite_direction(dir):
    #     backwards_directions = {
    #         "n": "s",
    #         "s": "n",
    #         "w": "e",
    #         "e": "w"
    #     }
    #     return backwards_directions[dir]

    visited_rooms = set()
    stack = deque()
    # Choose the initial cell, mark it as visited and push it to the stack
    visited_rooms.add(starting_room)
    stack.append(starting_room)
    directions_list = []
    room_list = []
    room_directions_list = []
    # While the stack is not empty
    while len(stack) > 0:
        # Pop a cell from the stack and make it a current cell

        current = stack.pop()
        neighbors = g.get_neighbors(current)

        # print("current at start of each loop: ", current)
        # print("        v      ")
        room_list.append(current)
        unvisited_neighbors = []

        # print("neighbors: ", neighbors)
        for neighbor in neighbors:
            if neighbor not in visited_rooms:
                unvisited_neighbors.append(neighbor)

        # If the current cell has any neighbours which have not been visited
        # print(f"unvisited neighbors for {current}: ", unvisited_neighbors)
        if len(unvisited_neighbors) > 0:
            # Push the current cell to the stack
            stack.append(current)
            # get direction that matches room from original graph?
            for direction in room_graph[current][1]:
                # print("unvisited_neighbors[0]: ", unvisited_neighbors[0])
                # print("room_graph[current][1][direction]: ",
                #   room_graph[current][1][direction])
                if room_graph[current][1][direction] == unvisited_neighbors[0]:
                    directions_list.append(direction)

            # Choose one of the unvisited neighbours, mark it as visited and push it to the stack
            visited_rooms.add(unvisited_neighbors[0])
            stack.append(unvisited_neighbors[0])

            unvisited_neighbors.remove(unvisited_neighbors[0])
        else:

            for direction in room_graph[current][1]:
                if len(stack) > 0:
                    if room_graph[current][1][direction] == stack[-1]:
                        directions_list.append(direction)
    # print("room list: ", room_list)

    # Compare each item with the item in the graph
    for index in range(0, len(room_list) - 1):
        for direction in room_graph[room_list[index]][1]:
            # print("direction value: ",
            #       room_graph[room_list[index]][1][direction])
            # print("next room's id: ", room_list[index + 1])
            if room_graph[room_list[index]][1][direction] == room_list[index + 1]:
                # print("direction: ", direction)
                # print("match")
                room_directions_list.append(direction)
    # Find out which direction it connects with the next room
    # Write that direction in our list, one by one til we reach the end
    # print(directions_list)
    # print("room list: ", room_list)
    print("room directions list: ", room_directions_list)
    return room_directions_list


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = find_all_rooms(room_graph, 0)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# find_all_rooms(room_graph, 0)
