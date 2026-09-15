import random
from english_words import english_words_lower_set

def choisir_mot():
    return random.choice(list(english_words_lower_set))

def afficher_tirets(mot):
    for i in range(len(mot)):
        print("_ ", end="")

def afficher_mot(mot, lettres_trouvees):
    for lettre in mot:
        if lettre in lettres_trouvees:
            print(lettre, end=" ")
        else:
            print("_ ", end="")

                 ######################  LE JEU COMMENCE ICI ########################

mot = choisir_mot()

afficher_tirets(mot)
print()

penalites = 0
lettres_trouvees = []

while penalites <= 12:
    proposition = input("Propose une lettre ou le mot entier : ").lower()

    if proposition == "":
       print("Tu dois entrer une lettre ou un mot.")
       continue

    if len(proposition) > 1:
        if proposition == mot:
            print("You win!!!")
            break
        else:
            penalites += 5
            print("Mauvais mot !")
            print("Pénalités :", penalites)

    else:
        if proposition in mot:
            lettres_trouvees.append(proposition)
            print("Bonne lettre. Bien joué !")
        else:
            penalites += 1
            print("Mauvaise lettre. Essaie encore !")
            print("Pénalités :", penalites)

    afficher_mot(mot, lettres_trouvees)
    print()

    if set(mot) == set(lettres_trouvees):
        print("You win!!!")
        break


if penalites > 12:
    print("You lose!")


                        ######################  FIN DU JEU ########################