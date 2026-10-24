#Exercici 10: Joc d'endevinar el número.
#El número secret és el 7.
#1. Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
#fins que l'encerti.
#2. Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
num_secret = 3
num_usuari = int(input("Intenta endevinar el número secret (introdueix un enter): "))
comptador = 0

while num_usuari != num_secret:
    if num_secret > num_usuari:
        num_usuari = int(input("INCORRECTE, EL NÚMERO SECRET ÉS MÉS GRAN: "))
    else:
        num_usuari = int(input("INCORRECTE, EL NÚMERO SECRET ÉS MÉS PETIT: "))

print("HAS ENCERTAT EL NÚMERO!!!!!!!")
        