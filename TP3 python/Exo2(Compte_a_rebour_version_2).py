import time

while True:
    n = int(input("Entrez un nombre entier positif : "))
    if n >= 0:
        break
    else:
            print("Veuillez entrer un nombre positif.")


while n >= 0:
    print(n)
    time.sleep(1)  
    n -= 1  