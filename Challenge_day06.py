import time

def fast_power(base, exposant):

    if exposant == 0:
        return 1

    elif exposant % 2 == 0:
        resultat = fast_power(base, exposant // 2)
        return resultat * resultat

    elif exposant % 2 != 0:
        return base * fast_power(base, exposant - 1)
debut = time.time()
resultat = fast_power(42, 84)
fin = time.time()
temps = fin - debut
print("42^84 =", resultat)
print("Temps :", temps, "secondes")        

debut = time.time()
resultat = fast_power(42, 168)
fin = time.time()
temps = fin - debut
print("42^168 =", resultat)
print("Temps :", temps, "secondes")   

debut = time.time()
resultat = fast_power(420, 16877)
fin = time.time()
temps = fin - debut
print("420^16877 =", resultat)
print("Temps :", temps, "secondes")  