# Fonction pour vérifier si une chaîne est un palindrome
def est_palindrome(chaine):
    # Retirer les caractères non alphabétiques et convertir en minuscules
    chaine_epuree = ''.join(c for c in chaine if c.isalpha()).lower()
    
    # Vérifier si la chaîne épurée est égale à elle-même inversée
    return chaine_epuree == chaine_epuree[::-1]

# Fonction principale
def main():
    # Lire une chaîne de caractères du clavier
    chaine = input("Entrez un mot ou une phrase : ")
    
    # Tester si c'est un palindrome
    if est_palindrome(chaine):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

# Appeler la fonction principale
if __name__ == "__main__":
    main()
