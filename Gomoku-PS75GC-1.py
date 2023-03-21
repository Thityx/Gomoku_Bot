# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:38:42 2022

@author: thityx
"""

import numpy as np
import random
import time

plateau = np.zeros((15,15))

def String(plateau):
    """Un ToString du plateau avec les indices (lettres et chiffres des coordonnées) sur le côté gauche et la bas"""
    result = ''
    compteurIndice = 15
    if len(plateau) != 15:
        return "Not a 15x15 matrix"
    else :
        for i in range(0,15):
            result += str(compteurIndice)
            if compteurIndice < 10:
                result += ' '
            compteurIndice -= 1
            result += '|'
            for j in range(0,15):
                
                
                if plateau[i,j]==1:
                    result+='X '
                elif plateau[i,j]==2:
                    result+='O '
                elif plateau[i,j]==9: # La case du coup gagnant
                    result+='W '
                else:
                    # result+='□ '
                    result+='. '
            result += '\n'
        result += '   ------------------------------\n'
        result += '   A B C D E F G H I J K L M N O \n'
    return result            


def Test_Victoire(tab, x, y):
    """Vérifie une victoire créée par le dernier coup x,y joué et retourne en retourne un booléen"""
    result= False
    if tab[x][y] != 0:
        val = tab[x][y] # On définie la valeur comme étant celle du dernier coup joué, donc du dernier joueur ayant joué

#--------------Victoire avec les lignes----------------#
        if not result:
            for i in range(0,5): # de 0 à 4
                try: #On évite les sorties de tableau
                    if (tab[x][y-i], tab[x][y-i+1], tab[x][y-i+2], tab[x][y-i+3], tab[x][y-i+4]) == (val, val, val, val, val) and (y-i+4) >= 0 and (y-i+3) >= 0 and (y-i+2) >= 0 and (y-i+1) >= 0 and (y-i) >= 0:
                        # On vérifie que toute la ligne à la même valeur
                        result = True
                        break
                except:
                    # Si on a une erreur de sortie du tableau, on passe juste et on continue le calcul
                    # Cela fait perdre du temps mais on ne fait qu'1 if, et on évite d'avoir 45 conditions pour l'éviter
                    # print('Error : out of array')
                    pass
    
#--------------Victoire avec les colonnes----------------#
        if not result:
            for i in range(0,5): # de 0 à 4
                try: #On évite les sorties de tableau
                    if (tab[x-i][y], tab[x-i+1][y], tab[x-i+2][y], tab[x-i+3][y], tab[x-i+4][y]) == (val, val, val, val, val) and (x-i+4) >= 0 and (x-i+3) >= 0 and (x-i+2) >= 0 and (x-i+1) >= 0 and (x-i) >= 0:
                        # On vérifie que toute la colonne à la même valeur
                        result = True
                        break
                except:
                    # Si on a une erreur de sortie du tableau, on passe juste et on continue le calcul
                    # Cela fait perdre du temps mais on ne fait qu'1 if, et on évite d'avoir 45 conditions pour l'éviter
                    # print('Error : out of array')
                    pass
                    
#--------------Victoire Diagonale 1 (haut gauche, bas droite)----------------#  
        if not result:
            for i in range(0,5): # de 0 à 4, on commence en haut à gauche et on parcourt jusqu'en basà droite
                try:
                    if (tab[x+i-4][y+i-4], tab[x+i-3][y+i-3], tab[x+i-2][y+i-2], tab[x+i-1][y+i-1], tab[x+i][y+i]) == (val, val, val, val, val) and (x+i-4) >= 0 and (y+i-4) >= 0 and (x+i-3) >= 0 and (y+i-3) >= 0 and (x+i-2) >= 0 and (y+i-2) >= 0 and (x+i-1) >= 0 and (y+i-1) >= 0 and (x+i) >= 0 and (y+i) >= 0:
                        # On vérifie une diagonale
                        result = True
                        break
                except:
                    # Si on a une erreur de sortie du tableau, on passe juste et on continue le calcul
                    # Cela fait perdre du temps mais on ne fait qu'1 if, et on évite d'avoir 45 conditions pour l'éviter
                    # print('Error : out of array')
                    pass
    
#--------------Victoire Diagonale 2 (haut droite, bas gauche)----------------#  
        if not result:
            for i in range(0,5): # de 0 à 4, on commence en haut à gauche et on parcourt jusqu'en basà droite
                try:
                    if (tab[x+i-4][y-i+4], tab[x+i-3][y-i+3], tab[x+i-2][y-i+2], tab[x+i-1][y-i+1], tab[x+i][y-i]) == (val, val, val, val, val) and (x+i-4) >= 0 and (y-i+4) >= 0 and (x+i-3) >= 0 and (y-i+3) >= 0 and (x+i-2) >= 0 and (y-i+2) >= 0 and (x+i-1) >= 0 and (y-i+1) >= 0 and (x+i) >= 0 and (y-i) >= 0:
                        # On vérifie l'autre diagonale
                        result = True
                        break
                except:
                    # Si on a une erreur de sortie du tableau, on passe juste et on continue le calcul
                    # Cela fait perdre du temps mais on ne fait qu'1 if, et on évite d'avoir 45 conditions pour l'éviter
                    # print('Error : out of array')
                    pass

    else : # Dans le cas (normalement impossible) où le dernier coup est une case vide, on retourne False
        result = False

    return result
        
def PlateauPlein(tab):
    """Vérifie si le plateau est plein donc si il y un une égalité, en retourne un booléen"""
    result= False
    if not result:
        temp = True # Variable temporaire, elle reste True tant qu'on a pas trouvé de '0' et si elle l'est encore à
        # la fin, c'est qu'il n'y a aucune place de libre et que le plateau est plein, donc on passe result en True
        for i in range(0,14):
            if 0 in tab[i]:
                temp = False
                break # On a trouvé un 0 donc une place, on sort de la boucle sans changer result qui reste False
        if temp:
            result = True
    return result

def LectureCoord():
    """Lis la console et traduit un string de la forme 'X99' en coordonnées (x,y) utilisable sur le plateau"""
    a,b = (-1,- 1) 
    while((a,b) == (-1,-1)):
        try:
            string = input("Coordonnées de la forme 'A12' avec la lettre de A à O et le nombre de 1 à 15: ")
            if len(string)<2 or len(string)>3:
                print("Problème de synthaxe, coordonnées trop courtes ou trop longues")
            elif not string[0].isalpha() or not (string[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']):
                print("Problème de synthaxe, le premier caractère n'est pas une lettre ou pas une bonne lettre(bonne forme : 'A12'")
            elif not string[1:].isdigit() or not string[1:] in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
                print("Problème de synthaxe, les 2ème (et 3ème) caractères ne sont pas des chiffres ou pas dans l'intervalle [1,15] (bonne forme : 'A12')")
            else:
                dicoNombre = {'15' : 0, '14' : 1, '13' : 2, '12' : 3, '11' : 4, '10' : 5, '9' : 6, '8' : 7, '7' : 8, '6' : 9, '5' : 10, '4' : 11, '3' : 12, '2' : 13, '1' : 14}
                a = dicoNombre[string[1:]]
                dicoLettres = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14}
                b = dicoLettres[string[0]]
                print('au final :', a, b)
                if plateau[a,b]!=0:
                    print("Case non libre")
                else:
                    (x,y) = (a,b)
        except:
            print("Erreur, entrez un couple d'entier de la forme 'x,y'")

    return (x,y)

def PlayPvP():
    """Lance une partie Player versus Player (joueur contre joueur)"""
    plateau = np.zeros((15,15))
    plateauplein = False
    victoire = False
    print(String(plateau))
    while(not victoire):   
        # Tour joueur 1
        print("Tour du joueur 1 (X) : ")
        (x1, y1) = LectureCoord()
        plateau[x1,y1] = 1
        print(String(plateau))
        # Vérification victoire joueur 1
        victoire = Test_Victoire(plateau, x1, y1)
        if victoire:
            plateau[x1,y1] = 9  
            print(String(plateau))
            print("Victoire du joueur 1 (X) !!")
            break
        # Vérification de fin partie
        plateauplein = PlateauPlein(plateau)
        if plateauplein:
            print("Egalité, le plateau est plein, personne de gagne !!")
            break
        
        # Tour joueur 1
        print("Tour du joueur 2 (O) : ")
        (x2, y2) = LectureCoord()
        plateau[x2,y2] = 2
        print(String(plateau))
        # Vérification victoire joueur 2
        victoire = Test_Victoire(plateau, x2, y2)
        if victoire:
            plateau[x2,y2] = 9
            print(String(plateau))
            print("Victoire du joueur 2 (O) !!")
            break
        # Vérification de fin partie
        plateauplein = PlateauPlein(plateau)
        if plateauplein:
            print("Egalité, le plateau est plein, personne de gagne !!")
            break

def PlayRandvRand():
    """Lance une partie Random versus Random (aléatoire contre aléatoire)"""
    dureepause = 0.1
    plateau = np.zeros((15,15))
    victoire = False
    plateauplein = False
    print(String(plateau))
    time.sleep(dureepause)
    while(not victoire):   
        # Tour joueur 1
        print("Tour du joueur 1 (X) : ")
        (x1,y1) = (-1,-1)
        # On génère un coup valide aléatoire
        while((x1,y1) == (-1,-1)):
            x = random.randint(1, 15)
            y = random.randint(1, 15)
            if plateau[x-1,y-1]!=0:
                # print("Case non libre")
                pass
            else:
                (x1,y1) = (x-1,y-1)
        print(x1, y1)
        plateau[x1,y1] = 1
        print(String(plateau))
        # Pause pour visualisation
        time.sleep(dureepause)
        
        # Vérification victoire joueur 1
        victoire = Test_Victoire(plateau, x1, y1)
        if victoire:
            plateau[x1,y1] = 9  
            print(String(plateau))
            print("Victoire du joueur 1 (X) !!")
            break
        # Vérification de fin partie
        plateauplein = PlateauPlein(plateau)
        if plateauplein:
            print("Egalité, le plateau est plein, personne de gagne !!")
            break
        
        # Tour joueur 1
        print("Tour du joueur 2 (O) : ")
        (x2,y2) = (-1,-1)
        # On génère un coup valide aléatoire
        while((x2,y2) == (-1,-1)):
            x = random.randint(1, 15)
            y = random.randint(1, 15)
            if plateau[x-1,y-1]!=0:
                #print("Case non libre")
                pass
            else:
                (x2,y2) = (x-1,y-1)
        print(x2, y2)
        plateau[x2,y2] = 2
        print(String(plateau))
        # Pause pour visualisation
        time.sleep(dureepause)
        
        # Vérification victoire joueur 2
        victoire = Test_Victoire(plateau, x2, y2)
        if victoire:
            plateau[x2,y2] = 9
            print(String(plateau))
            print("Victoire du joueur 2 (O) !!")
            break
        # Vérification de fin partie
        plateauplein = PlateauPlein(plateau)
        if plateauplein:
            print("Egalité, le plateau est plein, personne de gagne !!")
            break
        

# %% zone du main
if __name__ == '__main__' :
    PlayPvP()
    # PlayRandvRand()
