#Partie 1

#1

def init_bonus():
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
    
    list_bonus = [[] for i in range(15)]
    cases = [cases_MT, cases_MD, cases_LT, cases_LD]
    case_dico = {0:"MT", 1:"MD", 2:"LT", 3:"LD", 4:""}

    for i in range(15):
        for j in range(15):
            place = False
            for case in range(len(cases)):
                if ([i,j] in cases[case]):
                    list_bonus[i].append(case_dico[case])
                    place = True
            if (place == False):
                list_bonus[i].append(case_dico[4])
    return list_bonus
            
#print(init_bonus())
    

    
#2

def init_jetons():
    list_jeton = [["" for i in range(15)] for j in range(15)]
    return list_jeton
    
#print(init_jetons())

#3




# Partie 2

#1

def init_dico():
    dico={"A":{"occ":9, "val":1},"B":{"occ":2, "val":3},"C":{"occ":2, "val":3},"D":{"occ":3, "val":2},"E":{"occ":15, "val":1},"F":{"occ":2, "val":4},"G":{"occ":2, "val":2},"H":{"occ":2, "val":4},"I":{"occ":8, "val":1},"J":{"occ":1, "val":8},"K":{"occ":1, "val":10},"L":{"occ":5, "val":1},"M":{"occ":3, "val":2},"N":{"occ":6, "val":1},"O":{"occ":6, "val":1},"P":{"occ":2, "val":3},"Q":{"occ":1, "val":8},"R":{"occ":6, "val":1},"S":{"occ":6, "val":1},"T":{"occ":6, "val":1},"U":{"occ":6, "val":1},"V":{"occ":2, "val":4},"W":{"occ":1, "val":10},"X":{"occ":1, "val":10},"Y":{"occ":1, "val":10},"Z":{"occ":1, "val":10},"?":{"occ":2, "val":0}}
    return dico

dico=init_dico()


#2
def init_pioche(dico):
    pioche = []
    for l in dico:
        for occ in range(dico[l]['occ']):
            pioche.append(l)
    return pioche

#3
def piocher(x, sac):
    liste=[]
    if x<=len(sac):
        for l in range(x):
            p=random.randint(0,len(sac)-1)
            liste.append(sac.pop(p))
    else:
        for l in sac:
            liste.append(l)
    return liste


#4
def completer_main(main, sac):
    x=7-len(main)
    if len(sac)!=0:
        main.extend(piocher(x, sac))


#5
def echanger(jetons, main, sac):
    reponse=False
    if all(e in jetons for e in main):
        for e in jetons:
            main.remove(e)
        completer_main(main, sac)
        sac.extend(jetons)
        reponse=True
    return reponse




# Partie 3

#1

def generer_dico(nf):
    liste=nf.readlines()
    l1=[e[0:-1]for e in liste]
    return l1


