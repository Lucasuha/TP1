# a) Initialisation de la liste avec trois zéros
L1 = [0] * 3
print("Liste initiale :", L1)
print("Type de L1 :", type(L1))
print("ID de L1 :", id(L1))

# b) Affichage des valeurs, types et identifiants des éléments de la liste
for i in L1:
    print(f"Valeur: {i}, Type: {type(i)}, ID: {id(i)}")

# c) Modification de l'élément en deuxième position et affichage des détails
L1[1] += 1  # Incrémente l'élément à l'index 1
print("\nListe après modification :", L1)
print("Type de L1 après modification :", type(L1))
print("ID de L1 après modification :", id(L1))

# d) Vérification des identifiants des éléments après modification
for i in L1:
    print(f"Valeur: {i}, ID: {id(i)}")

# e) Test avec une chaîne de caractères
chaine = "machaine"
print("\nID de la chaîne :", id(chaine))

# Affichage de l'identifiant de chaque caractère de la chaîne
for char in chaine:
    print(f"Caractère: {char}, ID: {id(char)}")
