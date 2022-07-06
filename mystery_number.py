import random
mystery_number = random.randint(1,100)
essai = ''
for i in range(10,-1,-1):
    print("Il te reste", i, "essai")
    essai = input("Try to find the mystery number !: ")
    if i == 0:
        print("Vous avez perdu ! Le nombre mystère était :",mystery_number,"!")
    elif not essai.isdigit():
        print('The mystery "NUMBER" so TYPE A NUMBER please ! :D ')
        essai = input("Try to find the mystery number !: ")
    elif int(essai) < int(mystery_number) :
        print("The myster number is bigger!")
    elif int(essai) > int(mystery_number) :
        print("The mystery number is smaller!")
    if int(essai) == int(mystery_number):   
        break
print("Vous avez trouvé!!")     
print("Le nombre mystère était bien,",mystery_number,"!")
print("Vous avez trouvé le nombre mystère en",i,"essais!")
