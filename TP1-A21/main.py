#!/usr/bin/env python3
import matrix_parser
import conventional
import argparse

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
    print(algorithm)
    print(path_matrix1)
    print(path_matrix2)
    print(show_result)
    print(show_time)

    matrix_parser.parse(r"C:\Users\yanis\Desktop\Poly\A2021\INF8775\TP1-A21\data\ex1_0",r"C:\Users\yanis\Desktop\Poly\A2021\INF8775\TP1-A21\data\ex1_1")
    print(matrix_parser.matrix1)
    print(matrix_parser.matrix2)

    if show_time:
        from timeit import default_timer as timer
        start = timer()

    result = conventional.multiply(matrix_parser.matrix1, matrix_parser.matrix2)

    if show_result:
        print(result)
    
    if show_time:
        end = timer()
        print("--- %s seconds ---" % (end - start))