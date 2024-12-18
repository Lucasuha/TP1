import os
import datetime

# Fonction pour vérifier si le fichier existe et obtenir sa taille
def obtenir_taille_et_date(fichier):
    if os.path.isfile(fichier):
        taille = os.path.getsize(fichier)
        # Récupérer la date de dernière modification du fichier
        date_modification = os.path.getmtime(fichier)
        # Convertir le timestamp en un format lisible
        date_modification_formatee = datetime.datetime.fromtimestamp(date_modification).strftime('%Y-%m-%d %H:%M:%S')
        return taille, date_modification_formatee
    else:
        return None, None

# Demander à l'utilisateur d'entrer les deux noms de fichiers
fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

# Obtenir les tailles et dates de modification des deux fichiers
taille1, date1 = obtenir_taille_et_date(fichier1)
taille2, date2 = obtenir_taille_et_date(fichier2)

# Vérifier si les fichiers existent
if taille1 is not None and taille2 is not None:
    # Afficher les tailles des fichiers
    print(f"Le fichier '{fichier1}' fait {taille1} octets et a été modifié le {date1}.")
    print(f"Le fichier '{fichier2}' fait {taille2} octets et a été modifié le {date2}.")
    
    # Comparer les dates de modification pour savoir lequel est le plus récent
    if date1 > date2:
        print(f"Le fichier '{fichier1}' est le plus récent.")
    elif date2 > date1:
        print(f"Le fichier '{fichier2}' est le plus récent.")
    else:
        print("Les deux fichiers ont été modifiés à la même date et heure.")
else:
    if taille1 is None:
        print(f"Le fichier '{fichier1}' n'existe pas.")
    if taille2 is None:
        print(f"Le fichier '{fichier2}' n'existe pas.")
