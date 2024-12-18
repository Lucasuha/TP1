L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Complétez le programme à partir d'ici.

# Créer un dictionnaire pour compter les occurrences des éléments dans la liste
frequency = {}

# Parcourir la liste L1 et compter les occurrences
for num in L1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Variables pour suivre l'élément le plus fréquent
most_frequent_num = None
max_count = 0

# Parcourir la liste pour trouver l'élément le plus fréquent
for num in L1:
    if frequency[num] > max_count:
        most_frequent_num = num
        max_count = frequency[num]

# Affichage du résultat
print(f"Le nombre le plus frequent dans la liste est le : {most_frequent_num} ({max_count} x)")

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Ne rien modifier après cette ligne.
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
