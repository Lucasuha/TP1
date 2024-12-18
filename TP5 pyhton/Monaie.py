somme = int(input("Entrez une somme en euros : "))

billets_100 = somme // 100
somme = somme % 100

billets_50 = somme // 50
somme = somme % 50

billets_10 = somme // 10
somme = somme % 10

pieces_2 = somme // 2
somme = somme % 2

pieces_1 = somme

# Affichage du résultat
print(f"{somme} euros, c’est donc {billets_100} billets de 100,{billets_50} de 50, {billets_10} de 10, {pieces_2} pièces de 2 et {pieces_1} pièce(s) de 1.")

