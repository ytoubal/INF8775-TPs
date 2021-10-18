#!/usr/bin/env python3
import matrix_parser
import conventional
import argparse
import strassen
import strassen_sueil
import numpy as np
from timeit import default_timer as timer
import time


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

    # matrix_parser.parse(r"/Users/yacinehamdani/Desktop/SessionA21-etranger/cours/inf8775/TP1-A21/INF8775-TPs/TPs/TP1-A21/data/ex2_0",r"/Users/yacinehamdani/Desktop/SessionA21-etranger/cours/inf8775/TP1-A21/INF8775-TPs/Tps/TP1-A21/data/ex2_1")
    matrix_parser.parse(r"C:\Users\yanis\Desktop\Poly\A2021\INF8775\TPs\TP1-A21\data\ex8_0",r"C:\Users\yanis\Desktop\Poly\A2021\INF8775\TPs\TP1-A21\data\ex8_1")
    #print(matrix_parser.matrix1)
    #print(matrix_parser.matrix2)

    if show_time:
        start = timer()

    if algorithm == "conv":
        result = conventional.multiply(matrix_parser.matrix1, matrix_parser.matrix2)
        # result2 = strassen.strassen(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2))
        # print(result)
        # print(result2)
        # if (result == result2).all():
        #     print("MEME REPONSE")
        # else: 
        #     print("REPONSE DIFFERENTE")

    if algorithm == "strassen":
        result = strassen.strassen(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2))
    
    if algorithm == "strassenSeuil":
        #result1 = strassen.strassen(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2))
        result = strassen_sueil.strassenSeuil(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2), 60)

    if show_result:
        print(result)

    if show_time:
        end = timer()
        print("--- %s seconds ---" % (end - start))

# results = []
# for i in range(9):
#     start = timer()
#     strassen_sueil.strassenSeuil(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2), 2**i)
#     end = timer()
#     results.append(end-start)
#     print("--- %s seconds ---" % (end - start))
# index = results.index(min(results))
# print(results)
# print(2**index)
    

results = []
for i in range(3,9):
    for j in range(1,5):
        matrix_parser.parse(rf"C:\Users\yanis\Desktop\Poly\A2021\INF8775\TPS\TP1-A21\data\ex{i}_0",rf"C:\Users\yanis\Desktop\Poly\A2021\INF8775\TPS\TP1-A21\data\ex{i}_{j}")
        #print(f"Dimension: {i}, exemplaire: {0} multiply {j}")
        #start = timer()
        #start = time.perf_counter()
        #result = conventional.multiply(matrix_parser.matrix1, matrix_parser.#matrix2)
        #end = time.perf_counter()
        #end = timer()
        #print("conv")
        #print((end - start))

        # start = timer()
        # result = strassen.strassen(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2))
        # end = timer()
        # print("strassen")
        # print("--- %s seconds ---" % (end - start))

        # start = timer()
        # result = strassen_sueil.strassenSeuil(np.array(matrix_parser.matrix1), np.array(matrix_parser.matrix2), 8)
        # end = timer()
        # print("strassen seuil")
        # print("--- %s seconds ---" % (end - start))
        # print()

