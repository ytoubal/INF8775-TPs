#!/usr/bin/env python3
import numpy as np


def parse(matrix1_path, matrix2_path):
    global matrix1, matrix2

    with open(matrix1_path, "r") as matrix1_file:
        N1 = matrix1_file.readline()
        matrix1 = [list(map(int,line.split())) for line in matrix1_file] 

    with open(matrix2_path, "r") as matrix2_file:
        N2 = matrix2_file.readline()
        matrix2 = [list(map(int,line.split())) for line in matrix2_file] 

    if (N1 != N2):
        quit("On ne peut pas multiplier des matrices de tailles differentes!")



