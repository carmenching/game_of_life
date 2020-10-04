# -*-coding: utf-8 -*-
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

def imprimerCellule(cellule):
    if cellule : 
        return 'O'
    return '_'
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
        grille = [[cellule for y in range(ligne)] for x in range(colonne)]
    
    for (i,j) in enumerate(celluleInitiale):
        grille[j[0]][j[1]] = True
    return grille

def imprimerGrille(grille):
    for ligne in grille :
        for colonne in ligne :
            print(imprimerCellule(colonne),end='')
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

            
            # print('('+str(ligne)+','+str(colonne)+'):' + str(lstVoisin))


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

def main():
    celluleInitiale = [(3, 49), (19, 0), (9, 6), (10, 6), (11, 6), (39, 7), (3, 25), (42, 48), (8, 0), (33, 28), (28, 38), (5, 32), (18, 11), (6, 22), (24, 39), (29, 32), (22, 34), (30, 40), (28, 7), (8, 43), (36, 43), (22, 31), (47, 14), (35, 9), (25, 15), (21, 14), (10, 0), (27, 6), (1, 18), (14, 44), (14, 41), (31, 29), (47, 33), (26, 7), (5, 21), (27, 29), (14, 42), (20, 17), (31, 13), (1, 12), (36, 25), (18, 0), (7, 14), (24, 39), (25, 30), (46, 42), (14, 17), (49, 0), (32, 6), (40, 21), (31, 32), (1, 26), (1, 35), (41, 25), (28, 1), (6, 19), (24, 25), (44, 48), (16, 19), (1, 30), (21, 8), (6, 40), (1, 37), (9, 22), (40, 27), (28, 10), (40, 11), (30, 9), (32, 5), (22, 21), (15, 32), (20, 7), (12, 29), (42, 42), (9, 5), (20, 0), (14, 26), (46, 45), (30, 7), (13, 19), (5, 9), (35, 42), (29, 5), (4, 34), (18, 41), (12, 3), (25, 16), (2, 2), (14, 33), (37, 49), (46, 32), (15, 8), (31, 28), (13, 44), (44, 39), (30, 16), (40, 37), (26, 49), (8, 40), (45, 14), (23, 33), (49, 21), (28, 22), (21, 18), (16, 41), (33, 28), (40, 32), (31, 22), (5, 15), (5, 25), (31, 40), (25, 44), (45, 34), (16, 23), (34, 45), (14, 17), (22, 19), (35, 40), (2, 26), (23, 14), (20, 37), (38, 7), (29, 33), (48, 39), (35, 29), (35, 42), (19, 35), (5, 11), (48, 33), (10, 49), (41, 4), (31, 7), (11, 13), (3, 10), (27, 15), (49, 33), (18, 38), (0, 40), (26, 10), (48, 38), (29, 33), (20, 13), (16, 33), (9, 35), (5, 23), (26, 34), (23, 9), (22, 19), (25, 40), (2, 41), (47, 26), (28, 33)]
    grilleInitiale = creerGrille(50, 50, True, celluleInitiale)
    print("grille taille: " + str(len(grilleInitiale)))
    print("imprimerGrille")
    imprimerGrille(grilleInitiale)
    print("Test Neighbour List")
    nextGrille = prochaineGeneration(grilleInitiale)
    imprimerGrille(nextGrille)

    # imprimerGrille(grilleInitiale)    
if __name__ == '__main__':
    main()

