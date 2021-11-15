import common
import glouton

def explore_coloration(graph, coloration, number_color):
    colorations = []
    for i, color in enumerate(coloration):
        graph.nodes[i].set_color(color)
    chosen_node = common.glouton_choice(graph)
    chosen_node_index = int(chosen_node.id) -1 
    for color in range(number_color+1):
        chosen_node.set_color(color)
        #print(graph.evaluate_num_conflicts())
        new_coloration = coloration[:]
        new_coloration[chosen_node_index] = color
        #print(new_coloration)
        if graph.evaluate_num_conflicts() == 0:
            new_coloration = coloration[:]
            new_coloration[chosen_node_index] = color
            colorations.append(new_coloration)
        chosen_node.set_color(-1)
    return colorations

def find_colors(graph):
    best_solution = glouton.find_colors(graph) # initial solution
    best_solution_cost = max(best_solution) + 1 #upper bound, number of colors
    node_stack = []
    C = [-1 for _ in graph.nodes]
    first_node = common.find_first_node(graph)
    C[int(first_node.id)-1] = 0 #index of node is node.id -1
    node_stack.append(C)

    while len(node_stack) > 0:
        current_coloration = node_stack.pop()
        current_solution_cost = max(current_coloration) +1 

        if -1 not in current_coloration:
            if current_solution_cost < best_solution_cost:
                best_solution = current_coloration
                best_solution_cost = current_solution_cost
        elif current_solution_cost < best_solution_cost:
            for coloration in explore_coloration(graph, current_coloration, current_solution_cost):
                node_stack.append(coloration)

    return best_solution 