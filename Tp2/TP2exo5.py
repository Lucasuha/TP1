X = int(input("ENtrez un nombre entier:"))

if X%2 == 0 and X>0:
    print("Le nombre est positif et pair")
elif  X%2 == 1 and X>0:
    print("Le nombre est positif et impair")
elif  X%2 == 0 and X<0:
    print("Le nombre est négatif et pair")
elif  X%2 == 1 and X<0:
    print("Le nombre est négatif et impair")
elif X == 0 :
    print("Le nombre est zéro (et il est pair)")