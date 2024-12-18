# Taille maximale des vecteurs
nMax = 4

# Déclaration des listes pour les vecteurs
v1 = []
v2 = []

# Demande de la taille des vecteurs et vérification
while True:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    if 1 <= n <= nMax:
        break
    else:
        print(f"Erreur : la taille doit être comprise entre 1 et {nMax}.")

# Saisie des composantes du premier vecteur v1
print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input(f"v1[{i}] = ")))

# Saisie des composantes du second vecteur v2
print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input(f"v2[{i}] = ")))

# Calcul du produit scalaire
produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

# Affichage du résultat
print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire:.1f}")
