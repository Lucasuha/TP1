# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0

# Déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

# Demande des notes pour chaque étudiant et calcul de la somme des notes
for i in range(nombreEtudiants):
    while True:  # On répète jusqu'à obtenir une note valide
        try:
            note = float(input(f"Note étudiant {i} : "))  # Demande la note de l'étudiant i
            if 0 <= note <= 20:  # Vérifie que la note est valide
                notes.append(note)  # Ajoute la note à la liste
                moyenne += note  # Ajoute la note à la somme pour calculer la moyenne
                break  # Sortie de la boucle si la note est valide
            else:
                print("Erreur : La note doit être entre 0 et 20.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

# Calcul de la moyenne de la classe
moyenne /= nombreEtudiants

# Affichage de la moyenne de la classe
print("Moyenne de classe :",moyenne,)

# Affichage des écarts à la moyenne pour chaque étudiant
print("\nNuméro de l’Etudiant | note | écart à la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne  # Calcul de l'écart à la moyenne
    print(f"{i} | {notes[i]:.1f} | {ecart:.2f}")














