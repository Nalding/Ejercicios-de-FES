#Exercici 1:
#Crear una tupla amb els noms de 5 ciutats i mostrar la segona i la penúltima ciutat.
ciutats = ("Madrid", "Paris", "Barcelona", "Londres", "Venècia")
print(ciutats[1])
print(ciutats[3])


#Exercici 2:
#Donada una tupla amb números enters, comptar quantes vegades apareix el número 3 a la tupla.
numeros = (2, 3, 4, 3, 1, 3, 3, 1, 1)

print(f"El número 3 apareix {numeros.count(3)} vegades a la tupla 'numeros")


#Exercici 3:
#Crear una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla_numeros):
    return tuple(sorted(tupla_numeros))

tupla_desordenada = [3, 14, 87, 22, -1]

print("La tupla original es", tupla_desordenada)
print("La tupla ordenada es:", ordenar_tupla(tupla_desordenada))
