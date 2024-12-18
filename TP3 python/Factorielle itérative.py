def factorielle_for(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print(f"Étape {i}: {fact}")
    return fact

def factorielle_while(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        print(f"Étape {i}: {fact}")
        i += 1
    return fact

def main():
    n = int(input("Entrez un entier positif n pour calculer sa factorielle: "))
    
    if n < 0:
        print("La factorielle est définie uniquement pour les entiers positifs ou nuls.")
        return
    
    print("Choisissez le type de boucle à utiliser:")
    print("1 - Utiliser une boucle for")
    print("2 - Utiliser une boucle while")
    
    choix = int(input("Votre choix (1 ou 2): "))
    
    if choix == 1:
        print("Calcul avec une boucle for:")
        factorielle_for(n)
    elif choix == 2:
        print("Calcul avec une boucle while:")
        factorielle_while(n)
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
main()
