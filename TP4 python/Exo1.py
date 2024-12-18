nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

# Création d'une liste vide pour stocker les résultats
table = []

# Remplissage de la liste avec les résultats de la table de multiplication
for i in range(10):  # On fait la table de multiplication de 0 à 9
    table.append(nombre * i, 1)  # On arrondit à 1 décimale

# Affichage des résultats
for i in range(10):
    print(f"{nombre} * {i} = {table[i]}")
