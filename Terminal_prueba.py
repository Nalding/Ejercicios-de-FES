#Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules.
#1. Crear una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
#2. Ordena la llista sense distingir entre majúscules i minúscules.
#3. Mostrar la llista resultant.
fruites = ["Poma", "pera", "PLÀTAN", "taronja"]

fruites.sort(key = str.lower)

print("Fruites ordenades (sense distingir entre majúsucles i minúscules):", fruites)
