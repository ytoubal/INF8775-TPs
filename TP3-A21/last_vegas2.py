# 66_99.0 #fail
# 66_99.1 #fail
# 66_534.0 #54
# 66_534.1 #54
# 66_970.0 #56
# 66_970.1 #56

# 118_178.0 #fail
# 118_178.1 #fail
# 118_1570.0 #106
# 118_1570.1 #102
# 118_2962.0 #110
# 118_2962.1 #110

# 558_837.0 #fail   
# 558_837.1 #fail
# 558_31973.0 #fail
# 558_31973.1 #fail
# 558_63109.0 #550
# 558_63109.1 #549

import random
from timeit import default_timer as timer

def algo(graph, start):
    #index = 0
    #sorted_height = sorted(graph.nodes, key=lambda x: x.height)
    first_node = random.choice(graph.nodes)
    path = [first_node]
    
    while timer() - start < 180:
        potential_path = extension(graph, path)
        if potential_path != None:
            #print(len(path))
            path = potential_path
            continue
        
        new_paths = posa_extension(graph, path)
        # for new_path in new_paths:
        new_path = random.choice(new_paths)
        potential_path = extension(graph, new_path)
        if potential_path != None:
                #print(len(path))
            path = potential_path
            continue
        
        if len(path) == len(graph.nodes):
            #print("Solution found")
            return path
        else:
            #print("Solution not found")
            #print(len(path))
            #index += 1
            # if index == len(graph.nodes):
            #     print("Solution not found")
            #     break
            first_node = random.choice(graph.nodes)
            path = [first_node]
        #break
        
def extension(graph, path):
    path_start = path[0]
    path_end = path[-1]
    for node in graph.nodes:
        if node in path: continue

        if node.id in path_end.friends:
            path.append(node)
            return path
        if node.id in path_start.friends:
            path.insert(0, node)
            return path
        
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