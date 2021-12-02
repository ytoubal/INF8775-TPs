#!/usr/bin/env python3
import graph_parser
from graph_parser import Node
import argparse
import operator
import math
from timeit import default_timer as timer
import last_vegas1
import last_vegas2
import last_vegas3

#branch and bound
# def hamiltonianPaths(graph, v, visited, path, n):
 
#     # if all the vertices are visited, then the Hamiltonian path exists
#     if len(path) == n:
#         # print the Hamiltonian path
#         print(path)
#         return
 
#     # Check if every edge starting from vertex `v` leads to a solution or not
#     for friend_id in graph.nodes[v-1].friends:
#         friend_idx = int(friend_id) -1
#         # process only unvisited vertices as the Hamiltonian
#         # path visit each vertex exactly once
#         if not visited[friend_idx]:
#             visited[friend_idx] = True
#             path.append(friend_id)
 
#             # check if adding vertex `w` to the path leads to the solution or not
#             hamiltonianPaths(graph, int(friend_id), visited, path, n)
 
#             # backtrack
#             visited[friend_idx] = False
#             path.pop()
 
 
# def findHamiltonianPaths(graph, n):
#     sorted_height = sorted(graph.nodes, key=lambda x: x.height)
#     # start with every node
#     for i in range(n):
 
#         # add starting node to the path
#         path = [str(i+1)]
    
#         # mark the start node as visited
#         visited = [False] * n
#         visited[i] = True
    
#         hamiltonianPaths(graph, i+1, visited, path, n)

def find_conflicts(path):
    if len(path) == 0:
        return 9999
    max_height = -1
    number_conflicts = 0
    for student in path:
        if student.height >= max_height:
            max_height = student.height
        else:
            number_conflicts += 1 
    
    return number_conflicts


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--path_ex", required=True, type=str,
                        help="Represente le chemin vers le fichier contenant lexemplaire")
    parser.add_argument("-p", "--show_result", required=False, default=False, action='store_true',
                        help="Represente s'il faut la solution")
    args = parser.parse_args()

    # Parameters
    path_graph = args.path_ex
    show_result = args.show_result

    #Constructing the matrices
    graph_parser.parse(path_graph)
    
    
    #while True:
    start = timer()
    best_conflicts = 999
    result_ids = None
    
    while timer() - start < 180:
        
        #result = last_vegas1.algo(graph_parser.graph, start)
        result = last_vegas2.algo(graph_parser.graph, start)
        if result == None:
            break
        number_conflicts = find_conflicts(result)
        if number_conflicts < best_conflicts:
            result_ids = [student.id for student in result]
            best_conflicts = number_conflicts
        #print("Conflits: " + str(number_conflicts))
    end = timer()
    print(end - start)
    print(best_conflicts)


    if show_result:
        if result_ids != None:
            print(*result_ids)
            #sorted_height = sorted(graph_parser.graph.nodes, key=lambda x: x.height)
            #print(*[s.id for s in sorted_height])
        #else:
            #print(str(number_conflicts))
