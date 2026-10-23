#Exercici 2: Combinar i buidar llistes.
#1. Crear dues llistes:
# - llista_a = [1, 2, 3]
# - llista_b = [4, 5, 6, 1, 2]
#2. Ampliar la llista_a amb llista_b fent servir extend().
#3. Eliminar la primera aparició del nombre 1 de llista_a fent servir remove().
#4. Elimina l'element de l'índex 3 de llista_a fent servir pop(). 
#5. Imprimeix l'element eliminat.
#6. Buida completament llista_b fent servir clear().
#7. Imprimeix les dues llistes resultants.
llista_a = [1, 2, 3]
llista_b = [4, 5, 6, 1, 2]

llista_a.extend(llista_b)
llista_a.remove(1)
element_index_3 = llista_a.pop(3)
print(element_index_3)
llista_b.clear()
print(llista_a)
print(llista_b)