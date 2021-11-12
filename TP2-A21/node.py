#!/usr/bin/env python3

class Node:
    def __init__(self, couleur, DSAT, degree):
        self.couleur = couleur
        self.DSAT = DSAT
        self.degree = degree

    def definirCouleur(self, coul):
        self.couleur = coul
       
    def trouverDSAT(self):
        self.DSAT 
    
    def calculateDegree(self, matrix):
        self.degree
        for i in matrix[1]:
            for j in i:
                if j == 1:
                    self.degree += 1
        print(self.degree)
            

    def afficherCouleur(self):
        print("Couleur sommet: " + self.couleur)




