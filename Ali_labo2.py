from copy import copy
from copy import deepcopy
from encodings import utf_8



# Étape 1

# Chaque variable permet de lire leur base de donnée
def  lecture_fichier():
    f1 = open("data1.txt", "r", encoding='utf8')
    f2 = open("data2.txt", "r", encoding='utf8')
    f3 = open("data3.txt", "r", encoding='utf8')
    read_line1 = f1.readlines()
    read_line2 = f2.readlines()
    read_line3 = f3.readlines()
    read_line1[1] = float(read_line1[1])
    read_line1[2] = float(read_line1[2])
    read_line1[3] = float(read_line1[3])
    read_line1[4] = float(read_line1[4])
    read_line1[5] = float(read_line1[5])

    read_line2[1] = float(read_line2[1])
    read_line2[2] = float(read_line2[2])
    read_line2[3] = float(read_line2[3])
    read_line2[4] = float(read_line2[4])
    read_line2[5] = float(read_line2[5])

    read_line3[1] = float(read_line3[1])
    read_line3[2] = float(read_line3[2])
    read_line3[3] = float(read_line3[3])
    read_line3[4] = float(read_line3[4])
    read_line3[5] = float(read_line3[5])
    
    liste = read_line1, read_line2, read_line3
    f1.close()
    f2.close()
    f3.close()
    return liste

liste_equipe = lecture_fichier()


# Étape 2





# Étape 3

# Vous devez afficher les statistiques suivantes :

#   * Équipe ayant le coureur le plus rapide et le temps de ce dernier.
#   * Temps moyens par équipe présenté en ordre croissant, donc de l'équipe la plus rapide à la plus lente. 
#     Vous devez y afficher le nom de l'équipe et leur temps de course moyen.

def execution_user(l_equipe):

    print("1 pour Afficher les statistiques")
    print("2 pour Sauvegarder les statistiques")
    print("3 pour Afficher l'équipe avec les coureurs les plus similaires")
    print("4 pour Ajouter une faute à une équipe")
    
    choix = int(input("Veuillez faire votre choix: "))

    if choix == 1:
        min4 = min(liste_equipe[0:5])
        min2 = min(liste_equipe[1:5])
        min3 = min(liste_equipe[2:5])
        totalmin = min([min2]), min([min4])
        print(min(totalmin[1:5]))
    elif choix == 2:
        # Sauvegarder les statistiques
        print("jdjd")
    elif choix == 3:
        # Afficher l'équipe avec les coureurs les plus similaires
        print("jddj")
    elif choix == 4:
        # Ajouter une faute à une équipe
        print("sjs")
    else:
        print("Mauvais choix")
    return

execution_user(liste_equipe)