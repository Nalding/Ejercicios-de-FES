#Exercici 1: Imprimir números parells.
#Imprimir tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
for num in range(2, 21, 2):
    print(num)


#Exercici 2: Calcular la mitjana d'una llista.
#Donada la llista de números següent:
# - numeros = [10, 20, 30, 40, 50]
#Calcular la mitjana dels números fent servir un bucle for.
numeros = [10, 20, 30, 40, 50]
suma = 0

for num in numeros:
    suma += num

mitjana = suma / len(numeros)
print("La mitjana dels numeros de la llista és: ", mitjana)


#Exercici 3: Buscar el màxim d'una llista.
#Donada la llista de números següent:
# - numeros = [15, 5, 25, 10, 20]
#Trobar el número màxim de la llista fent servir un bucle for.
numeros = [15, 5, 25, 10, 20]

maxim = numeros[0]
for num in numeros:
    if num > maxim:
        maxim = num

print("El número més gran de la llista és:", maxim)


#Exercici 4: Filtrar cadenes per longitud.
#Donada la llista de paraules següent:
# - paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
#Crear una llista nova que contingui només les paraules amb més de 5 lletres,
#fent servir un bucle for i list comprehension.
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
paraules_5_lletres = [paraula for paraula in paraules if len(paraula) > 5]

print("Les paraules de més de 5 lletres són:", paraules_5_lletres)


#Exercici 5: Comptar paraules que comencen per una lletra.
#Donada la llista de paraules següent:
# - paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
#1. Demanar a l'usuari que introdueixi una lletra.
#2. Comptar quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input("Introdueix una lletra: ").lower()
comptador = 0

for paraula in paraules:
    if paraula.lower().startswith(lletra):
        comptador += 1

print(f"Hi han {comptador} paraules dintre de la llista que comencen amb la lletra {lletra}")


#Exercici 6: Mesures de tensió d'un sensor.
#Durant una prova s'han registrat les tensions següents (en volts):
# - tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
#Fent servir un bucle for, calcular la tensió mitjana i imprimir-la
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
suma = 0

for tensio in tensions:
    suma += tensio

mitjana = suma / len(tensions)

print("La tensió mitjana és:", mitjana)


#Exercici 7: Corrent en resistències.
#En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# - resistencies = [100, 220, 470, 1000]
#Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcular i imprimir
#el corrent que circula per cada resistència, en ampers.
resistencies = [100, 220, 470, 1000]
intensitat = 0

for idx, r in enumerate(resistencies):
    intensitat = 12 / r
    print(f"Per la {idx} resistencia la intensitat és: {intensitat:.2f}")


# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.