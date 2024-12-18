def is_leap_year(year):
    """Vérifie si une année est bissextile."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def verify_date(date):
    """Vérifie si la date au format jjmmaaaa est valide."""
    
    # Vérification du format : la chaîne doit être composée de 8 chiffres
    if len(date) != 8 or not date.isdigit():
        print("Erreur : La date doit être sous la forme jjmmaaaa avec des chiffres uniquement.")
        return
    
    # Extraction des parties de la date
    jour = int(date[:2])  # Les 2 premiers caractères pour le jour
    mois = int(date[2:4])  # Les 2 caractères suivants pour le mois
    annee = int(date[4:])  # Les 4 derniers caractères pour l'année
    
    # Vérification du mois
    if mois < 1 or mois > 12:
        print(f"Erreur : Le mois {mois} n'est pas valide. Il doit être entre 01 et 12.")
        return
    
    # Vérification du jour en fonction du mois
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        # Ces mois ont 31 jours
        if jour < 1 or jour > 31:
            print(f"Erreur : Le jour {jour} n'est pas valide pour le mois {mois:02d}. Ce mois a 31 jours.")
            return
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        # Ces mois ont 30 jours
        if jour < 1 or jour > 30:
            print(f"Erreur : Le jour {jour} n'est pas valide pour le mois {mois:02d}. Ce mois a 30 jours.")
            return
    elif mois == 2:
        # Février, vérifier selon l'année bissextile ou non
        if is_leap_year(annee):
            if jour < 1 or jour > 29:
                print(f"Erreur : Le jour {jour} n'est pas valide pour le mois 02. Février {annee} a 29 jours.")
                return
        else:
            if jour < 1 or jour > 28:
                print(f"Erreur : Le jour {jour} n'est pas valide pour le mois 02. Février {annee} a 28 jours.")
                return
    
    # Si toutes les vérifications sont passées
    print(f"La date {date} est valide.")

# Demande de saisie de l'utilisateur
date_saisie = input("Veuillez entrer une date au format jjmmaaaa : ")
verify_date(date_saisie)


