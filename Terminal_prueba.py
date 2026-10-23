#Exercici 6: Números primers fins a n.
#1. Demanar a l'usuari que introdueixi un número enter positiu n.
#2. Imprimir tots els números primers menors o iguals que n fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n = int(input("Itrodueix un número enter positiu:"))
comptador = 2

while comptador <= n:
    num_primer = True
    divisor = 2
    while divisor < comptador and num_primer:
        if comptador % divisor == 0:
            num_primer = False
            break
        divisor += 1
    if num_primer == True:
        print(comptador)
    comptador += 1