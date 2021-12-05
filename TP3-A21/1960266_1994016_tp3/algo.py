import random
import sys

#Print the best current solution 
def print_solution(show_result, solution, conflicts):
    
    if show_result:
        solution_ids = [student.id for student in solution]
        print(*solution_ids, flush=True)
    else:
        print(conflicts, flush=True)
    sys.stdout.flush()

#Count the number of conflicts of a solution
def calculate_conflicts(path):
    max_height = -1
    number_conflicts = 0

    for student in path:
        if student.height >= max_height: #current student is taller or equal to the previous taller student
            max_height = student.height
        else:
            number_conflicts += 1 
    
    return number_conflicts

#Algorithm 
def find_result(graph, show_result):
    first_node = random.choice(graph.nodes)
    path = [first_node]
    potential_paths = [path]
    solution = []
    best_conflict = 999
    
    while True:
       
        #We check if we can extend the current path
        extended_paths = extension(graph, path)
        if extended_paths != None:
            path = update_path(path, extended_paths, potential_paths)
            continue
        
        #We cant no longer extend the current path so we apply a posa extension to generate new paths
        new_paths = posa_rotation(graph, path)
        potential_paths.extend(new_paths)
        potential_paths.remove(path)
        path = random.choice(new_paths)

        #We check if we can extend the current path generate by the posa extension
        extended_paths = extension(graph, path)
        if extended_paths != None:
            path = update_path(path, extended_paths, potential_paths)
            continue
        
        #Solution found
        if len(path) == len(graph.nodes):
            conflicts = calculate_conflicts(path)
            if conflicts < best_conflict:
                solution = path
                best_conflict = conflicts
                print_solution(show_result, solution, best_conflict)
            potential_paths.remove(path)
        
        #Visit other paths or finish the algorithm
        if len(potential_paths) > 0:
            path_idx = find_longest_path(potential_paths)
            path = potential_paths[path_idx]
        else:
            break

#Update potential paths and return a new path to follow
def update_path(path, extended_paths, potential_paths):
    potential_paths.extend(extended_paths)
    potential_paths.remove(path)
    
    return random.choice(extended_paths)

#Find and select the longest potential path 
def find_longest_path(potential_paths):
    path_max = [len(p) for p in potential_paths]
    return path_max.index(max(path_max))

#If possible extend the current path from the start or the end
def extension(graph, path):
    node_start = path[0]
    node_end = path[-1]
    
    #friends that are not currently in the path that can be attached to the start node/end node
    node_start_possible = [graph.nodes[int(friend_id)-1] for friend_id in node_start.friends if graph.nodes[int(friend_id)-1] not in path] 
    node_end_possible = [graph.nodes[int(friend_id)-1] for friend_id in node_end.friends if graph.nodes[int(friend_id)-1] not in path] 

    if len(node_start_possible) == 0 and len(node_end_possible) == 0:
        return None

    new_paths = []
    for friend in node_start_possible:
        new_path = path[:]
        new_path.insert(0, friend) #friend becomes the first node of the path
        new_paths.append(new_path)
    
    for friend in node_end_possible:
        new_path = path[:]
        new_path.append(friend) #friend becomes the last node of the path
        new_paths.append(new_path)
    
    return new_paths
      
#Inspired by https://reader.elsevier.com/reader/sd/pii/S0012365X06005097?token=1EFA63B2236734161C96D4107EDADB47136DA535E4DC2EA105CF1610A3E397EA0364668E7DE92464560ADA64D0026AD9&originRegion=us-east-1&originCreation=20211129221424
#If possible apply a rotation of the last node and its friends already in the path
#Mecanism to escape a path that we can no longer escape 
def posa_rotation(graph, path):
    extensions = []
    
    for friend_id in path[-1].friends: #find the friends of the last node
        friend = graph.nodes[int(friend_id)-1]

        if friend in path: #if friend is in the current path we can form a new path
            index = path.index(friend)

            #we reverse the order of the nodes between the friend and the last node
            changed_path = path[index+1:] 
            changed_path.reverse()

            #we form a new path with the rotation of the friend and the last node
            new_path = path[:index+1] + changed_path
            extensions.append(new_path)

    return extensions