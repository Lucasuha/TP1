# Initialisation des compteurs
count_moinsde10 = 0
count_10a14 = 0
count_15etplus = 0

# Lecture des 10 valeurs
for i in range(10):
    while True:
        valeur = float(input(f"Entrez la valeur {i + 1} (comprise entre 0 et 20) : "))
        if 0 <= valeur <= 20:
            break  # Valeur valide, on sort de la boucle
        else:
            print("La valeur doit être comprise entre 0 et 20. Essayez encore.")

    # Incrémentation des compteurs selon la valeur entrée
    if valeur < 10:
        count_moinsde10 += 1
    elif 10 <= valeur < 15:
        count_10a14 += 1
    else:
        count_15etplus += 1

# Affichage des résultats
print("\nRésultats :")
print(f"Nombre de valeurs inférieures à 10 : {count_moinsde10}")
print(f"Nombre de valeurs comprises entre 10 et 14 : {count_10a14}")
print(f"Nombre de valeurs supérieures ou égales à 15 : {count_15etplus}")
