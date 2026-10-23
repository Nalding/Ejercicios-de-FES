#Exercici 1: El missatge secret.
#Donada la llista següent:
# - missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
#1. Fent servir slicing i concatenació, crea una llista nova que contingui només el missatge "secret".
#2. Mostrar la nova llista.
missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
missatge_modificat = missatge[5:]

print(missatge_modificat)


#Exercici 2: Intercanvi de posicions.
#Donada la llista següent:
# - nombres = [10, 20, 30, 40, 50]
#1. Intercanvia la primera i l'última posició fent servir només l'assignació per índex.
#2. Mostra la llista cambiada.
nombres = [10, 20, 30, 40, 50]
nombres[0], nombres[4] = nombres[4], nombres[0]

print(nombres)


#Exercici 3: L'entrepà de llistes.
# Donades les llistes següents:
# - pa_de_dalt = ["pa de dalt"]
# - ingredients = ["pernil", "formatge", "tomàquet"]
# - pa_de_sota = ["pa de sota"]
#1. Crear una llista anomenada entrepa que contingui, en aquest ordre:
# - el pa de dalt, els ingredients i el pa de sota.
#2. Mostrar la llista entrepa.
pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]
entrepa = pa_de_dalt + ingredients + pa_de_sota

print(entrepa)


#Exercici 4: Duplicar una llista.
#Donada una llista:
# - llista = [1, 2, 3]
#1. Crear una llista nova que contingui duplicats els elements de la llista original.
#Exemple: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
#2. Mostar la nova llista.
llista = [1, 2, 3]
llista_duplicada = llista + llista

print(llista_duplicada)


#Exercici 5: Extreure l'element central.
#Donada una llista amb un nombre senar d'elements: 
# - llista = [10, 20, 30, 40, 50] 
#1. Extreure l'element central fent servir slicing per mostrar-lo.
#Exemple: llista = [10, 20, 30, 40, 50] -> L'element central és 30.
llista = [10, 20, 30, 40, 50, 60, 70]
element_central = len(llista) // 2

print("L'element central és:", llista[element_central])


#Exercici 6: Inversió parcial.
#Donada una llista:
# - llista1 = [1, 2, 3, 4, 5, 6]
#1. Inverteix-ne només la primera meitat (fent servir slicing i concatenació).
#2. Mostrar la llista modificada.
# Exemple: llista = [1, 2, 3, 4, 5, 6] -> Resultat: [3, 2, 1, 4, 5, 6]
llista1 = [1, 2, 3, 4, 5, 6]
meitat_llista = len(llista1) // 2
llista2 = llista1[:meitat_llista][::-1] + llista1[meitat_llista:]

print("La llista modificada és:", llista2)