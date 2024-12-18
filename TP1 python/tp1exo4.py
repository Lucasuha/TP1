# tp1exo4.py

# Demander à l'utilisateur de saisir le nombre de minutes écoulées depuis le début du mois
minutes_ecoulees = int(input("Veuillez entrer le nombre de minutes écoulées depuis le début du mois : "))

# Calculer le jour du mois à partir des minutes écoulées
# 1 jour = 1440 minutes (24h * 60min)
jour_du_mois = (minutes_ecoulees // 1440) + 1  # Diviser par 1440 pour obtenir le jour

# Afficher le jour du mois associé
print(f"Le jour du mois associé aux {minutes_ecoulees} minutes écoulées est le jour {jour_du_mois}.")
