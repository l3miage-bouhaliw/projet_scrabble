###############################################
# Module de S C R A B B L E
# Auteur : IMBERT Thomas BOUHALI Walid
# Année  : 2020
###############################################


# liste des librairiesrairies
import random #lecture aleatoire
from copy import deepcopy #recopi de liste
import os #fichier
import re #expression reguliere pour split

# nb joueurs
nb_joueurs = 0
tableau_joueur_main = []

# contient la liste des bonus et des éléments liés
lst_bonus = [['MT','$','GREEN','Mot compte triple'],['MD','£','YELLOW','Mot compte double'],['LT','*','MAGENTA','Lettre compte triple'],['LD','!','GREY','Lettre compte double'],['','','','Acun bonus']];

# dimension du plateaude scrabble
int_dimensiontableau = 15

# liste des cases bonus
cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

# dictionnaire de jeu
dico_jeu = {}
dico_jeu = {"A" : {"occ" : 9, "val" : 1}, "B" : {"occ" : 2, "val" : 3}, "C" : {"occ" : 2, "val" : 3}, "D" : {"occ" : 3, "val" : 2},\
"E" : {"occ" : 15, "val" : 1}, "F" : {"occ" : 2, "val" : 4}, "G" : {"occ" : 2, "val" : 2}, "H" : {"occ" : 2, "val" : 4},\
"I" : {"occ" : 8, "val" : 1}, "J" : {"occ" : 1, "val" : 8}, "K" : {"occ" : 1, "val" : 10}, "L" : {"occ" : 5, "val" : 1},\
"M" : {"occ" : 3, "val" : 2}, "N" : {"occ" : 6, "val" : 1}, "O" : {"occ" : 6, "val" : 1}, "P" : {"occ" : 2, "val" : 3},\
"Q" : {"occ" : 1, "val" : 8}, "R" : {"occ" : 6, "val" : 1}, "S" : {"occ" : 6, "val" : 1}, "T" : {"occ" : 6, "val" : 1},\
"U" : {"occ" : 6, "val" : 1}, "V" : {"occ" : 2, "val" : 4}, "W" : {"occ" : 1, "val" : 10}, "X" : {"occ" : 1, "val" : 10},\
"Y" : {"occ" : 1, "val" : 10}, "Z" : {"occ" : 1, "val" : 10}, "§" : {"occ" : 2, "val" : 0}
}

# dico_jeu = {"A" : {"occ" : 1, "val" : 1}, "B" : {"occ" : 1, "val" : 3}, "C" : {"occ" : 1, "val" : 3}, "D" : {"occ" : 1, "val" : 2},\
# "E" : {"occ" : 1, "val" : 1}, "F" : {"occ" : 1, "val" : 4}, "G" : {"occ" : 1, "val" : 2}, "H" : {"occ" : 1, "val" : 1},\
# "I" : {"occ" : 1, "val" : 1}, "J" : {"occ" : 1, "val" : 8}, "K" : {"occ" : 1, "val" : 10}, "L" : {"occ" : 1, "val" : 1},\
# "M" : {"occ" : 1, "val" : 2}, "N" : {"occ" : 1, "val" : 1}, "O" : {"occ" : 1, "val" : 1}, "P" : {"occ" : 1, "val" : 3}\
# }

# dictionnaire des joueurs
dico_joueur = {}
# pour info pour un joueurs
dico_joueur = {"nomjoueur" : {"ordre" : 1, "nb_points" : 0, "main" : []}}

main_joueur = []

def init_bonus():
    """ Initialise les cases bonus d'un tableau.
    Parameters
    ----------
    Returns
    -------
    liste
        Le tableau (variable globale) à 2 dimension contenant les bonus.
    """
    #initialisation du tableau à vide
    tableau = init_tableau_chainevide()
    
    #Affectation des cases bonus
    for ligne in cases_MT:
        tableau[ligne[0]][ligne[1]] = 'MT'
    for ligne in cases_MD:
        tableau[ligne[0]][ligne[1]] = 'MD'
    for ligne in cases_LT:
        tableau[ligne[0]][ligne[1]] = 'LT'
    for ligne in cases_LD:
        tableau[ligne[0]][ligne[1]] = 'LD'
    return tableau


def affiche_bonus(b):
    """ Affiche le code bonus d'un bonus.
    
    Parameters
    ----------
    b : string
        Valeur alphanumérique du bonus
        
    Returns
    -------
    string
        Le code du bonus.
    """
    retour = ''
    for i in range(0,4):
        if lst_bonus[i][0]==b: 
            retour=lst_bonus[i][1]
    return retour

#fonction non utilisée pour le moment
def affiche_couleurbonus(b):
    retour=''
    for i in range(0,5):
        if lst_bonus[i][0] == b: 
            retour=lst_bonus[i][2]
    return retour

def init_tableau_chainevide():
    """ Initialise un tableau de chaîne vide avec la dimension du tableau en variable globale.
    
    Parameters
    ----------
        
    Returns
    -------
    liste
        Tableau de chaîne vide.
    """
    tableau = []
    # creation des lignes independantes par ajout
    for i in range(int_dimensiontableau):
        tableau.append([''] * int_dimensiontableau)
    return tableau

def  init_jetons():
    return init_tableau_chainevide()

#retourne la valeur de la case et son éventuel bonus
def affiche_jetons(j):
    #un jeton est un doublet repéré par
    #les coordonnées i et j où on le dépose
    #sur le plateau
    svaleurjeton = ''
    ligne = j[0]
    colonne = j[1]
    #sa position peut aussi concerné un bonus
    valeurjeton = tab_jeu[ligne][colonne]
    valeurbonus = tab_bonus[ligne][colonne]
    return [valeurjeton, valeurbonus]


def affiche_tableau():
    ligne_horizontale = '-------------------------------------------------------------'
    print(ligne_horizontale)
    for i in range(0, int_dimensiontableau):
        print('|', end="")
        #Parcours des colonnes
        for j in range(0,int_dimensiontableau):
            jeton = [i,j]
            retour_affichejeton = affiche_jetons(jeton)
            bonus = retour_affichejeton[1]
            valeurjeton = retour_affichejeton[0]
            #on affiche 3 caractères : espace + valeur + bonus
            if bonus == '': 
                sbonus = ' '
            else: 
                sbonus = affiche_bonus(bonus)
            if valeurjeton == '':
                svaleur = ' '
            else:
                svaleur = valeurjeton
            print(' ' + svaleur + sbonus, end="|")
        #saut de ligne
        print()
        #ligne horizontale
        print(ligne_horizontale)

def init_dico():
    return dico_jeu

def init_pioche(dico):
    liste = []
    for cle in dico.keys():
        for i in range(dico[cle]["occ"]):
            #print(cle)    
            liste.append(cle)
    return liste
 
def piocher(x, sac):
    """ Initialise un tableau de chaîne vide avec la dimension du tableau en variable globale.
    
    Parameters
    ----------
    x : int qui représente le nombre de jetons
    sac : liste qui représente tous les jetons
    
    Returns
    -------
    liste    de tout ce que l'on a piocher
    """ 
    liste_tirage = []
    for i in range(x):
        #tirage d'une lettre du sac
        nb_lettre = len(sac)-1
        tirage = random.randint(0, nb_lettre)
        element_tire = sac[tirage]
        sac.remove(element_tire)
        liste_tirage.append(element_tire)
    return liste_tirage
    
def completer_main(main,sac):
    #on compte le nombre de jetons 
    nb_jetons = len(main)
    nb_jetons_a_piocher = 7 - nb_jetons
    #test du nombre de pions dans le sac restant
    print(sac)
    print(main)
    if len(sac) < nb_jetons_a_piocher: 
        nb_jetons_a_piocher = len(sac)
        print('Il n y a plus de jetons')
    else:
        main.extend(piocher(nb_jetons_a_piocher, sac))

def echanger(jetons, main, sac):
    """ Initialise un tableau de chaîne vide avec la dimension du tableau en variable globale.
    
    Parameters
    ----------
    jetons : liste de jetons pris de la main
    main : liste qui représente tous les jetons pour le jeu
    sac : liste de la pioche
    
    Returns
    -------
    booleen qui indique si l'échange a réussi
    """
    # On contrôle que les jetosn sont bien dans la main 
    # avant de les echanger
    echange_reussi = True
    main_temporaire = main
    for j in jetons:
        if j not in main: 
            echange_reussi = False
            break
        else: 
            main_temporaire.remove(j)
            
    # On contrôle que l'échange est possible
    if len(jetons) > len(sac):
        echange_reussi = False
    # On peut procéder à l'échange
    if echange_reussi: 
        main = main_temporaire
        print(main)
        print(jetons)
        main.extend(piocher(len(jetons),sac))
        print(main)
        sac.extend(jetons)
    return echange_reussi

def generer_dico(nf):
    """ Initialise le dictionnaire des mots autorisés à partir d'un fichier
    
    Parameters
    ----------
    nf : nom du fichier situé à la racine du programme
    
    Returns
    -------
    liste qui indique les mots autorisés
    """
    liste_mots = []
    f = open(nf, "r")
    for mot in f:
        mot = mot.replace('\n','')
        liste_mots.append(mot)
    return liste_mots


def mot_jouable(mot, ll, nb_lettre_manquant):
    """ Indique si le mot fait fait partie de la liste
    
    Parameters
    ----------
    mot : chaine qui correspond au mot à tester
    ll : liste qui comprend la liste des lettres
    
    Returns
    -------
    booleen qui indique si le mot existe dans la liste
    """
    
    lettre_trouve = True
    main_copy = deepcopy(ll)
    joker = "§"
    nb_let_possible = nb_lettre_manquant
    for i in range(len(mot)):
        lettre_mot = mot[i]
        if lettre_mot in main_copy:
            main_copy.remove(lettre_mot)
        else:
            if joker in main_copy:
               main_copy.remove(joker)
            else:
                if (nb_let_possible > 0) and (lettre_mot in liste_lettre_tableau_jeu):
                    nb_let_possible = nb_let_possible - 1
                else:
                    lettre_trouve = False
                    break
    # if lettre_trouve == True :
       # ll = deepcopy(main_copy)
    #print (lettre_trouve)
    return lettre_trouve

    
    
def mots_jouables(motsfr, ll, nb_lettre_manquantes):
    """ Retourne les mots présents dans la liste
    
    Parameters
    ----------
    motsfr : liste de mots à tester
    ll : liste de lettre de la main
    ll_plateau : liste de lettres du plateau
    nb_lettre_manques : nombre de lettres manquantes (présentes sur le tableau)
    
    Returns
    -------
    liste des mots présents dans la liste de lettres
    """
    liste_mots_jouables = []
    for mot in motsfr:
        if mot_jouable(mot, ll, nb_lettre_manquantes):
            liste_mots_jouables.append(mot)
    return liste_mots_jouables
        
def lettres_plateau():
    liste_lettres_plateau = []
    for i in range(0, int_dimensiontableau):
        #Parcours des colonnes
        for j in range(0,int_dimensiontableau):
            liste_lettres_plateau.append(tab_jeu[i][j])
    return liste_lettres_plateau
    
    
    
    
def valeur_mot(mot, dico):
    """ Retourne la valeur du mot
    
    Parameters
    ----------
    mot : chaine du mot à tester
    dico : dictionnaire qui contient valeurs des lettres
    
    Returns
    -------
    Retourn un entier 
    """
    valeurs_mots = 0
    for i in range(len(mot)):
        lettre_mot = mot[i]
        valeurs_lettres = dico[lettre_mot]["val"]
        valeurs_mots = valeurs_lettres + valeurs_mots
    return valeurs_mots

    
def meilleur_mot(motsfr, ll, dico):
    """ Retourne le mot de plus haute valeur
    
    Parameters
    ----------
    motsfr : liste de mots jouables
    ll : liste de jetons
    dico : dictionnaire qui contient valeurs des lettres
    
    Returns
    -------
    Retourn un chaine du mot
    """
    liste_mots_jouables = mots_jouables(motsfr, ll, 0)
    mot_retenu = ''
    valeur = 0
    for mot in liste_mots_jouables:
        if valeur < valeur_mot(mot, dico):
            valeur = valeur_mot(mot, dico)
            mot_retenu = mot 
    return mot_retenu
    
    
def lire_coords():
    """ Retourne une coordonnée vide du tableau, elle vaut 0,0 si ce n'est pas possible
    
    Parameters
    ----------
        aucun
        
    Returns
    -------
    Coordonnée du placement possible
    """
    
    liste_coordonnee = ['0','0']
    chaine_coordonnee = input("Entrez les coordonnées de votre mot avec le format : i,j ")
#    print(re.split(',', chaine_coordonnee))
    liste_chaine_coordonnee = re.split(',', chaine_coordonnee)
    i = int(liste_chaine_coordonnee[0])
    j = int(liste_chaine_coordonnee[1])
    if i >= 0 and i < 15:
        if j >= 0 and j < 15:
            print(tab_jeu[i][j])
            if tab_jeu[i][j] == '':
               liste_coordonnee =  liste_chaine_coordonnee
    return liste_coordonnee
    
def tester_placement(plateau,i,j,direction,mot):
    """ Retourne une coordonnée vide du tableau, elle vaut 0,0 si ce n'est pas possible
    
    Parameters
    ----------
        plateau : liste du plateau de jeu
        i,j : entier coordonneé de la première lettre du mot
        direction : chaine parmi H ou V qui donne la direction Horizontal ou Vertical
        mot : chaine qui indique le mot à placer
        
    Returns
    -------
    liste_lettres : liste avec les lettre du mot (sans les lettres déjà présentes sur la tableau OU une liste vide
    """
    liste_lettres = []
    bl_on_continue = False
    int_longueur_mot = len(mot)
    int_i = int(i)
    int_j = int(j)
    # On test si le mot rentre dans le tableau
    if direction == 'V':
        if (int_i + int_longueur_mot) <= 15:
            bl_on_continue = True
    if direction == 'H':
        if (int_j + int_longueur_mot) <= 15:
            bl_on_continue = True
    if bl_on_continue:
        if direction == 'V':
            for i_mot in range(int_longueur_mot):
                #print('Mot : ', mot[i_mot], ' ',str(i_mot))
                #print('Tableau lettre : ', plateau[int_i + i_mot][int_j ], ' ', i, ' ', str(int_j + i_mot)) 
                if plateau[int_i + i_mot][int_j] == '':
                    bl_on_continue = True
                    liste_lettres.append(mot[i_mot])
                else:
                    if mot[i_mot] == plateau[int_i + i_mot][int_j]:
                        bl_on_continue = True
                    else:
                        bl_on_continue = False
                        break
        if direction == 'H':
            for i_mot in range(int_longueur_mot):
                #print('Mot : ', mot[i_mot], ' ',str(i_mot))
                #print('Tableau lettre : ', plateau[int_i][int_j + i_mot], ' ', i, ' ', str(int_j + i_mot)) 
                if plateau[int_i][int_j + i_mot] == '':
                    bl_on_continue = True
                    liste_lettres.append(mot[i_mot])
                else:
                    if mot[i_mot] == plateau[int_i][int_j  + i_mot]:
                        bl_on_continue = True
                    else:
                        bl_on_continue = False
                        break
    return liste_lettres
    
    
def placer_mot(plateau,lm,mot,i,j,direction):
    bln_mot_place = False
    lst_lettre_restante = tester_placement(plateau,i,j,direction,mot)
    int_longueur_mot = len(mot)
    int_i = int(i)
    int_j = int(j)

    # On test si on peut placer le mot dans le tableau
    if lst_lettre_restante == []:
        bln_mot_place = False
    else:
        # On peut placer le mot dans le plateau
        # liste des mots jouables
        bln_mot_jouable = mot_jouable(mot, lm, 1)
        if bln_mot_jouable == False:
            print("Ce mot n'est pas dans votre main")
            bln_mot_place = False
        else:
            # on test si le mot fait parti des mots jouables
            lst_mots_jouables = mots_jouables(liste_mots_dico, lm, 1)
            if mot in lst_mots_jouables:            
                # le mot est jouable et fait partir du dico et placable donc on le place
                if direction == 'V':
                    for i_mot in range(int_longueur_mot):
                        # print('Mot : ', mot[i_mot], ' ',str(i_mot))
                        # print('Tableau lettre : ', plateau[int_i + i_mot][int_j], ' ', i, ' ', str(int_j + i_mot)) 
                        plateau[int_i + i_mot][int_j] = mot[i_mot]
                if direction == 'H':
                    for i_mot in range(int_longueur_mot):
                        # print('Mot : ', mot[i_mot], ' ',str(i_mot))
                        # print('Tableau lettre : ', plateau[int_i][int_j + i_mot], ' ', i, ' ', str(int_j + i_mot)) 
                        plateau[int_i][int_j + i_mot] = mot[i_mot]
                # on enlève les lettres de la main
                for s_lettre in lst_lettre_restante:
                    if s_lettre in lm:
                        lm.remove(s_lettre)
                    else:
                        lm.remove('§')
                bln_mot_place = True
            else:
                print("Ce mot n'est pas dans le dico")
                bln_mot_place = False
    return bln_mot_place
    
def valeur_mot_tableau(mot, dico, plateau, i, j, direction):
    """ Retourne la valeur du mot
    
    Parameters
    ----------
    mot : chaine du mot à tester
    dico : dictionnaire qui contient valeurs des lettres
    
    Returns
    -------
    Retourn un entier 
    """
    valeurs_mots = 0

    int_longueur_mot = len(mot)
    int_i = int(i)
    int_j = int(j)
    int_bonus_mot = 1
    int_bonus_lettre = 1
    valeurs_mots = 0
    
    # le mot est jouable et placable donc on le place
    if direction == 'V':
        for i_mot in range(int_longueur_mot):
            # print('Mot : ', mot[i_mot], ' ',str(i_mot))
            # print('Tableau lettre : ', plateau[int_i + i_mot][int_j], ' ', i, ' ', str(int_j + i_mot)) 
            #plateau[int_i + i_mot][int_j] = mot[i_mot]
            #On cherche la valeur de la lettre et la valeur du bonus s'il y en a un
            lettre_mot = mot[i_mot]
            # print('Lettre de mon mot : ',lettre_mot)
            valeurs_lettres = dico[lettre_mot]["val"]
            # print('Valeur de lettre mot du dico: ', str(valeurs_lettres))
            #test du bonus lettre
            if tab_bonus[int_i + i_mot][int_j] == 'LD':
                #lettre compte double
                int_bonus_lettre = 2
            if tab_bonus[int_i + i_mot][int_j] == 'LT':
                int_bonus_lettre = 3
            if tab_bonus[int_i + i_mot][int_j] == 'MT':
                int_bonus_mot = 3
            if tab_bonus[int_i + i_mot][int_j] == 'MD':
                int_bonus_mot = 2
            valeurs_lettres = dico[lettre_mot]["val"] * int_bonus_lettre
            valeurs_mots = valeurs_lettres + valeurs_mots
            print('Valeur de lettre avec bonus: ', str(valeurs_lettres), ' valeur mot : ', str(valeurs_mots))    
    if direction == 'H':
        for i_mot in range(int_longueur_mot):
            # print('Mot : ', mot[i_mot], ' ',str(i_mot))
            # print('Tableau lettre : ', plateau[int_i][int_j + i_mot], ' ', i, ' ', str(int_j + i_mot)) 
            plateau[int_i][int_j + i_mot] = mot[i_mot]
            lettre_mot = mot[i_mot]
            valeurs_lettres = dico[lettre_mot]["val"]
            #test du bonus lettre
            #test du bonus lettre
            if tab_bonus[int_i][int_j + i_mot] == 'LD':
                #lettre compte double
                int_bonus_lettre = 2
            if tab_bonus[int_i][int_j + i_mot] == 'LT':
                int_bonus_lettre = 3
            if tab_bonus[int_i][int_j + i_mot] == 'MT':
                int_bonus_mot = 3
            if tab_bonus[int_i][int_j + i_mot] == 'MD':
                int_bonus_mot = 2
            valeurs_lettres = dico[lettre_mot]["val"] * int_bonus_lettre
            valeurs_mots = valeurs_lettres + valeurs_mots
        
    # test du bons mot
    valeurs_mots = valeurs_mots * int_bonus_mot
    
    if len(mot) == 7:
        valeurs_mots = valeurs_mots + 50
    
    return valeurs_mots

def tour_joueur(plateau, main):
    affiche_tableau()
    i_valeur_retour = 0
    
    s_reponse = input("Que voulez-vous jouer [PA]sser, [EC]hanger, [PL]acer : ")
    if s_reponse == "PA":
        #fonction à créer passer son tour_joueur
        print("Je passe ...")
    else:
        if s_reponse == "EC":
            # jetons à demander : jetons
            # sac est une picohe globale donc pas de paramètre
            nb_jetons_a_echanger = input('Combien de jetons, voulez-vous echanger ?')
            liste_jetons_a_echanger = []
            for i in range(int(nb_jetons_a_echanger)):
                jeton_a_echanger = input('Quelle lettre voulez-vous enlever ?')
                liste_jetons_a_echanger.append(jeton_a_echanger)
            #appel à la fonction
            #print(echanger(liste_jetons_a_echanger,main,liste_pioche))
            if echanger(liste_jetons_a_echanger, main, liste_pioche) == False:
                tour_joueur(plateau, main)
        else:
            if s_reponse == "PL":
                #print(meilleur_mot(liste_mots_dico, main, dico_jeu))
                i = input("Coordonnee i: ")
                if i.isdigit():
                    j = input("Coordonnee j: ")
                    if j.isdigit():
                        mot = input("Mot à placer: ")
                        direction = input("Donnez la direction H ou V: ")
                        if placer_mot(plateau,main,mot,i,j,direction) == False:
                            tour_joueur(plateau, main)
                        else:
                            #Le mot a été placé avec succès
                            i_valeur_retour = valeur_mot_tableau(mot, dico_jeu, plateau,i ,j, direction)
                            completer_main(main,liste_pioche)
                    else:
                        return tour_joueur(plateau, main)
                else:
                    return tour_joueur(plateau, main)
            else:
                return tour_joueur(plateau, main)
    return i_valeur_retour    
    
# Programme principal
# print('debut PP')

###############################################
# Initialisation du jeu
###############################################
# Initialisation : tableau de jeu
tab_bonus = init_bonus()#initialisation du tableau de bonus
tab_jeu = init_jetons()#initialisation du tableau de jeu
nom_fichier = "littre.txt"  
liste_mots_dico = generer_dico(nom_fichier)
liste_pioche = init_pioche(dico_jeu)
dico_joueur = {}
bln_fin_de_partie = False

###############################################
# Initialisation des joueurs
###############################################
affiche_tableau()
s_rep = input("Combien de joueurs dans votre partie de scrabble (entre 2 et 4) ? ")
i_rep = int(s_rep) + 1
i = 1
while i < i_rep:
    s_nom = input("Entrez le nom du joueur : ")
    main_joueur = piocher(7,liste_pioche)
    dico_joueur[s_nom] = {"ordre" : i, "nb_points" : 0, "main" : main_joueur}
    print(dico_joueur[s_nom])
    i = i + 1

###############################################
# jeu
###############################################
s_nom_joueur_termine = ""
bln_partie_terminee = False    
while bln_partie_terminee == False:
    for cle, valeur in dico_joueur.items():
        liste_lettre_tableau_jeu = lettres_plateau()
        # Affichage pioche 
        # print(liste_pioche)
        # Affiche le joueur
        print("Joueur : ", cle, valeur['main'])
        main_joueur = valeur['main']
        nb_points_mot = tour_joueur(tab_jeu, main_joueur)
        print(main_joueur)
        dico_joueur[cle]['main'] = main_joueur
        print(dico_joueur[cle])
        # Calcul 
        print('Nombre de points gagnés : ', str(nb_points_mot))
        dico_joueur[cle]['nb_points'] = dico_joueur[cle]['nb_points'] + nb_points_mot
        print('Score : ', str(dico_joueur[cle]['nb_points']))
        # Fin de partie : il n'y a plus de jetons
        if len(main_joueur) < 7:
            s_nom_joueur_termine = cle
            bln_partie_terminee = True
            break
            
###############################################
# Calcul des scores finaux
###############################################
for cle, valeur in dico_joueur.items():
    if cle != s_nom_joueur_termine:
        # Calcul la valeur de la main pour ma retrancher au scores
        mot_restant = "".join(valeur['main'])
        nb_points_a_enlever = valeur_mot(mot_restant, dico_jeu)
        valeur['nb_points'] = valeur['nb_points'] - nb_points_a_enlever
        
###############################################
# Affichage du 1er gagnant
###############################################
s_nom_gagnant = ""
i_nb_points_gagnant = 0
for cle, valeur in dico_joueur.items():
    print('Score du joueur : ', cle, str(valeur['nb_points']))
    if valeur['nb_points'] > i_nb_points_gagnant:
        s_nom_gagnant = cle
        i_nb_points_gagnant = valeur['nb_points']        

# Affiche le gagnant
print('Le gagnant est : ', s_nom_gagnant)

# val_mot = valeur_mot("ELEA", dico_jeu)
# print(str(val_mot))

# main_joueur = piocher(7,liste_pioche)
# print(main_joueur)
# print(meilleur_mot(liste_mots_dico, main_joueur, dico_jeu))

# tab_jeu[2][2] = 'J' #exemple de lettre affectée
# tab_jeu[2][3] = 'O' #exemple de lettre affectée
# tab_jeu[2][4] = 'U' #exemple de lettre affectée
# tab_jeu[2][5] = 'R' #exemple de lettre affectée
# affiche_tableau()

# tour_joueur(tab_jeu, main_joueur)

# print(main_joueur)

# #print(lire_coords())
# i = input("Coordonnee i: ")
# j = input("Coordonnee j: ")
# mot = input("Mot à placer: ")
# direction = input("Donnez la direction H ou V: ")
# #print(tester_placement(tab_jeu, i, j, direction, mot))
# if placer_mot(tab_jeu,main_joueur,mot,i,j,direction):
    # affiche_tableau()
    # print(main_joueur)
    # print(str(valeur_mot_tableau(mot, dico_jeu, tab_jeu, i, j, direction)))
    


# liste_lettre_tableau_jeu = lettres_plateau()

# nb_joueurs = input('Entrez le nombre de joueurs : ')

# print(liste_pioche)

# for i in range (int(nb_joueurs)):
    # main_joueur = piocher(0,liste_pioche)
    # completer_main(main_joueur,liste_pioche)
    # tableau_joueur_main.append(main_joueur)
    # print(main_joueur)
    # print(mots_jouables(liste_mots_dico, main_joueur,1))
    # test=input('Entrez un mot : ')
    # print(mot_jouable(test, main_joueur,1))
    # print(main_joueur)
# # print(tableau_joueur_main)
# # print(liste_pioche)  
# # nom_fichier = "c:/temp/scrabble_dico.txt"  
# # generer_dico(nom_fichier)
# # print(generer_dico(nom_fichier))



# # print(liste_pioche)
# # main_joueur = piocher(2,liste_pioche)
# # print(main_joueur)
# # print(liste_pioche)
# # completer_main(main_joueur,liste_pioche)
# # print(main_joueur)
# # print(liste_pioche)

# nb_jetons_a_echanger = input('combien de jetons, voulez-vous enlever ?')
# liste_jetons_a_echanger = []
# for i in range(int(nb_jetons_a_echanger)):
    # jeton_a_echanger = input('Quelle lettre voulez-vous enlever ?')
    # liste_jetons_a_echanger.append(jeton_a_echanger)
# #appel à la fonction
# print(echanger(liste_jetons_a_echanger,main_joueur,liste_pioche))
# print(main_joueur)
# print(liste_pioche)
# print('fin PP')     
