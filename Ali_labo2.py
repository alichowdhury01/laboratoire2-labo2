# Étape 1

# Chaque variable permet de lire leur base de donnée
bdd_lion = open("data1.txt", "r", encoding='utf8')
bdd_lion_read = bdd_lion.read()
bdd_rocket = open("data2.txt", "r", encoding='utf8')
bdd_rocket_read = bdd_rocket.read()
bdd_aigle = open("data3.txt", "r", encoding='utf8')
bdd_aigle_read = bdd_aigle.read()

# Étape 2

def user_menu():
    
    print("1 pour Afficher les statistiques")
    print("2 pour Sauvegarder les statistiques")
    print("3 pour Afficher l'équipe avec les coureurs les plus similaires")
    print("4 pour Ajouter une faute à une équipe.")
    return 

#user_menu()

choix = int(input("Veuillez faire votre choix: "))

# Étape 3

# Vous devez afficher les statistiques suivantes :

#   * Équipe ayant le coureur le plus rapide et le temps de ce dernier.
#   * Temps moyens par équipe présenté en ordre croissant, donc de l'équipe la plus rapide à la plus lente. 
#     Vous devez y afficher le nom de l'équipe et leur temps de course moyen.

def afficher_stats():

    if choix == 1:
        #fait choix 1

        print("sksks")
    elif choix == 2:
        #fait choix 2
        print("jdjd")
    elif choix == 3:
        # fait chox 3
        print("jddj")
    elif choix == 4:
        # fait choix 4
        print("sjs")
    else:
        print("Mauvais choix")
    return

afficher_stats()