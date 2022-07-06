import random
users_life = 50
ennemy_life = 50
ennemy_attack = random.randint(5,12)
users_attack =  random.randint(5,10)
potions_heal = random.randint(15,50)
potions = 3
tour_ennemy = ''
choices =["1","2"]
while True: 
    ennemy_attack = random.randint(5,12)
    users_attack =  random.randint(5,10)
    potions_heal = random.randint(15,50)
    users_choice = input("Souhaitez-vous attaquer(1) ou utiliser une potion(2)")
    if users_choice not in choices:
        print("Il vous faut choisir entre attaquer en tapant 1 ou prendre une potion avec 2!")
    else:
        if users_choice == "1":
            print("Vous avez infliger,",users_attack,"dégats à l'ennemi!")
            ennemy_life = ennemy_life - users_attack
        elif users_choice == "2":
            potions = potions - 1
            print("Il vous reste",potions,"potions.")
            if potions > 0:
                print("Vous avez reçu",potions_heal,"points de vie en +")        
                users_life = users_life + potions_heal
            elif potions <= 0:
                print("Désolé, vous n'avez plus de potions!")
        tour_ennemy = ennemy_attack
        users_life = users_life - ennemy_attack
        print("L'ennemi vous a infliger,", ennemy_attack,"dégats!")
        print("L'ennemi lui reste",ennemy_life,"points de vie.")
        print("Il vous reste",users_life,"points de vie.")
        if users_life <= 0 or ennemy_life <0 :#Double condition d'arrêt OK :D
            break
if users_life <= 0:
    print("Vous avez perdu..")
    print("Fin du jeu.")
else:
    print("Bravo vous avez gagné!!")
    print("Fin du gameeeeeeeeeeee")
