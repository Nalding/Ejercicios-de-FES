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
llista_b.clear()

print("Element eliminat:", element_eliminat)
print("Llista a:", llista_a)
print("Llista b:", llista_b)


#Exercici 3: Slicing i eliminació amb del.
#1. Crear una llista amb els nombres de l'1 al 10.
#2. Fer servir slicing i del per eliminar els elements des de l'índex 2 fins al 5 (sense incloure el 5).
#3. Imprimir la llista resultant.
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del nombres[2:5]

print(nombres)


#Exercici 4: Ordenar i comptar.
#1. Crear una llista amb els nombres següents: [5, 2, 8, 1, 9, 4, 2].
#2. Ordenar la llista de manera ascendent fent servir sort().
#3. Comptar quantes vegades apareix el nombre 2 a la llista fent servir count().
#4. Comprovar si el nombre 7 és a la llista fent servir in.
#5. Mostrar tots els casos.
nombres = [5, 2, 8, 1, 9, 4, 2]

nombres.sort()
quantitat_dos = nombres.count(2)
set_a_la_llista = 7 in nombres

print("Llista ordenada:", nombres)
print(f"El 2 apareix a la llista {quantitat_dos} vegades")
print("El número 7 es a la llista:", set_a_la_llista)


#Exercici 5: Còpia i referència.
#1. Crear una llista anomenada original amb els nombres [1, 2, 3].
#2. Crear una còpia anomenada copia_1 fent servir slicing.
#3. Crear una altra còpia anomenada copia_2 fent servir copy().
#4. Crear una referència a la llista original anomenada referencia.
#5. Modifica a 10 el primer element de la llista referencia.
#6. Imprimir les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.
original = [1, 2, 3]

copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10

print("Llista original:", original)
print("Copia_1:", copia_1)
print("Copia_2:", copia_2)
print("Llista de referencia:", referencia)


#Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules.
#1. Crear una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
#2. Ordena la llista sense distingir entre majúscules i minúscules.
#3. Mostrar la llista resultant.
fruites = ["Poma", "pera", "PLÀTAN", "taronja"]

fruites.sort(key = str.lower)

print("Fruites ordenades (sense distingir entre majúsucles i minúscules):", fruites)