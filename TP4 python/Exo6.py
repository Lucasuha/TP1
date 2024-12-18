def tri_par_selection(tab):
    n = len(tab)
    
    # Parcours de chaque élément du tableau
    for i in range(n):
        # On suppose que l'élément à la position i est le plus petit
        min_index = i
        for j in range(i+1, n):
            # On cherche le plus petit élément dans le reste de la liste
            if tab[j] < tab[min_index]:
                min_index = j
        
        # Si min_index a changé, on permute les éléments
        if min_index != i:
            tab[i], tab[min_index] = tab[min_index], tab[i]
        
        # Affichage de l'état de la liste à chaque phase
        print(tab)

# Liste donnée en exemple
tab = [5, 2, 4, 8, 1, 3]

# Appliquer le tri par sélection
tri_par_selection(tab)
