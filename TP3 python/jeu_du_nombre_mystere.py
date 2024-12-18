import random

valeur_mystere = random.randint(0, 100)
compteur = 0

while True:
    NB = int(input("Devinez la valeur mystère (entre 0 et 100) : "))
    compteur += 1

    if NB < valeur_mystere:
        print("La valeur est plus grande.")
    elif NB > valeur_mystere:
        print("La valeur est plus petite.")
    else:
        print(f"Bravo ! Vous avez trouvé la valeur mystère {valeur_mystere} en {compteur} tentatives.")
        break  

