#!/usr/bin/env python3
import numpy as np


def parse(matrix_path):
    global matrix
    global vertex_num

    with open(matrix_path, "r") as matrix_file:
        vertex_num = int(matrix_file.readline())
        matrix = [list(map(int,line.split())) for line in matrix_file] 



