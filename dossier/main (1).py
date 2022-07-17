import sys
import json
from regex import W

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

with open("liste.json","r") as file:
    LISTE = json.load(file)
while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        #LISTE.append(item)
        with open("liste.json","r",encoding = "utf-8") as file:
            LISTE = json.load(file)   
        LISTE.append(item)   
        with open("liste.json","w",encoding = "utf-8") as file:
            json.dump(LISTE, file, indent=2)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        with open("liste.json","r",encoding = "utf-8") as file:
            LISTE = json.load(file) 
        if item in LISTE:
            LISTE.remove(item)
            with open("liste.json","w",encoding = "utf-8") as file:
                json.dump(LISTE, file, indent=2)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if LISTE: #La je veux dire si elle a aucun élém voila quoi
            print("Voici le contenu de votre liste :")
            with open("liste.json","r",encoding = "utf-8") as file:
                LISTE = json.load(file)
                print(LISTE)
        else:  
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":# Vider la liste
        with open("liste.json","r",encoding = "utf-8") as file:
            LISTE = json.load(file)   
        LISTE.clear()   
        with open("liste.json","w",encoding = "utf-8") as file:
            json.dump(LISTE, file, indent=2)
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        sys.exit()

    print("-" * 50)

#Stocker un fichier dans une variable(chemin?) 
#Sauvegarder un fichier
#Souci si y'a aucun élement dans le fichier json pour le #3
#le fichier json prends une liste c'est évident.
#Donc c surtout comment gérer un fichier un json avec les listes 
"""
for i, item in enumerate(LISTE, 1):
print(f"{i}. {item})
"""






