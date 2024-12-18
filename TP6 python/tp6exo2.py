# a) Déclaration de la fonction ajouter_elt
def ajouter_elt(lst, elt):
    lst.append(elt)  # Ajoute l'élément à la fin de la liste
    return lst  # Retourne la liste modifiée

# b) Création de la liste lst1 initialisée avec [0, 1, 2]
lst1 = [0, 1, 2]
# Création de la liste lst2 en utilisant la fonction ajouter_elt
lst2 = ajouter_elt(lst1, len(lst1))  # Ajoute la longueur de lst1 à lst1

# c) Affichage du contenu, type et identifiant des listes
print(f"Liste lst1 : {lst1}")
print(f"Type de lst1 : {type(lst1)}")
print(f"ID de lst1 : {id(lst1)}")

print(f"Liste lst2 : {lst2}")
print(f"Type de lst2 : {type(lst2)}")
print(f"ID de lst2 : {id(lst2)}")
