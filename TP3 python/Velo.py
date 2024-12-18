def calculer_prix(debut, fin):
    # Vérification des heures de location et des tarifs
    prix = 0
    for i in range(debut, fin):
        if 0 <= i < 7 or 17 <= i < 24:
            prix += 1  # Tarif 1 euro par heure
        elif 7 <= i < 17:
            prix += 2  # Tarif 2 euros par heure
    return prix

def main():
    while True:
        # Demande des heures de début et de fin
        debut = int(input("Entrez l'heure de début de la location: "))
        fin = int(input("Entrez l'heure de fin de la location: "))

        # Validation des entrées
        if not (0 <= debut <= 24 and 0 <= fin <= 24):
            print("Les heures doivent être comprises entre 0 et 24 !")
            continue
        if debut == fin:
            print("Attention ! l'heure de fin est identique à l'heure de début.")
            continue
        if debut > fin:
            print("Attention ! le début de la location est après la fin ...")
            continue

        # Calcul du prix de la location
        prix = calculer_prix(debut, fin)

        # Affichage du prix
        print(f"Le prix de la location est : {prix} euros.")
        break

main()
