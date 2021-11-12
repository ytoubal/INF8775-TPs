#!/usr/bin/env python3
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def parse(matrix_path):
    global graph

    graph = nx.Graph()

    with open(matrix_path, "r") as matrix_file:
        #Skip 11 first lines which arent important
        #Inspired by https://stackoverflow.com/questions/9578580/skip-first-couple-of-lines-while-reading-lines-in-python-file
        for _ in range(11):
            next(matrix_file)
        info_graph = matrix_file.readline().split(' ')
        number_node = info_graph[2]
        number_edge = info_graph[3]
        # print(number_vertex)
        # print(number_edge)
        graph.add_nodes_from([str(i+1) for i in range(int(number_node))], color=-1) # no color for each node
        next(matrix_file)

        for line in matrix_file: 
            info_edge = line.strip('\n').split(' ')
            edge1 = info_edge[1]
            edge2 = info_edge[2]
            # print(info_edge)
            graph.add_edge(edge1, edge2)
        # print(graph.nodes)
        # print(graph.edges)
        nx.draw_networkx(graph, with_labels=True)
        #plt.show()
    


