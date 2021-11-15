#!/usr/bin/env python3

class Graph:

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1_id, node2_id):
        #Index is id-1 since id start at 1
        node1 = self.nodes[node1_id-1]
        node2 = self.nodes[node2_id-1]
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)     

    def evaluate_num_conflicts(self):
        total_conflicts = 0
        for node in graph.nodes:
            for neighbor in node.neighbors:
                if node.color != -1 and \
                   neighbor.color != -1 and \
                   node.color == neighbor.color:
                   total_conflicts += 1
                    
        return total_conflicts/2

    def show_graph(self):
        for node in self.nodes:
            print("Node: " + node.id)
            print("Color: " + str(node.color))
            print("Degree: " + str(node.get_degree()))
            print("Neighbors: " + str([node.id for node in node.neighbors]))
            print()


class Node:
    
    def __init__(self, id, color = -1):
        self.id = id
        self.color = color
        self.neighbors = []

    def set_color(self, color):
        self.color = color

    def add_neighbor(self, node):
        self.neighbors.append(node)
    
    def remove_neighbor(self, node):
        self.neighbors.remove(node)

    # def evaluate_color_conflict(self, color):
    #     num_conflicts = 0
    #     for neighbor in self.neighbors:
    #         if neighbor.color == color:
    #             num_conflicts += 1
    #     return num_conflicts

    def get_degree(self):
        return len(self.neighbors)

    def find_DSAT(self):
        return sum(1 for node in self.neighbors if node.color != -1)


def parse(matrix_path):
    global graph

    graph = Graph()

    with open(matrix_path, "r") as matrix_file:
        #Skip 11 first lines which arent important
        #Inspired by https://stackoverflow.com/questions/9578580/skip-first-couple-of-lines-while-reading-lines-in-python-file
        for _ in range(11):
            next(matrix_file)
        info_graph = matrix_file.readline().split(' ')
        number_node = info_graph[2]

        for i in range(int(number_node)):
            graph.add_node(Node(str(i+1))) #Nodes start at 1
        
        next(matrix_file)

        for line in matrix_file: 
            info_edge = line.strip('\n').split(' ')
            edge1 = int(info_edge[1])
            edge2 = int(info_edge[2])
            graph.add_edge(edge1, edge2)
        



