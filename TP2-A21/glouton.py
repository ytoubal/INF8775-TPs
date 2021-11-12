<<<<<<< HEAD
#!/usr/bin/env python3

import matrixparser
import node

matrix = matrixparser.parse("/Users/yacinehamdani/Desktop/SessionA21-etranger/cours/inf8775/TP1-A21/INF8775-TPs/TP2-A21/instances/ex5_0")
node1 = node.Node(None, None, None)


              


def chooseFirstPoint():
       node1.calculateDegree(matrix)


node1.calculateDegree(matrix)
=======
# def find_max_degree(matrix):
#     max_val, max_index = -1, -1
#     for index, row in enumerate(matrix):
#         row_deg = sum(row)
#         if row_deg > max_val:
#             max_val, max_index = row_deg, index
#     return max_index

# def glutton_choice(matrix, uncolored_vertex, colored_vertex):
#     max_val, max_index = -1, -1
#     for index, vertex in enumerate(uncolored_vertex):
#         dsat = 0
#         for num, connection in enumerate(matrix[vertex]):
#             if connection == 1 and colored_vertex[num] != -1:
#                 dsat += 1
#         if dsat > max_val:
#             max_val, max_index = dsat, index
#     return max_index

# def choose_smallest_color():


def find_colors(matrix):
     return
#     #All the vertex are not colored
#     C = [-1 for _ in range(len(matrix))]
#     uncolored_vertex = [i for i in range(len(matrix))]
#     index_max_deg = find_max_degree(matrix)
#     next_color = 0
#     C[index_max_deg] = next_color
#     next_color += 1
#     print("Chosen vertex: " + str(uncolored_vertex[index_max_deg]))
#     uncolored_vertex.pop(index_max_deg)
    
#     while len(uncolored_vertex) > 0:
#         V = glutton_choice(matrix, uncolored_vertex, C)
#         print("Chosen vertex: " + str(uncolored_vertex[V]))
#         C[uncolored_vertex[V]] = next_color
#         next_color += 1
#         uncolored_vertex.pop(V)
#     return
>>>>>>> 4452e322569673e7e2db0c751ab3eca700cf6a17
