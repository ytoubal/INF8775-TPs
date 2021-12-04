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
        node1.add_friend(node2.id)
        node2.add_friend(node1.id)     

    def show_graph(self):
        for node in self.nodes:
            print("Node: " + node.id)
            print("Height: " + str(node.height))
            print("Friends: " + str([node for node in node.friends]))
            print()

class Node:
    
    def __init__(self, id, height):
        self.id = id
        self.height = height
        self.friends = []

    def add_friend(self, node):
        self.friends.append(node)


def parse(instance_path):
    global graph
    
    graph = Graph()

    with open(instance_path, "r") as instance_file:
        number_students = instance_file.readline()
        number_friends = instance_file.readline()
        
        for i in range(int(number_students)):
            height = instance_file.readline()
            graph.add_node(Node(str(i+1), int(height))) #Ids start at 1
        
        for i in range(int(number_friends)):
            friends = instance_file.readline().split(" ")
            friend1 = int(friends[0])
            friend2 = int(friends[1])
            graph.add_edge(friend1, friend2)
        



