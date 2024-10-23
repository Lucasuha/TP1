BASE = 4
fromage = float(800)
eau = 2
ail = 2 
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) convié a la fonude:"))
fromage = fromage * nbConvives / BASE 
eau = eau * nbConvives / BASE 
ail = ail * nbConvives / BASE 
pain = pain * nbConvives / BASE 

print("Pour faire une fondue fribourgeoise pour" ,nbConvives, "personnes, il vous faut :")
print("-" ,fromage, "gr de fromage")
print("-" ,eau, "dl d'eau")
print("-" ,ail, "gousse(s)")
print("-" ,pain, "gr de pain")