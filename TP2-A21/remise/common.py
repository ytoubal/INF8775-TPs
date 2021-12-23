def find_first_node(graph):
    nodes_degree = [node.get_degree() for node in graph.nodes]
    max_degree_node = nodes_degree.index(max(nodes_degree)) # v
    return graph.nodes[max_degree_node]

def check_nodes_colored(graph):
    for node in graph.nodes:
        if node.color == -1:
            return False
    return True    

def glouton_choice(graph):
    max_DSAT, dsat_nodes = find_DSAT(graph)
    potential_nodes = [graph.nodes[i] for i, dsat in enumerate(dsat_nodes) if dsat == max_DSAT]

    max_deg, best_node = -1, None
    for node in potential_nodes:
        degree = node.get_degree()
        if degree > max_deg:
            max_deg = degree
            best_node = node
    
    return best_node    


def find_DSAT(graph):
    max_dsat, dsat_nodes = -1, []
    for node in graph.nodes:
        if node.color != -1:
            dsat_nodes.append(0)
            continue
        
        dsat = 0
        for adj_node in node.neighbors:
            if adj_node.color != -1:
                dsat += 1

        dsat_nodes.append(dsat)
        if dsat > max_dsat:
            max_dsat = dsat
            
    return max_dsat, dsat_nodes