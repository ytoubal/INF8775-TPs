import common

def find_smallest_color(node):
    colors_taken = [adj_node.color for adj_node in node.neighbors]
    max_color = max(colors_taken)
    for i in range(max_color+1):
        if i not in colors_taken:
            return i
    return max_color + 1

def find_colors(graph):
    first_node = common.find_first_node(graph)
    first_node.set_color(0) # C[v] = 0
    
    while not common.check_nodes_colored(graph):
        chosen_node = common.glouton_choice(graph)
        color = find_smallest_color(chosen_node)
        chosen_node.set_color(color)

    return [node.color for node in graph.nodes]