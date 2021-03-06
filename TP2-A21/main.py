#!/usr/bin/env python3
import graph_parser
import argparse
from timeit import default_timer as timer
import glouton
import branch_and_bound
import tabou

if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", required=True, type=str,
                        help="Represente l'algorithme a utiliser pour la multiplication de matrice")
    parser.add_argument("-e", "--path_ex", required=True, type=str,
                        help="Represente le chemin vers le fichier contenant lexemplaire")
    parser.add_argument("-p", "--show_result", required=False, default=False, action='store_true',
                        help="Represente s'il faut afficher le nombre et les couleurs")
    parser.add_argument("-t", "--show_time", required=False, default=False, action='store_true',
                        help="Represente s'il faut afficher le temps d'execution")
    args = parser.parse_args()

    # Parameters
    algorithm = args.algorithm
    path_graph = args.path_ex
    show_result = args.show_result
    show_time = args.show_time

    #Constructing the matrices
    graph_parser.parse(path_graph)

    if show_time:
        start = timer()

    if algorithm == "glouton":
        result = glouton.find_colors(graph_parser.graph)
    elif algorithm == "branch_bound":
       result = branch_and_bound.find_colors(graph_parser.graph)
    elif algorithm == "tabou":
        result = tabou.find_colors(graph_parser.graph)
    else:
        quit("L'algorithme en parametre n'est pas valide.")

    if show_result:
        print(max(result)+1)
        print(*result)

    if show_time:
        end = timer()
        print(1000*(end - start))
