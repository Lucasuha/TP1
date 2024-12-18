L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Complétez le programme à partir d'ici.

# Variables pour suivre l'élément le plus fréquent
most_frequent_num = None
max_count = 0

# Parcourir la liste et utiliser count() pour trouver l'élément le plus fréquent
for num in L1:
    count = L1.count(num)         # Utiliser la méthode count() pour compter le nombre d'occurrences de num dans la liste

    if count > max_count:         # Si ce nombre d'occurrences est supérieur au maximum actuel, on met à jour
        most_frequent_num = num
        max_count = count

# Affichage du résultat
print(f"Le nombre le plus frequent dans la liste est le : {most_frequent_num} ({max_count} x)")

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Ne rien modifier après cette ligne.
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
