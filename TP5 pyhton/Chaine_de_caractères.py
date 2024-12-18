# Fonction pour calculer la taille de la chaîne
def taille_chaine(T):
    taille = 0
    for caractere in T:
        taille += 1
    return taille

# Fonction pour calculer le pourcentage de voyelles dans la chaîne
def pourcentage_voyelles(T):
    voyelles = "aeiouyAEIOUY"
    compteur_voyelles = 0
    total_caracteres = 0
    
    for caractere in T:
        if caractere != '':  # Ignore le caractère vide ou de fin de chaîne
            total_caracteres += 1
            if caractere in voyelles:
                compteur_voyelles += 1
    
    if total_caracteres == 0:
        return 0
    return (compteur_voyelles / total_caracteres) * 100

# Fonction pour tester si "wagon" est une sous-chaîne de T
def est_sous_chaine(T, sous_chaine):
    n = len(T)
    m = len(sous_chaine)
    for i in range(n - m + 1):
        if T[i:i+m] == sous_chaine:
            return i  # Retourne l'index de la première occurrence
    return -1  # Si "wagon" n'est pas trouvé

# Fonction pour compter le nombre d'occurrences de "wagon" dans T
def compter_occurrences(T, sous_chaine):
    count = 0
    n = len(T)
    m = len(sous_chaine)
    for i in range(n - m + 1):
        if T[i:i+m] == sous_chaine:
            count += 1
    return count

# Exemple d'utilisation du programme
# Demander la chaîne de caractères à l'utilisateur
T = input("Entrez une chaîne de caractères : ")

# 1. Calculer la taille de la chaîne
taille = taille_chaine(T)
print(f"La taille de la chaîne est : {taille}")

# 2. Calculer le pourcentage de voyelles
pourcentage = pourcentage_voyelles(T)
print(f"Le pourcentage de voyelles est : {pourcentage:.2f}%")

# 3. Tester si "wagon" est une sous-chaîne et donner l'index de la première occurrence
sous_chaine = "wagon"
index_premiere_occurrence = est_sous_chaine(T, sous_chaine)
if index_premiere_occurrence != -1:
    print(f"Le mot 'wagon' est trouvé à l'index {index_premiere_occurrence}")
else:
    print("Le mot 'wagon' n'est pas une sous-chaîne.")

# 4. Compter le nombre d'occurrences de "wagon"
nombre_occurrences = compter_occurrences(T, sous_chaine)
print(f"Le mot 'wagon' apparaît {nombre_occurrences} fois dans la chaîne.")
