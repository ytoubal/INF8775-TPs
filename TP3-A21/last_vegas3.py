# 66_99.0 #63 62 fail
# 66_99.1 #fail fail fail   
# 66_534.0 #62 59 53
# 66_534.1 #61 61 54
# 66_970.0 #58 61 53
# 66_970.1 #62 63 55

# 118_178.0 #fail fail  
# 118_178.1 #fail fail
# 118_1570.0 #112 111 105
# 118_1570.1 #108 112 110
# 118_2962.0 #113 111 106
# 118_2962.1 #113 116 108

# 558_837.0 #fail fail 
# 558_837.1 #fail fail
# 558_31973.0 #551 548 550
# 558_31973.1 #549 550 550
# 558_63109.0 #553 551 549
# 558_63109.1 #547 552 549

import random
from timeit import default_timer as timer

def find_conflicts(path):
    max_height = -1
    number_conflicts = 0
    for student in path:
        if student.height >= max_height:
            max_height = student.height
        else:
            number_conflicts += 1 
    
    return number_conflicts

def algo(graph, start):
    #index = 0
    #sorted_height = sorted(graph.nodes, key=lambda x: x.height)
    first_node = random.choice(graph.nodes)
    path = [first_node]
    potential_paths = [path]
    solution = []
    best_conflict = 999
    
    while timer() - start < 180:
        potential_path = extension(graph, path)
        if potential_path != None:
            potential_paths.remove(path)
            path = random.choice(potential_path)
            potential_paths.extend(potential_path)
            continue
        
        new_paths = posa_extension(graph, path)
        # for new_path in new_paths:
        potential_paths.extend(new_paths)
        potential_paths.remove(path)
        path = random.choice(new_paths)
        potential_path = extension(graph, path)
        if potential_path != None:
                #print(len(path))
            potential_paths.remove(path)
            path = random.choice(potential_path)
            potential_paths.extend(potential_path)
            continue
        
        if len(path) == len(graph.nodes):
            #print("Solution found")
            conflicts = find_conflicts(path)
            if conflicts < best_conflict:
                solution = path
                best_conflict = conflicts
            potential_paths.remove(path)
            #print("Solution not found")
            #print(len(path))
            #index += 1
            # if index == len(graph.nodes):
            #     print("Solution not found")
            #     break
        
        if len(potential_paths) > 0:
            path = random.choice(potential_paths)
        else:
            first_node = random.choice(graph.nodes)
            path = [first_node]
            potential_paths = [path]
        #break
    return solution
        
def extension(graph, path):
    path_start = path[0]
    path_end = path[-1]
    for node in graph.nodes:
        if node in path: continue
        new_paths = []
        if node.id in path_end.friends:
            new_path = path[:]
            new_path.append(node)
            new_paths.append(new_path)
        if node.id in path_start.friends:
            new_path = path[:]
            new_path.insert(0, node)
            new_paths.append(new_path)
        
        if len(new_paths) > 0:
            return new_paths
    return None
      
#Inspired by https://reader.elsevier.com/reader/sd/pii/S0012365X06005097?token=1EFA63B2236734161C96D4107EDADB47136DA535E4DC2EA105CF1610A3E397EA0364668E7DE92464560ADA64D0026AD9&originRegion=us-east-1&originCreation=20211129221424
def posa_extension(graph, path):
    extensions = []
    
    for friend_id in path[-1].friends: #find the friends of the last node
        friend = graph.nodes[int(friend_id)-1]
        if friend in path: #if friend is in the current path we can form a new path
            index = path.index(friend)
            changed_path = path[index+1:]
            changed_path.reverse()
            new_path = path[:index+1] + changed_path
            extensions.append(new_path)
    return extensions