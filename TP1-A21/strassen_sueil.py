#!/usr/bin/env python3


import numpy as np
import conventional
import strassen

def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassenSeuil(x, y, seuil):
       x = np.array(x)
       y = np.array(y)
       return  conventional.multiply(x,y) if len(x) <= seuil else strassen.strassen(x,y)