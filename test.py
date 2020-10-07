# -*-coding: utf-8 -*-
import random
import time
import os
import matplotlib
import matplotlib.pyplot as plt


def creerGrille(ligne, colonne):
    y = []
    x = []
    for i in ligne:
        for j in colonne:
            y.append(i)
            x.append(j)

    


def printGraph():
    a = [1, 2, 3, 4, 2]
    b = [1, 4, 9, 16, 5]
    plt.plot(a, b, 'bs')
    plt.axis([0,6,0,20])
    plt.show()

def main():
    printGraph()
    
if __name__ == '__main__':
    main()
