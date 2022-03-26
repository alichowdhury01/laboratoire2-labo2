# Étape 1

# Chaque variable permet de lire leur base de donnée




# Étape 2

def user_menu():
    
    print("1 pour Afficher les statistiques")
    print("2 pour Sauvegarder les statistiques")
    print("3 pour Afficher l'équipe avec les coureurs les plus similaires")
    print("4 pour Ajouter une faute à une équipe")
    return 

user_menu()

choix = int(input("Veuillez faire votre choix: "))

# Étape 3

# Vous devez afficher les statistiques suivantes :

#   * Équipe ayant le coureur le plus rapide et le temps de ce dernier.
#   * Temps moyens par équipe présenté en ordre croissant, donc de l'équipe la plus rapide à la plus lente. 
#     Vous devez y afficher le nom de l'équipe et leur temps de course moyen.

def afficher_stats():

    f1 = open("data1.txt", "r", encoding='utf8')
    #f2 = open("data2.txt", "r", encoding='utf8')
    #f3 = open("data3.txt", "r", encoding='utf8')

    

    if choix == 1:     
        
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

afficher_stats()