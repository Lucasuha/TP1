x = int(input('Entrez x:'))
y = int(input('Entrez y:'))
z = int(0)       #variable temporaire

print('Avant permutation :')
print('X:',x)
print('Y:',y)

z = x     # ou on peut faire x,y = y,x 
x = y
y = z
print('Après permutation :')
print('X :',x)
print('y :',y)

