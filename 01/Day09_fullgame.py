import pygame
import random
import sys

pygame.init()

# -----------------------------
# FENETRE
# -----------------------------

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")

font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 70)

# -----------------------------
# MOT
# -----------------------------

try:
    fichier = open("mots.txt", "r")
    mots = fichier.readlines()
    fichier.close()
except FileNotFoundError:
    print("Error: file not found")
    pygame.quit()
    sys.exit()

mots_propres = []

for mot in mots:
    mot = mot.strip().lower()

    if mot != "" and mot.isalpha():
        mots_propres.append(mot)

if len(mots_propres) == 0:
    print("Error: empty word list")
    pygame.quit()
    sys.exit()

mot = random.choice(mots_propres)

# -----------------------------
# JEU
# -----------------------------

lettres_trouvees = []
lettres_fausses = []
erreurs = 0
max_erreurs = 6

running = True
victoire = False
defaite = False

while running:

    # -----------------------------
    # EVENEMENTS
    # -----------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if not victoire and not defaite:

                lettre = event.unicode.lower()

                if lettre.isalpha() and len(lettre) == 1:

                    if lettre in lettres_trouvees or lettre in lettres_fausses:
                        continue

                    if lettre in mot:
                        lettres_trouvees.append(lettre)

                    else:
                        lettres_fausses.append(lettre)
                        erreurs += 1

                    # Vérification victoire
                    victoire = True

                    for lettre_mot in mot:
                        if lettre_mot not in lettres_trouvees:
                            victoire = False
                            break

                    # Vérification défaite
                    if erreurs >= max_erreurs:
                        defaite = True
                        victoire = False

            else:

                # R pour recommencer
                if event.key == pygame.K_r:
                    mot = random.choice(mots_propres)
                    lettres_trouvees = []
                    lettres_fausses = []
                    erreurs = 0
                    victoire = False
                    defaite = False

    # -----------------------------
    # AFFICHAGE
    # -----------------------------

    screen.fill((0, 0, 0))

    # Titre
    titre = big_font.render("HANGMAN", True, (255, 255, 255))
    screen.blit(titre, (190, 30))

    # Mot caché
    affichage_mot = ""

    for lettre in mot:

        if lettre in lettres_trouvees:
            affichage_mot += lettre + " "

        else:
            affichage_mot += "_ "

    texte_mot = big_font.render(affichage_mot, True, (255, 255, 255))
    screen.blit(texte_mot, (120, 150))

    # Erreurs
    texte_erreurs = font.render(
        "Erreurs : " + str(erreurs) + " / " + str(max_erreurs),
        True,
        (255, 255, 255)
    )
    screen.blit(texte_erreurs, (180, 250))

    # Lettres fausses
    texte_fausses = font.render(
        "Fausses : " + " ".join(lettres_fausses),
        True,
        (255, 255, 255)
    )
    screen.blit(texte_fausses, (120, 310))

    # -----------------------------
    # PENDU
    # -----------------------------

    # Potence
    pygame.draw.line(screen, (255, 255, 255), (100, 500), (250, 500), 5)
    pygame.draw.line(screen, (255, 255, 255), (175, 500), (175, 350), 5)
    pygame.draw.line(screen, (175, 255, 255), (175, 350), (250, 350), 5)
    pygame.draw.line(screen, (255, 255, 255), (250, 350), (250, 380), 5)

    # Tête
    if erreurs >= 1:
        pygame.draw.circle(screen, (255, 255, 255), (250, 405), 25, 4)

    # Corps
    if erreurs >= 2:
        pygame.draw.line(screen, (255, 255, 255), (250, 430), (250, 470), 5)

    # Bras gauche
    if erreurs >= 3:
        pygame.draw.line(screen, (255, 255, 255), (250, 440), (220, 460), 5)

    # Bras droit
    if erreurs >= 4:
        pygame.draw.line(screen, (255, 255, 255), (250, 440), (280, 460), 5)

    # Jambe gauche
    if erreurs >= 5:
        pygame.draw.line(screen, (250, 470), (220, 500), 5)

    # Jambe droite
    if erreurs >= 6:
        pygame.draw.line(screen, (250, 470), (280, 500), 5)

    # -----------------------------
    # FIN DE PARTIE
    # -----------------------------

    if victoire:

        texte = font.render(
            "VICTOIRE ! Appuie sur R pour rejouer",
            True,
            (255, 255, 255)
        )
        screen.blit(texte, (80, 550))

    elif defaite:

        texte = font.render(
            "PERDU ! Mot : " + mot,
            True,
            (255, 255, 255)
        )
        screen.blit(texte, (130, 550))

        texte2 = font.render(
            "Appuie sur R pour rejouer",
            True,
            (255, 255, 255)
        )
        screen.blit(texte2, (160, 90))

    pygame.display.flip()

pygame.quit()