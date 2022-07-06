import sys
from traceback import print_tb
menu = Choisissez l'action souhaitée ! :
        1: Ajouter un élement à la liste.
        2: Retirer un élement de la liste.
        3: Afficher la liste.
        4: Vider la liste.
        5: Quitter
        Le numéro de votre choix : 
   #Menu OK    
choix_menu = ["1","2","3","4","5"]
list_user= []
mot_user = ''
mot_a_enlever = ''

while True: # Quand on veut faire une boucle infinie et que la condition d'arrêt est dans la boucle.
    users_choice = input(menu)
    if users_choice not in choix_menu:
        print("Je n'ai pas compris! Choisissez un nombre entre 1 et 5!")
        continue 
    if users_choice == "1":
        mot_user = (input("Entrer un mot que vous voulez rajouter à votre liste :"))
        list_user.append(mot_user)
        print("Le mot",mot_user,"a bien été ajouté à la liste!")
    if users_choice == "2":
        mot_a_enlever = (input("Entrer un élément à retirer de la liste de courses: "))
        if mot_a_enlever in list_user: 
            list_user.remove(mot_a_enlever)
            print("Votre mot à bien été retiré de votre liste!")
        else:
            print("Votre mot n'existe pas veuillez entrer un élément existant.")    
    if users_choice == "3":
        print("Voici le contenu de la liste !")
        print(list_user)
        if len(list_user) == 0:
            print("Votre liste ne contient aucun élement")
    if users_choice == "4":
        list_user.clear()
        print("Votre liste à bien été vidée !")
    if users_choice == "5":
        print("A bientôt :3 !")
        sys.exit()
