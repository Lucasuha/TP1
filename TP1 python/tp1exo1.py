# Initialisation des variables
nom = "Toto"            # chaîne de caractères pour le nom
prenom = "Titi"         # chaîne de caractères pour le prénom
math = 14.5             # réel pour la note en mathématiques
anglais = 12.0          # réel pour la note d'anglais
info = 13.0             # réel pour la note en informatique
promotion = 2023        # entier pour l'année de promotion

# Calcul de la moyenne des trois notes
moy = (math + anglais + info) / 3

# 1) Affichage du type de chaque variable
print(f"Type de 'nom' : {type(nom)}")
print(f"Type de 'prenom' : {type(prenom)}")
print(f"Type de 'math' : {type(math)}")
print(f"Type de 'anglais' : {type(anglais)}")
print(f"Type de 'info' : {type(info)}")
print(f"Type de 'promotion' : {type(promotion)}")
print(f"Type de 'moy' : {type(moy)}")

# 2) Affichage de la moyenne de manière formatée
print(f"L'étudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {moy:.1f}")
