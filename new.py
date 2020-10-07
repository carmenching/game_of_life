# -*-coding: utf-8 -*-
import os
import time
import random


def imprimerCellule(cellule):
    if cellule : 
        return '•'
    return ' '
#-----------------Grille-----------------#

# Créer la grille
def creerGrille(ligne, colonne, wrap, celluleInitiale):
    cellule = False
    if wrap : 
        ligneWrap = ligne*2
        grille = [[cellule for y in range(colonne)] for x in range(ligneWrap)]
        # multiply each cellule by 2
        celluleCopie = []
        for (i,j) in enumerate(celluleInitiale):
            coordoneeWrap = (j[0]+ligne,j[1])
            celluleCopie.append(coordoneeWrap)
        for(i,j) in enumerate(celluleCopie):
            celluleInitiale.append(j)
    else : 
        grille = [[cellule for y in range(colonne)] for x in range(ligne)]
    
    # print("grille ligne:" + str(len(grille)))
    # print("grille colonne:" + str(len(grille[0])))
    for (i,j) in enumerate(celluleInitiale):
        grille[j[0]][j[1]] = True
    
    

    return grille

def imprimerGrille(grille):
    for ligne in grille :
        for colonne in ligne :
            print(imprimerCellule(colonne), end='')
        print()

#-------------------------------------------------#

def prochaineGeneration(grille):
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            lstVoisin = verifierVoisin(ligne, colonne, grille)
            lstVoisinVivant = []
            for (i,j) in enumerate(lstVoisin):
                if grille[j[0]][j[1]]:
                    lstVoisinVivant.append((i,j))
            celluleTeste = grille[ligne][colonne]
            if celluleTeste : 
                if len(lstVoisinVivant) < 2 or len(lstVoisinVivant) > 3 :
                    celluleTeste = False
            else : 
                if len(lstVoisinVivant) == 3 :
                    celluleTeste = True
            grille[ligne][colonne] = celluleTeste
    return grille

def verifierVoisin(y, x, grille):
    lstVoisin = []
    for ligne in range(-1,2):
        for colonne in range(-1,2):
            ligneVoisin = y+ligne
            colonneVoisin = x+colonne
            estVoisin = True
            if ligneVoisin == y and colonneVoisin == x:
                estVoisin = False
            if ligneVoisin < 0 or ligneVoisin >= len(grille):
                estVoisin = False
            if colonneVoisin < 0 or colonneVoisin >= len(grille[0]):
                estVoisin = False
            if estVoisin:
                lstVoisin.append((ligneVoisin, colonneVoisin))
    return lstVoisin

def genererNombreCellule(total):
    return int(total*0.25)

def main():
    ligne = int(input("Inserer le nombre de ligne du graphe: "))
    colonne = int(input("Inserer le nombre de colonne du graphe: "))
    total = ligne*colonne
    frequency = int(input("nombre de génération souhaité : "))
    estWrap = False
    wrap = (input("Est-ce que le graphe sera wrappé? '0' pour non et '1' pour oui: "))
    if wrap == '1':
        estWrap = True
    nbrCellule = genererNombreCellule(total)
    celluleInitiale = [(int(random.random()*ligne), int(random.random()*colonne)) for x in range(nbrCellule)]
    grilleInitiale = creerGrille(ligne, colonne, estWrap, celluleInitiale)
    os.system('cls')
    imprimerGrille(grilleInitiale)
    time.sleep(3)
    os.system('cls')
    for i in range(frequency):
        nextGrille = prochaineGeneration(grilleInitiale)
        imprimerGrille(nextGrille)
        time.sleep(3)
        os.system('cls')
        grilleInitiale = nextGrille

    print("End")

if __name__ == '__main__':
    main()

#-----------------Cellule-----------------#
# def tuerCellule(cellule) :
#     cellule = False
#     return cellule

# def revivreCellule(cellule) : 
#     cellule = True
#     return cellule

# def estVivant(cellule) :
#     if cellule:
#         return True
#     else : return False