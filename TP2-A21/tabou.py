import random
import glouton

ALPHA = 2
MAX_ITERATION = 1500

def tabou_search(graph, num_color, new_coloration, total_conflicts):
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
                valid_color = node.color != color and \
                           (node.id not in tabou or \
                            color not in tabou[node.id])
                if not valid_color: 
                    continue

                old_color = node.color
                node.color = color
                total_conflicts = graph.evaluate_num_conflicts()
                node.color = old_color

                #Choose best neighbor
                if total_conflicts < lowest_conflict:
                    lowest_conflict = total_conflicts
                    best_neighbor = (node, color)

        #Update tabou list
        if lowest_conflict == 999:
            return True, []

        chosen_node = best_neighbor[0]
        old_color = chosen_node.color
        tabou_pair = (chosen_node, old_color)
        tabou.setdefault(chosen_node.id, []).append(old_color)
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
        chosen_node.color = new_color

        #Compare with best coloration
        if  lowest_conflict < best_conflicts:
            best_conflicts = lowest_conflict
            best_coloration = [node.color for node in graph.nodes]
            if best_conflicts == 0:
                return False, best_coloration
            i_without_improv = 0
        else:
            i_without_improv += 1

        i += 1
    return True, []

def evaluate_conflicts(graph, nodes, max_color): 
    lowest_conflicts = {}
    total_conflicts = 0

    #nodes has index of the node
    for node_recolor in nodes:
        curr_lowest_conflict, curr_best_color = 9999, -1

        for color in range(max_color): # check all colors except k-1
            old_color = node_recolor.color
            node_recolor.set_color(color)
            num_conflicts = graph.evaluate_num_conflicts()
            node_recolor.set_color(old_color)
            
            if num_conflicts < curr_lowest_conflict:
                curr_lowest_conflict = num_conflicts
                curr_best_color = color

        node_recolor_index = int(node_recolor.id) -1
        lowest_conflicts[node_recolor_index] = curr_best_color
        total_conflicts += curr_lowest_conflict

    return lowest_conflicts, total_conflicts

def reduce_num_colors(graph, solution, num_color): 
    max_color = num_color-1
    nodes_max_color = [graph.nodes[i] for i, color in enumerate(solution) if color == max_color] #Nodes containing highest color
    
    lowest_conflicts, total_conflicts = evaluate_conflicts(graph, nodes_max_color, max_color)

    new_solution = [color for color in solution]
    for node, color in lowest_conflicts.items():
        new_solution[node] = color 
    return new_solution, total_conflicts

def find_colors(graph):

    best_solution = glouton.find_colors(graph) # initial solution
    num_color = max(best_solution) + 1

    while True:
        new_coloration, total_conflicts = reduce_num_colors(graph,best_solution, num_color)
        num_color -= 1

        #Set graph colors to new coloration
        for index, color in enumerate(new_coloration):
            graph.nodes[index].color = color
        
        if total_conflicts == 0:
            better_solution = new_coloration
        else:
            #Fix conflicts
            stop_algo, better_solution = tabou_search(graph, num_color, new_coloration, total_conflicts) 

            if stop_algo:
                break
        best_solution = better_solution

    return best_solution