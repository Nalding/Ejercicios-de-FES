#Exercici 1: Afegir i modificar elements.
#1. Crear una llista amb els nombres de l'1 al 5.
#2. Afegir el nombre 6 al final fent servir append().
#3. Inserir el nombre 10 a la posició 2 fent servir insert().
#4. Modifica el primer element de la llista perquè sigui 0.
#5. Mostrar la llista modificada.
nombres = [1, 2, 3, 4, 5]
nombres.append(6)
nombres.insert(2, 10)
nombres[0] = 0

print(nombres)


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
element_eliminat = llista_a.pop(3)
print("Element eliminat:", element_eliminat)
llista_b.clear()
print("Llista a:", llista_a)
print("Llista b:", llista_b)


# Exercici 3: Slicing i eliminació amb del
# Crea una llista amb els nombres de l'1 al 10.
# Fes servir slicing i del per eliminar els elements des de l'índex 2 fins al 5
# (sense incloure el 5).
# Imprimeix la llista resultant.

# Exercici 4: Ordenar i comptar
# Crea una llista amb els nombres següents: [5, 2, 8, 1, 9, 4, 2].
# Ordena la llista de manera ascendent fent servir sort().
# Compta quantes vegades apareix el nombre 2 a la llista fent servir count().
# Comprova si el nombre 7 és a la llista fent servir in.

# Exercici 5: Còpia i referència
# Crea una llista anomenada original amb els nombres [1, 2, 3].
# Crea'n una còpia anomenada copia_1 fent servir slicing.
# Crea'n una altra còpia anomenada copia_2 fent servir copy().
# Crea una referència a la llista original anomenada referencia.
# Modifica a 10 el primer element de la llista referencia.
# Imprimeix les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.

# Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules
# Crea una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
# Ordena la llista sense distingir entre majúscules i minúscules.