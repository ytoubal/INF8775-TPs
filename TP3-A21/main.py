#!/usr/bin/env python3
#import instance_parser
import graph_parser
from graph_parser import Node
import argparse
import operator
import math
import random
from timeit import default_timer as timer

# def algo(students):
#     students_list = students[:]
#     best_solution = []
#     number_conflicts = 0
#     #https://stackoverflow.com/questions/6085467/python-min-function-with-a-list-of-objects
#     first_student = min(students_list, key = operator.attrgetter('height'))
#     best_solution.append(first_student.id)
#     students_list.remove(first_student)
    
#     while len(best_solution) != len(students):
#         selected_student = None
#         selected_height = 999999
#         neighbor_front = best_solution[-1]
#         for i in range(len(students_list)):
#             current_student = students_list[i]
            
#             if current_student.is_friend(neighbor_front) and current_student.height < selected_height:
#                 selected_student = current_student
#                 selected_height = current_student.height
        
#         if selected_student != None:
#             best_solution.append(selected_student.id)
#             students_list.remove(selected_student)
#         else:
#             print(len(best_solution))
#             print("Student not found")
    
#     return best_solution, number_conflicts

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
    max_height = -1
    number_conflicts = 0
    for student in path:
        if student.height >= max_height:
            max_height = student.height
        else:
            number_conflicts += 1 
    
    return number_conflicts

def algo(graph):
    index = 0
    sorted_height = sorted(graph.nodes, key=lambda x: x.height)
    first_node = sorted_height[index]
    path = [first_node]
    
    while True:
        potential_path = extension(graph, path)
        if potential_path != None:
            #print(len(path))
            path = potential_path
            continue
        
        new_paths = posa_extension(graph, path)
        for new_path in new_paths:
            potential_path = extension(graph, new_path)
            if potential_path != None:
                #print(len(path))
                path = potential_path
                continue
        
        if len(path) == len(graph.nodes):
            print("Solution found")
            return path
        else:
            #print("Solution not found")
            #print(len(path))
            index += 1
            first_node = sorted_height[index]
            path = [first_node]
        #break
        
def extension(graph, path):
    path_start = path[0]
    path_end = path[-1]
    for node in graph.nodes:
        if node in path: continue
        
        if node.id in path_start.friends:
            path.insert(0, node)
            return path
        elif node.id in path_end.friends:
            path.append(node)
            return path
    return None
      
#Inspired by https://reader.elsevier.com/reader/sd/pii/S0012365X06005097?token=1EFA63B2236734161C96D4107EDADB47136DA535E4DC2EA105CF1610A3E397EA0364668E7DE92464560ADA64D0026AD9&originRegion=us-east-1&originCreation=20211129221424
def posa_extension(graph, path):
    extensions = []
    
    for friend_idx in path[-1].friends: #find the friends of the last node
        friend = graph.nodes[int(friend_idx)-1]
        if friend in path: #if friend is in the current path we can form a new path
            index = path.index(friend)
            changed_path = path[index+1:]
            changed_path.reverse()
            new_path = path[:index+1] + changed_path
            extensions.append(new_path)
    return extensions

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
    # graph = graph_parser.graph
    # path = [graph.nodes[0], graph.nodes[9], graph.nodes[30], graph.nodes[25], graph.nodes[20], graph.nodes[5]]
    # graph.nodes[5].friends = ["31", "26"]
    # result1 = posa_extension(graph, path)
    # print(len(result1))
    # print([node.id for node in result1[0]])
    # print([node.id for node in result1[1]])
    # result = []
    result = algo(graph_parser.graph)
    result_ids = [student.id for student in result]
    # path = [Node("0", 10), Node("0", 1), Node("0", 2), Node("0", 4), Node("0", 11), Node("0", 5), Node("0", 20)]
    number_conflicts = find_conflicts(result)
    print("Conflits: " + str(number_conflicts))
    end = timer()
    print(end - start)

    if show_result:
        print(*result_ids)
        #else:
            #print(str(number_conflicts))
