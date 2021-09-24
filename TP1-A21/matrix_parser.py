#!/usr/bin/env python3
import numpy as np


def parse(matrix1_path, matrix2_path):
    global matrix1, matrix2

    with open(matrix1_path, "r") as matrix1_file:
        N1 = matrix1_file.readline()
        matrix1 = [list(map(int,line.split())) for line in matrix1_file] # À REVOIR

    with open(matrix2_path, "r") as matrix2_file:
        N2 = matrix2_file.readline()
        matrix2 = [list(map(int,line.split())) for line in matrix2_file] # À CHANGER

    if (N1 != N2):
        quit("Can't multiply the matrices since they don't have the same dimensions")



