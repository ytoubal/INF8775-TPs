#!/usr/bin/env python3

import numpy as np
import conventional
import strassen

def strassenSeuil(x, y, seuil):
       x = np.array(x)
       y = np.array(y)

       if len(x) <=  seuil:
              c = conventional.multiply(x,y)
       else:
              # Splitting the matrices into quadrants. This will be done recursively
              a, b, c, d = strassen.split(x)
              e, f, g, h = strassen.split(y)

              # Computing the 7 products, recursively (p1, p2...p7)
              p1 = strassenSeuil(a, f - h, seuil)
              p2 = strassenSeuil(a + b, h, seuil)
              p3 = strassenSeuil(c + d, e, seuil)
              p4 = strassenSeuil(d, g - e, seuil)
              p5 = strassenSeuil(a + d, e + h, seuil)
              p6 = strassenSeuil(b - d, g + h, seuil)
              p7 = strassenSeuil(a - c, e + f, seuil)

              # Computing the values of the 4 quadrants of the final matrix c
              c11 = p5 + p4 - p2 + p6
              c12 = p1 + p2
              c21 = p3 + p4
              c22 = p1 + p5 - p3 - p7

              # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
              # From https://www.geeksforgeeks.org/strassens-matrix-multiplication/
              c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

       return c 