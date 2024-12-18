# Fonction pour obtenir les notes et les coefficients
def obtenir_notes_et_coefficients():
    notes = []
    coefficients = []
    for i in range(1, 6):  # Pour les 5 modules
        entree = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
        note, coef = entree.split()  # On divise la chaîne par un espace
        notes.append(float(note))  # Convertir la note en float
        coefficients.append(int(coef))  # Convertir le coefficient en int
    return notes, coefficients

# Fonction pour calculer la moyenne pondérée
def calculer_moyenne(notes, coefficients):
    total_notes = sum(note * coef for note, coef in zip(notes, coefficients))  # Somme des notes pondérées
    total_coefficients = sum(coefficients)  # Somme des coefficients
    moyenne = total_notes / total_coefficients  # Moyenne pondérée
    return moyenne

# Fonction pour vérifier l'admission de l'étudiant
def verifier_admission(notes, moyenne):
    # Vérifier si la moyenne est supérieure à 10 et si aucune note n'est inférieure à 8
    if moyenne > 10 and all(note >= 8 for note in notes):
        return True
    else:
        return False

# Fonction principale
def main():
    # Obtenir les notes et coefficients
    notes, coefficients = obtenir_notes_et_coefficients()
    
    # Calculer la moyenne générale
    moyenne = calculer_moyenne(notes, coefficients)
    
    # Afficher la moyenne
    print(f"La moyenne générale de l'étudiant est : {moyenne:.2f}")
    
    # Vérifier si l'étudiant est admis
    if verifier_admission(notes, moyenne):
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")

# Appeler la fonction principale
if __name__ == "__main__":
    main()
