#!/usr/bin/env python3

def check_nodes_colored(graph):
    for node in graph.nodes:
        if node.color == -1:
            return False
    return True

def find_DSAT(graph):
    max_dsat, max_dsat_node = -1, None
    for node in graph.nodes:
        if node.color != -1:
            continue
        dsat = 0
        for adj_node in node.neighbors:
            if adj_node.color != -1:
                dsat += 1
        if dsat > max_dsat:
            max_dsat = dsat
            max_dsat_node = node   
            
    return max_dsat_node

def find_smallest_color(node):
    colors_taken = [adj_node.color for adj_node in node.neighbors]
    max_color = max(colors_taken)
    for i in range(max_color+1):
        if i not in colors_taken:
            return i
    return max_color + 1

def find_colors(graph):
    nodes_degree = [node.get_degree() for node in graph.nodes]
    max_degree_node = nodes_degree.index(max(nodes_degree)) # v
    graph.nodes[max_degree_node].set_color(0) # C[v] = 0

    while not check_nodes_colored(graph):
        chosen_node = find_DSAT(graph)
        color = find_smallest_color(chosen_node)
        chosen_node.set_color(color)

    return [node.color for node in graph.nodes]