# a) Définition de la fonction ajouter_elt avec des valeurs par défaut
def ajouter_elt(lst=[0, 1, 2], elt=3):
    print(f"ID de lst au début: {id(lst)}")  # Affichage de l'ID de lst avant modification
    lst.append(elt)  # Ajoute elt à la liste lst
    print(f"ID de lst après modification: {id(lst)}")  # Affichage de l'ID de lst après modification
    return lst

# Premier appel sans arguments : utilise les valeurs par défaut
print(ajouter_elt())  # lst = [0, 1, 2], elt = 3, résultat = [0, 1, 2, 3]

# Deuxième appel sans arguments : utilise les mêmes valeurs par défaut
print(ajouter_elt())  # lst devient [0, 1, 2, 3, 3]

# b) Définition de la fonction ajouter_carac avec des valeurs par défaut pour les chaînes
def ajouter_carac(ch="abc", elt="d"):
    print(f"ID de ch au début: {id(ch)}")  # Affichage de l'ID de ch avant concaténation
    print(f"ID de elt au début: {id(elt)}")  # Affichage de l'ID de elt avant concaténation
    result = ch + elt  # Concaténation de ch et elt
    print(f"ID du résultat: {id(result)}")  # Affichage de l'ID du résultat
    return result

# Premier appel sans arguments : utilise les valeurs par défaut
print(ajouter_carac())  # ch = "abc", elt = "d", résultat = "abcd"

# Deuxième appel sans arguments : utilise les mêmes valeurs par défaut
print(ajouter_carac())  # ch = "abc", elt = "d", résultat = "abcd"
