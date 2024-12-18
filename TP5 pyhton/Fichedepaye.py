def calculer_salaire(heures_travaillees, salaire_horaire):
    # Initialiser le salaire total à 0
    salaire_total = 0

    # Si l'ouvrier a travaillé 160 heures ou moins
    if heures_travaillees <= 160:
        salaire_total = heures_travaillees * salaire_horaire

    # Si l'ouvrier a travaillé entre 161 et 200 heures
    elif heures_travaillees <= 200:
        salaire_total = 160 * salaire_horaire  # Pour les 160 premières heures
        heures_supplementaires = heures_travaillees - 160
        salaire_total += heures_supplementaires * salaire_horaire * 1.25  # Majoration de 25%

    # Si l'ouvrier a travaillé plus de 200 heures
    else:
        salaire_total = 160 * salaire_horaire  # Pour les 160 premières heures
        salaire_total += 40 * salaire_horaire * 1.25  # Pour les heures entre 161 et 200
        heures_supplementaires = heures_travaillees - 200
        salaire_total += heures_supplementaires * salaire_horaire * 1.5  # Majoration de 50%

    return salaire_total

# Exemple d'utilisation du programme
# Demander le nombre d'heures travaillées et le salaire horaire
heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

# Calculer le salaire
salaire = calculer_salaire(heures_travaillees, salaire_horaire)

# Afficher le résultat
print(f"Le salaire total est : {salaire:.2f} €")
