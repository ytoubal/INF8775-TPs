#!/usr/bin/env python3
import numpy as np


def parse(matrix_path):
    global matrix1, matrix2

    with open(matrix_path, "r") as matrix1_file:
        N1 = matrix1_file.readline()
        matrix1 = [list(map(int,line.split())) for line in matrix1_file] 