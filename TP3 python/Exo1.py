N = int(input("ENtrez un nombre entier:"))
S = 0

for i in range (N+1):
    if  N == 100:
        break
    else:
        S += i

print("Le nombre total est", S )
