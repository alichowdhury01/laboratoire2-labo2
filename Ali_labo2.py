from copy import copy
from copy import deepcopy
from encodings import utf_8


def  lecture_fichier():
    f1 = open("data1.txt", "r", encoding='utf8')
    f2 = open("data2.txt", "r", encoding='utf8')
    f3 = open("data3.txt", "r", encoding='utf8')

    read_line_f1 = f1.readlines()
    read_line_f2 = f2.readlines()
    read_line_f3 = f3.readlines()

    read_line_f1[1] = float(read_line_f1[1])
    read_line_f1[2] = float(read_line_f1[2])
    read_line_f1[3] = float(read_line_f1[3])
    read_line_f1[4] = float(read_line_f1[4])
    read_line_f1[5] = float(read_line_f1[5])

    read_line_f2[1] = float(read_line_f2[1])
    read_line_f2[2] = float(read_line_f2[2])
    read_line_f2[3] = float(read_line_f2[3])
    read_line_f2[4] = float(read_line_f2[4])
    read_line_f2[5] = float(read_line_f2[5])

    read_line_f3[1] = float(read_line_f3[1])
    read_line_f3[2] = float(read_line_f3[2])
    read_line_f3[3] = float(read_line_f3[3])
    read_line_f3[4] = float(read_line_f3[4])
    read_line_f3[5] = float(read_line_f3[5])
    
    dictionnaire_equipe = {'A': read_line_f1[1:6], 'B': read_line_f2[1:6], 'C': read_line_f3[1:6]}

    f1.close()
    f2.close()
    f3.close()
    return dictionnaire_equipe

liste_equipe = lecture_fichier()
meilleur_temps = min(liste_equipe, key=liste_equipe.get)

def execution_user(l_equipe):

    print("1 pour Afficher les statistiques\n"
          "2 pour Sauvegarder les statistiques\n"
          "3 pour Afficher l'équipe avec les coureurs les plus similaires\n"
          "4 pour Ajouter une faute à une équipe")

    choix = int(input("Veuillez faire votre choix: "))

    if choix == 1:


        equipeA_moyenne = f"{sum(liste_equipe['A'])/len(liste_equipe['A']):.3f}"
        equipeB_moyenne = f"{sum(liste_equipe['B'])/len(liste_equipe['B']):.3f}"
        equipeC_moyenne = f"{sum(liste_equipe['C'])/len(liste_equipe['C']):.3f}"

        liste_moyenne = [equipeA_moyenne + ": Equipe A", equipeB_moyenne + ": Equipe B", \
                         equipeC_moyenne + ": Equipe C"]

        print(f"\nLe meilleur coureur est dans l'équipe {meilleur_temps} et son temps"
              f" étant de {min(liste_equipe[meilleur_temps])}\n")
          
        print(f"Moyenne des equipes: {sorted(liste_moyenne)}")
    elif choix == 2:
        equipeA_moyenne = f"{sum(liste_equipe['A'])/len(liste_equipe['A']):.3f}"
        equipeB_moyenne = f"{sum(liste_equipe['B'])/len(liste_equipe['B']):.3f}"
        equipeC_moyenne = f"{sum(liste_equipe['C'])/len(liste_equipe['C']):.3f}"

        liste_moyenne = [equipeA_moyenne + ": Equipe A", equipeB_moyenne + ": Equipe B", \
                         equipeC_moyenne + ": Equipe C"]
        liste_moyenne_croissant= sorted(liste_moyenne)

        sauvegarde_stat = open("stats.txt", "w", encoding='utf8')
        sauvegarde_stat.write(f"{meilleur_temps}")
        sauvegarde_stat.write(f"Moyennes des equipes: \n"
                              f"{liste_moyenne_croissant}")
        sauvegarde_stat.close()

        
    elif choix == 3:
        # Afficher l'équipe avec les coureurs les plus similaires
        print("jddj")
        
    elif choix == 4:

        ajout_faute = open("stats.txt", "a", encoding='utf8')

        selection_equipe_faute = int(input("Liste des équipes: \n"
                                           "1 pour Équipe A \n"
                                           "2 pour Équipe B \n"
                                           "3 pour Équipe C \n"
                                           "4 pour Toutes les équipes \n"
                                           "Choisissez pour qui voulez-vous attrier une faute?:"))
        if selection_equipe_faute == 1:
            ajout_faute.write("\n1 faute pour l'équipe A")
        elif selection_equipe_faute == 2:
            ajout_faute.write("\n1 faute pour l'équipe B")
        elif selection_equipe_faute == 3:
            ajout_faute.write("\n1 faute pour l'équipe C")
        elif selection_equipe_faute == 4:
            ajout_faute.write("\n1 faute pour toutes les équipes")
        else:
            print("Entrez invalide")
    else:
        print("Mauvais choix")
    return

execution_user(liste_equipe)