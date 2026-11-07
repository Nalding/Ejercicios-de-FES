#Exercici 1: Funció de salutació.
#1. Crear una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
#2. Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}")

saludar_a("Arnau", "Bon dia")
saludar_a("Arnau")


#Exercici 2: Parell o senar.
#Crear una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    return numero % 2 == 0

print(es_parell(15))
print(es_parell(30))


#Exercici 3: Mitjana d'una llista.
#1. Crear una funció mitjana(numeros) que rebi una llista de números i en retorni
#la mitjana fent servir un bucle for.
def mitjana(numeros):
    suma_numeros = 0

    for num in numeros:
        suma_numeros += num

    return suma_numeros / len(numeros)

print(mitjana([1, 2, 3, 2, 1]))


#Exercici 4: Suma amb *args.
#1. Crear una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
#2. Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    suma = 0

    for num in args:
        suma += num

    return suma

print(sumar_tot(2, 8))
print(sumar_tot(5, 4, 3, 2, 1))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#Exercici 5: Taula de multiplicar.
#Crear una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
#del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for num in range(numero, limit + 1):
        print(f"{numero} x {num} = {numero * num}")

num_usuari = int(input("Intrdueix un número per veure la seva taula de multiplicar: "))

taula_multiplicar(num_usuari)


#Exercici 6: Informació amb **kwargs.
#1. Crear una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
#2. Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom = "Arnau", edat = 19, grau = "Enginyeria de Sistemes de Telecomunicacions")


#Exercici 7: Reconvertir exercicis anteriors-
#Tornar a l'exercici del factorial (while) i del màxim d'una llista (for)
#i convertir-los en funcions que retornin el resultat.
def factorial(num):
    comptador = 1
    resultat = 1

    while comptador <= num:
        resultat *= comptador
        comptador += 1

    return resultat

def maxim(numeros):
    max = numeros[0]

    for num in numeros:
        if num > max:
            max = num

    return max

print(f"El factorial de 3 és: {factorial(3)}" )
print(f"El màxim és {maxim([15, 5, 25, 10, 20])}")


#Exercici 8: Comptar vocals.
#Crear una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
#(a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    vocals = "aeiouàèéíòóúïü"
    comptador = 0

    for lletra in text.lower():
        if lletra in vocals:
            comptador += 1

    return comptador

print(f"Les vocals que hi ha a 'arnau' són : {comptar_vocals('arnau')}")
print(f"Les vocals a 'MARVEL' són: {comptar_vocals('MARVEL')}")


#Exercici 9: Retorn múltiple (mínim i màxim).
#Crear una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
#mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    minim = numeros[0]
    maxim = numeros[0]

    for num in numeros[1:]:  
        if num < minim:
            minim = num
        if num > maxim:
            maxim = num

    return minim, maxim

llista_numeros = [2, -6, 14, 8, 3]
valor_minim, valor_maxim = minim_i_maxim(llista_numeros)

print(f"El mínim de la llista {llista_numeros} és {valor_minim} i el màxim {valor_maxim}")


#Exercici 10: Palíndrom.
#Crear una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
#que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
    text_sense_majuscules = text.lower()

    return text_sense_majuscules == text_sense_majuscules[::-1]

print("La paraula 'Nen' és un palíndrom:", es_palindrom("Nen"))
print("La paraula 'Saltar' és un palíndrom:", es_palindrom("Saltar"))