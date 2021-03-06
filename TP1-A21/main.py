#!/usr/bin/env python3
import matrix_parser
import conventional
import argparse
import strassen
import strassen_seuil
import numpy as np
from timeit import default_timer as timer

def print_result(array):
    # Inspired by https://stackoverflow.com/questions/9360103/how-to-print-a-numpy-array-without-brackets/34833917
    """
    prints a 2-D numpy array without brackets
    """
    for a in array:
        print(' '.join(map(str, a)))

if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", required=True, type=str,
                        help="Represente l'algorithme a utiliser pour la multiplication de matrice")
    parser.add_argument("-e1", "--path_ex1", required=True, type=str,
                        help="Represente le chemin vers le fichier contenant la matrice 1")
    parser.add_argument("-e2", "--path_ex2", required=True, type=str,
                        help="Represente le chemin vers le fichier contenant la matrice 2")
    parser.add_argument("-p", "--show_result", required=False, default=False, action='store_true',
                        help="Represente s'il faut afficher la matrice resultant")
    parser.add_argument("-t", "--show_time", required=False, default=False, action='store_true',
                        help="Represente s'il faut afficher le temps d'execution")
    args = parser.parse_args()

    # Parameters
    algorithm = args.algorithm
    path_matrix1 = args.path_ex1
    path_matrix2 = args.path_ex2
    show_result = args.show_result
    show_time = args.show_time

    #Constructing the matrices
    matrix_parser.parse(path_matrix1, path_matrix2)

    if show_time:
        start = timer()

    if algorithm == "conv":
        result = conventional.multiply(matrix_parser.matrix1, matrix_parser.matrix2)
    elif algorithm == "strassen":
        result = strassen.strassen(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2))
    elif algorithm == "strassenSeuil":
        result = strassen_seuil.strassenSeuil(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2), 8)
    else:
        quit("L'algorithme en parametre n'est pas valide.")

    if show_result:
        print_result(result)

    if show_time:
        end = timer()
        print(1000*(end - start))
