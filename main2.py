import random

coords = [(int(random.random()*50), int(random.random()*50)) for _ in range(150)]
print(coords)

# grille = [['x' for y in range(100)] for x in range(150)]
# celluleInitiale = [(5, 1), (28, 38), (3, 32), (34, 42), (17, 12), (7, 2), (24, 19), (1, 27), (32, 36), (47, 2), (3, 15), (0, 5), (26, 18), (44, 41), (35, 40), (33, 30), (44, 12), (45, 42), (2, 20), (35, 15), (13, 48), (24, 45), (40, 31), (40, 19), (30, 44), (35, 39), (33, 35), (46, 13), (41, 23), (48, 43)]
# celluCopie = []

# for (i,j) in enumerate(celluleInitiale):
#     x = j[0]+50
#     y = j[1]+50
#     j = (x,y) 
#     celluCopie.append(j)

# for(i,j) in enumerate(celluCopie):
#     celluleInitiale.append(j)
# print(celluleInitiale)
# print('celluCopie'+str(celluCopie))

# for (i,j) in enumerate(celluCopie):
#     grille[j[0]][j[1]] = 'o'
# print('grille')

# for ligne in grille :
#     for colonne in ligne :
#         print(colonne,end='')
#     print()


