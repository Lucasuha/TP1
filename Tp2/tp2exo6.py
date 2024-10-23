from random import randint
number = randint(0, 100)
print("Le nombre est",number)

if number < 50 :
    print("Pile !")
else :
    print("Face !")