#Exercici 1: Compte enrere.
#Imprimir els números del 10 a l'1 fent servir un bucle while.
comptador = 10

print("Compte enrere:")
while comptador >= 1:
    print(comptador)
    comptador -= 1


#Exercici 2: Suma de números parells (while).
#Calcular la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
comptador = 1
suma = 0

while comptador <= 20:
    if comptador % 2 == 0:
        suma += comptador
    comptador += 1


#Exercici 3: Factorial d'un número.
#1. Demana a l'usuari que introdueixi un número enter positiu.
#2. Calcula el seu factorial fent servir un bucle while.
#El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. 
# Per exemple, el factorial de 5 és 5! = 5 x 4 x 3 x 2 x 1 = 120.
#3. Mostrar el resultat
num = int(input("Introdueix un número enter positiu: "))
c = 1
factorial = 1

while c <= num:
    factorial *= c
    c += 1

print(f"El factorial de {num} és: {factorial}" )


#Exercici 4: Validació de contrasenya.
#1. Demanar a l'usuari que introdueixi una contrasenya.
# - la contrasenya ha de tenir almenys 8 caràcters.
#Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
#2. Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = ""

while len(contrasenya) < 8:
    contrasenya = input("Introdueix una contrasenya (almenys 8 caràcters): ")
    if len(contrasenya) < 8:
        print("La contrasenya ha de tenir almenys 8 caràcters!!")

print("Contrasenya vàlida")


#Exercici 5: Taula de multiplicar.
#1. Demanar a l'usuari que introdueixi un número.
#2. Imprimir la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num = int(input("Introduiex un número: "))
comptador = 1

print(f"TAULA DE MULTIPLICAR DEL {num}")
while comptador <= 10:
    resultat_multiplicacio = num * comptador
    print(f"{num} x {comptador} = {resultat_multiplicacio}")
    comptador += 1


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
    

#Exercici 7: Suma fins al zero.
#1. Demanar a l'usuari que introdueixi números enters.
#2. Anar sumant els números introduïts fins que l'usuari introdueixi el 0.
#3. Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
num = int(input("Introduiex un número enter (0 per acabar): "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Introduiex un altre enter (0 per acabar): "))

print("La suma de tots el números introduïts és:", suma)


#Exercici 8: Comptar les xifres d'un número.
#1. Demanar a l'usuari que introdueixi un número enter positiu.
#2. Comptabilitza quantes xifres té fent servir un bucle while.
#3. Finalment, imprimeix el nombre de xifres.
num = int(input("Introdueix un nombre enter positiu: "))
comptador = 0

if num == 0:
    comptador = 1
else:
    while num > 0:
        num //= 10            #permet eliminar l'última xifra del número.
        comptador += 1

print(f"El número introduït té {comptador} xifres")


#Exercici 9: Seqüència de Fibonacci.
#1. Demanar a l'usuari quants termes de la seqüència de Fibonacci vol veure.
#2. Imprimir aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
termes = int(input("Quants termes de la seqüència de Fibonacci vols veure?: "))
comptador = 0
anterior = 0
actual = 1

while comptador < termes:
    print(anterior)
    seguent = anterior + actual
    anterior = actual 
    actual = seguent
    comptador += 1


#Exercici 10: Joc d'endevinar el número.
#El número secret és el 7.
#1. Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
#fins que l'encerti.
#2. Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
num_secret = 7
num_usuari = int(input("Intenta endevinar el número secret (introdueix un enter): "))
comptador = 0

while num_usuari != num_secret:
    if num_secret > num_usuari:
        num_usuari = int(input("INCORRECTE, EL NÚMERO SECRET ÉS MÉS GRAN: "))
    else:
        num_usuari = int(input("INCORRECTE, EL NÚMERO SECRET ÉS MÉS PETIT: "))

print("HAS ENCERTAT EL NÚMERO!!!!!!!")
