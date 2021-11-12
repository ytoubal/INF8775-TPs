#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt

def check_nodes_colored(graph: nx.Graph):
    for node in graph.nodes:
        if graph.nodes[node]["color"] == -1:
            return False
    return True

def find_DSAT(graph: nx.Graph):
    max_dsat, max_dsat_node = -1, None
    for node in graph.nodes:
        if graph.nodes[node]["color"] != -1:
            continue
        dsat = 0
        for adj_node in graph.neighbors(node):
            if graph.nodes[adj_node]["color"] != -1:
                dsat += 1
        if dsat > max_dsat:
            max_dsat = dsat
            max_dsat_node = node   # À voir si on garde node
            
    return max_dsat_node

def find_smallest_color(node, graph: nx.graph, current_color = 0):
    colors_taken = []   
    for adj_node in graph.neighbors(node):
        colors_taken.append(graph.nodes[adj_node]["color"])
        if graph.nodes[adj_node]["color"] == current_color:
            current_color = find_smallest_color(node, graph, current_color + 1)
    return current_color

def find_colors(graph: nx.Graph):
    max_degree_node = max(graph.degree, key=lambda x: x[1])[0] # v
    graph.nodes[max_degree_node]["color"] = 0 # C[v] = 0

    while not check_nodes_colored(graph):
        chosen_node = find_DSAT(graph)
        color = find_smallest_color(chosen_node, graph)
        graph.nodes[chosen_node]["color"] = color

    #print(graph.nodes.data())
    #plt.show()
    return