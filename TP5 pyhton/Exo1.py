# Fonction pour formater le prénom et le nom selon les spécifications
def formater_personne(prenom, nom):
    # Mise en majuscule du nom et capitalisation du prénom
    prenom_formatte = prenom.capitalize()
    nom_formatte = nom.upper()
    return prenom_formatte, nom_formatte

# Fonction principale pour entrer les noms et prénoms et trier les résultats
def main():
    # Demander à l'utilisateur d'entrer les informations pour deux personnes
    prenom1 = input("Entrez le prénom de la première personne : ")
    nom1 = input("Entrez le nom de la première personne : ")
    
    prenom2 = input("Entrez le prénom de la deuxième personne : ")
    nom2 = input("Entrez le nom de la deuxième personne : ")
    
    # Formater les prénoms et noms
    prenom1, nom1 = formater_personne(prenom1, nom1)
    prenom2, nom2 = formater_personne(prenom2, nom2)
    
    # Créer des tuples (prenom, nom) pour les trier
    personne1 = (prenom1, nom1)
    personne2 = (prenom2, nom2)
    
    # Trier les personnes par nom, puis par prénom en cas de noms identiques
    personnes_triees = sorted([personne1, personne2], key=lambda x: (x[1], x[0]))
    
    # Afficher les résultats
    for prenom, nom in personnes_triees:
        print(f"{prenom} {nom}")

# Appeler la fonction principale
if __name__ == "__main__":
    main()
