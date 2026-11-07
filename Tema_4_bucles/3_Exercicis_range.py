#Exercici 1: Imprimir números de l'1 al 10.
#Imprimir els números de l'1 al 10 (inclosos) fent servir un bucle for i range().
for num in range(1, 11):
    print(num)


#Exercici 2: Imprimir números senars de l'1 al 20.
#Imprimir tots els números senars entre 1 i 20 (inclosos) fent servir un bucle for i range().
for num in range(1, 21, 2):
    print(num)


#Exercici 3: Imprimir múltiples de 5.
#Imprimir els múltiples de 5 des del 5 fins al 50 (inclosos) fent servir un bucle for i range().
for num in range(5, 51, 5):
    print(num)


#Exercici 4: Imprimir números en ordre invers.
#Imprimir els números del 10 a l'1 (inclosos) en ordre invers fent servir un bucle for i range().
for num in range(10, 0, -1):
    print(num)


#Exercici 5: Suma de números en un rang.
#Calcular la suma dels números de l'1 al 100 (inclosos) fent servir un bucle for i range().
suma = 0

for num in range(1, 101):
    suma += num

print("La suma dels números de l'1 al 100 és:", suma)


#Exercici 6: Taula de multiplicar.
#1. Demanar a l'usuari que introdueixi un número.
#2. Imprimir la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle for i range().
num_usuari = int(input("Introdueix un número per veure la seva taula de multiplicar: "))
operacio = 0

for num in range(1, 11):
    print(f"{num_usuari} x {num} = {num_usuari * num}")
