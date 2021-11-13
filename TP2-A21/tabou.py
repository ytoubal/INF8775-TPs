import networkx as nx
import random
import glouton

ALPHA = 2
MAX_ITERATION = 500

def node_color_conflict(graph, node_recolor, new_color):
    total_conflicts = 0
    old_color = graph.nodes[node_recolor]["color"]
    graph.nodes[node_recolor]["color"] = new_color
    
    for node in graph.nodes:
        for neighbor in graph.neighbors(node):
            if graph.nodes[node]["color"] == graph.nodes[neighbor]["color"]:
                total_conflicts += 1
                   
    graph.nodes[node_recolor]["color"] = old_color

    return total_conflicts/2

def tabou_search(graph: nx.Graph, num_color, new_coloration, total_conflicts):
    tabou = {}
    tabou_expiration = {}
    best_coloration = [color for color in new_coloration]
    best_conflicts = total_conflicts
    #Generate neighbors
    colors = [i for i in range(num_color)]
    i = 0
    i_without_improv = 0

    while i_without_improv != MAX_ITERATION:
        
        lowest_conflict, best_neighbor = 999, (-1,-1)
        
        #generate neighbors
        for node in graph.nodes:
            for color in colors:
                valid_color = graph.nodes[node]["color"] != color and \
                           (node not in tabou or \
                            color not in tabou[node])
                if not valid_color: 
                    continue

                total_conflicts = node_color_conflict(graph, node, color)
                #Choose best neighbor
                if total_conflicts < lowest_conflict:
                    lowest_conflict = total_conflicts
                    best_neighbor = (node, color)

        #Update tabou list
        if lowest_conflict == 999:
            return True, []

        chosen_node = best_neighbor[0]
        old_color = graph.nodes[chosen_node]["color"]
        tabou_pair = (chosen_node, old_color)
        tabou.setdefault(chosen_node, []).append(old_color)
        expiration = i + (ALPHA * lowest_conflict + random.uniform(1, 11))
        tabou_expiration.setdefault(expiration, []).append(tabou_pair)

        #remove expired tabou pairs
        if i in tabou_expiration:
            pairs_to_remove = tabou_expiration[i]
            for pair in pairs_to_remove:
                tabou[pair[0]].remove(pair[1])
            del tabou_expiration[i]

        #update graph
        new_color = best_neighbor[1]
        graph.nodes[chosen_node]["color"] = new_color

        #Compare with best coloration
        if  lowest_conflict < best_conflicts:
            best_conflicts = lowest_conflict
            best_coloration = [graph.nodes[node]["color"] for node in graph.nodes]
            if best_conflicts == 0:
                return False, best_coloration
            i_without_improv = 0
        else:
            i_without_improv += 1

        i += 1
    return True, []

def evaluate_node_conflict(graph, node_recolor, color):
    
    num_conflicts = 0
    for neighbor in graph.neighbors(node_recolor):
        if graph.nodes[neighbor]["color"] == color:
            num_conflicts += 1
    return num_conflicts

def evaluate_conflicts(graph, nodes, max_color):
    lowest_conflicts = {}
    total_conflicts = 0

    for node_recolor in nodes:
        curr_lowest_conflict, curr_best_color = 9999, -1
        for color in range(max_color): # check all colors except k-1
            num_conflicts = evaluate_node_conflict(graph, node_recolor, color)
            
            if num_conflicts < curr_lowest_conflict:
                curr_lowest_conflict = num_conflicts
                curr_best_color = color
                   
        lowest_conflicts[node_recolor] = curr_best_color
        total_conflicts += curr_lowest_conflict

    return lowest_conflicts, total_conflicts

def reduce_num_colors(graph: nx.Graph, solution):
    max_color = max(solution) # color k-1
    nodes_max_color = [str(i+1) for i, color in enumerate(solution) if color == max_color] #Nodes containing highest color
    
    lowest_conflicts, total_conflicts = evaluate_conflicts(graph, nodes_max_color, max_color)

    new_solution = [color for color in solution]
    for node, color in lowest_conflicts.items():
        new_solution[int(node)-1] = color #index of node is node-1
    return new_solution, total_conflicts

def find_colors(graph: nx.Graph):

    s0 = glouton.find_colors(graph) # intial solution
    num_color = max(s0) + 1
    best_solution = s0 #C*

    while True:
        new_coloration, total_conflicts = reduce_num_colors(graph, best_solution)
        num_color -= 1

        #Set graph colors to new coloration
        for index, color in enumerate(new_coloration):
            graph.nodes[str(index+1)]["color"] = color
        
        if total_conflicts == 0:
            better_solution = new_coloration
        else:
            #Fix conflicts
            stop_algo, better_solution = tabou_search(graph, num_color, new_coloration, total_conflicts) 

            if stop_algo:
                break
        best_solution = better_solution

    return best_solution