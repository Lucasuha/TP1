import random

# Fonction pour générer un tableau de 'nbr' valeurs aléatoires entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

# Fonction pour compter les valeurs inférieures à 'vseuil' dans 'table'
def combienInferieur(table, vseuil):
    return sum(1 for val in table if val < vseuil)

# Programme principal interactif
# Demander à l'utilisateur de préciser le nombre de valeurs à générer et l'intervalle
nb = int(input("Combien de nombres souhaitez-vous générer ? "))
vmin = int(input("Entrez la valeur minimale de l'intervalle : "))
vmax = int(input("Entrez la valeur maximale de l'intervalle : "))

# Demander si l'utilisateur veut préciser le seuil
reponse_seuil = input("Vous voulez préciser le seuil ? (Oui/Non) : ").strip().lower()

# Si l'utilisateur veut préciser le seuil
if reponse_seuil in ['oui', 'o']:
    seuil = int(input("Entrez le seuil : "))
else:
    # Sinon, appliquer le seuil par défaut de 30
    seuil = 30

# Générer le tableau et trier les valeurs
tab = generer(nb, vmin, vmax)
tab.sort()

# Afficher les résultats
print(f"Tableau généré : {tab}")
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
