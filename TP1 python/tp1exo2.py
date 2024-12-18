# Interaction avec l'utilisateur pour saisir le jour, l'heure et les minutes
jour = int(input("Saisir le jour du mois (1 à 31) : "))  # Jour entre 1 et 31
heure = int(input("Saisir l'heure (0 à 23) : "))  # Heure entre 0 et 23
minute = int(input("Saisir les minutes (0 à 59) : "))  # Minutes entre 0 et 59

# Calcul du nombre de minutes écoulées depuis le début du mois
minutes_ecoulees = (jour - 1) * 1440 + heure * 60 + minute  # 1440 minutes dans un jour (24h * 60min)

# Affichage du résultat
print("Le nombre de minutes écoulées depuis le début du mois est :", minutes_ecoulees)
