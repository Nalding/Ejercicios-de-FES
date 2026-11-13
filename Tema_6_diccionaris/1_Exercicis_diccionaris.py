#Exercici 1: Crear un diccionari.
#1. Crear un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
#(aquesta última, una llista amb tres assignatures). 
#2. Imprimeix-lo.
estudiant = {
    "nom" : "Arnau",
    "edat" : 19,
    "assignatures" : ["FES", "Senyals i Sistemes Discrets", "Xarxes"]
}

print(estudiant)


#Exercici 2: Accedir i modificar.
#Imprimir la segona assignatura de l'estudiant i canviar l'edat a un valor nou.
estudiant["edat"] = 21
print(estudiant["assignatures"][1])
print(estudiant["edat"])


#Exercici 3: Afegir i eliminar.
#Afegir la clau "grau" a l'estudiant i eliminar després la clau "edat" amb del.
estudiant["grau"] = "Enginyeria de Sistemes de Telecomunicacions"
del estudiant["edat"]

print(estudiant)

#Exercici 4: Comprovar claus
#Comprovar amb in si existeixen les claus "nom" i "email" i imprimir el resultat.
print("nom" in estudiant)
print("email" in estudiant)


# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".
#Exercici 5: Recórrer un diccionari.
#Recorrer el diccionari amb un bucle for i items() i imprimir cada parella com "clau: valor".
for clau, valor in estudiant.items():
    print(f"{clau} : {valor}")


#Exercici 6: Comptar paraules.
#Donada la llista de paraules:
# - paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
#Crear un diccionari que indiqui quantes vegades apareix cada paraula.
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
comptar_paraules = {}

for paraula in paraules:
    if paraula in comptar_paraules:
        comptar_paraules[paraula] += 1
    else:
        comptar_paraules[paraula] = 1

print(comptar_paraules)
