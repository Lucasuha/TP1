import unicodedata
import string


# Fonction pour nettoyer le texte : supprimer espaces, ponctuation, et convertir en minuscules
def nettoyer_texte(texte):
    # Convertir en minuscules
    texte = texte.lower()

    # Supprimer les caractères non-alphanumériques (ponctuation, espaces, etc.)
    texte_nettoye = ''.join(c for c in texte if c.isalnum())

    return texte_nettoye


# Fonction pour supprimer les accents
def supprimer_accents(texte):
    # Utilisation de la normalisation Unicode pour supprimer les accents
    texte_sans_accents = unicodedata.normalize('NFD', texte)
    texte_sans_accents = ''.join(c for c in texte_sans_accents if unicodedata.category(c) != 'Mn')

    return texte_sans_accents


# Fonction pour vérifier si un texte est un palindrome
def est_palindrome(texte):
    # Nettoyer le texte en supprimant les accents et les caractères spéciaux
    texte_nettoye = nettoyer_texte(texte)
    texte_sans_accents = supprimer_accents(texte_nettoye)

    # Vérifier si le texte est égal à son inverse
    return texte_sans_accents == texte_sans_accents[::-1]


# Programme principal interactif
def verifier_palindrome():
    # Demander à l'utilisateur de saisir un texte
    texte = input("Entrez un mot ou une phrase pour vérifier si c'est un palindrome : ")

    # Vérifier si le texte est un palindrome
    if est_palindrome(texte):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")


# Lancer le programme
verifier_palindrome()

