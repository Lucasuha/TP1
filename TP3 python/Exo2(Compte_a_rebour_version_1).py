import time

while True:
    n = int(input("Entrez un nombre entier positif : "))
    if n >= 0:
        break
    else:
        print("Veuillez entrer un nombre positif.")

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)