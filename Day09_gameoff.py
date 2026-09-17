import sys
import random
from datetime import date


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

# Récupération du nom du fichier
if len(sys.argv) < 2:
    print("Error: missing argument")
    sys.exit()

fichier_mots = sys.argv[1]

highscore = open("highscore.txt", "r")
score = highscore.read()

if score == "":
    print("Aucun record pour le moment.")
else:
    print("Record actuel :", score) 
date_jeu = date.today()


# Ouverture du fichier
try:
    fichier = open(fichier_mots, "r")
except FileNotFoundError:
    print("Error: file not found")
    sys.exit()

# Récupération des mots
mots = fichier.readlines()

# Suppression des \n
for i in range(len(mots)):
    mots[i] = mots[i].strip()

if len(mots) == 0:
    print("Error: empty word list")
    sys.exit()

# Choix aléatoire du mot
mot = random.choice(mots)

afficher_tirets(mot)
print()

penalites = 0
tentatives = 0
lettres_trouvees = []

while penalites <= 12:
    proposition = input("Propose une lettre ou le mot entier : ").lower()
    tentatives += 1

    if proposition == "":
        print("Tu dois entrer une lettre ou un mot.")
        continue

    if len(proposition) > 1:
        if proposition == mot:
            print("Bien joué!!! Un vrai Madrilène toi")
            break
        else:
            penalites += 5
            print("Mauvais mot!!! Barç....")
            print("Pénalités :", penalites)

    else:
        if proposition in mot:
            lettres_trouvees.append(proposition)
            print("Bonne lettre. Bien joué !")
        else:
            penalites += 1
            print("Mauvaise lettre. Tu es barcelonais toi... !")
            print("Pénalités :", penalites)

    afficher_mot(mot, lettres_trouvees)
    print()

    if set(mot) == set(lettres_trouvees):
        print("VICTOIRE!!! HALLA MADRID mon frerot")
        break


if penalites > 12:
    print("Tu as PERDU!!!! BARCELONAIS")

print("Nombre de tentatives :", tentatives)
print("Date :", date_jeu)

ancien_score = int(score.split("|")[0])

if tentatives < ancien_score:
    highscore = open("highscore.txt", "w")
    highscore.write(str(tentatives) + "|" + str(date_jeu))
    highscore.close()
    print("Best ever! Nouveau record !")
else:
    print("Record non battu.")


######################  FIN DU JEU ########################