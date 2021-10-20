#!/usr/bin/env python3
import numpy as np


def parse(matrix_path):
    global matrix

    with open(matrix_path, "r") as matrix_file:
        matrix = [list(map(int,line.split())) for line in matrix_file] 
        print(matrix)



