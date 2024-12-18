# tp1exo3.py

# Demande à l'utilisateur de saisir le jour, l'heure et les minutes avec des messages personnalisés
jour = int(input("Veuillez entrer le jour du mois (1 à 31) : "))  # Saisie du jour
heure = int(input("Veuillez entrer l'heure (0 à 23) : "))  # Saisie de l'heure
minute = int(input("Veuillez entrer les minutes (0 à 59) : "))  # Saisie des minutes

# Calcul du nombre de minutes écoulées depuis le début du mois
# 1 jour = 1440 minutes (24h * 60min)
minutes_ecoulees = (jour - 1) * 1440 + heure * 60 + minute  # Calcul des minutes

# Affichage du résultat
print(f"Le nombre total de minutes écoulées depuis le début du mois est : {minutes_ecoulees} minutes.")
