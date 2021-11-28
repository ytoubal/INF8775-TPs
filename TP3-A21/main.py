#!/usr/bin/env python3
import instance_parser
import argparse

if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--path_ex", required=True, type=str,
                        help="Represente le chemin vers le fichier contenant lexemplaire")
    parser.add_argument("-p", "--show_result", required=False, default=False, action='store_true',
                        help="Represente s'il faut la solution")
    args = parser.parse_args()

    # Parameters
    path_graph = args.path_ex
    show_result = args.show_result

    #Constructing the matrices
    instance_parser.parse(path_graph)
    result = []

    if show_result:
        print(*result)
