#Exercici 1: Imprimir missatges.
#Imprimir el meu nom i la meva ciutat en línies separades.
print("Arnau Rastrollo")
print("Barcelona")


#Exercici 2: Mostrar els tipus de dades de les variables següents:
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

print(f"Tipus de dades de a: {type(a)}")
print(f"Tipus de dades de b: {type(b)}")
print(f"Tipus de dades de c: {type(c)}")
print(f"Tipus de dades de d: {type(d)}")
print(f"Tipus de dades de e: {type(e)}") 


#Exercici 3: Conversió de types. 
#1. Convertir la cadena "12345" a un enter i després a un float i mostrar-ho.
#2. Convertir el float 3.99 a un enter i veure què passa.
cadena = "12345"
canvi_a_enter = int(cadena)
canvi_a_float = float(canvi_a_enter)

print(f"El nombre transformat a enter és: {canvi_a_enter}")
print(f"El nombre transformat a decimal és: {canvi_a_float}")

decimal_og = 3.99
decimal_convertit = int(decimal_og)

print(f"El nombre decimal original és: {decimal_og}")
print(f"El nombre decimal convertit a enter és: {decimal_convertit}. Han desaparegut els decimals.")


#Exercici 4: Variables. 
#1. Crear variables per el meu nom, edat i alçada.
#2. Utilitzar f-strings per imprimir una presentació.
nom = "Arnau"
edat = 19
alçada = 1.75

print(f"Hola, em dic {nom}, tinc {edat} anys i la meva alçada és de {alçada} metres.")


#Exercici 5: Nombres.
#1. Utilitzar el valor aproximat de PI (3.1416) sense desar-lo en una variable.
#2. Arrodonir el nombre amb round().
#3. Fer la divisió entera entre el nombre resultant i el nombre 2.
#4. El resultat hauria de ser 1.
resultat = int(round(3.1416) / 2)

print(f"El nombre pi arrodonnit és: {round(3.1416)}")
print(f"El resultat de dividir el nombre PI entre 2 és: {resultat}.")


#Exercici 6: Conversor de temperatura.
#1. Demanar a l'usuari una temperatura en graus Celsius.
#2. Convertir-la a Fahrenheit amb la fórmula: F = (C * 9/5) + 32.
#3. Mostrar tots dos valors amb un missatge clar.
temperatura_en_celsius = float(input("Introdueix la temperatura en graus Celsius: "))
temperatura_en_fahrenheit = (temperatura_en_celsius * 9/5) + 32

print(f"La temperatura de {temperatura_en_celsius}°C és equivalent a {temperatura_en_fahrenheit:.2f}°F.")


#Exercici 7: Calculadora de propines
#1. Demanar l'import total d'un compte i el percentatge de propina.
#2. Calcular l'import de la propina i el total que cal pagar.
#3. Mostrar els resultats amb 2 decimals.
import_total = float(input("Import total del compte (en euros): "))
percentatge_propina = float(input("Percentatge de propina: "))

propina = import_total * (percentatge_propina / 100)
total_a_pagar = import_total + propina

print(f"Import de la propina: {propina:.2f} €")
print(f"Total a pagar: {total_a_pagar:.2f} €")


#Exercici 8: Comprovador senzill de contrasenya.
#1. Demanar una contrasenya a l'usuari.
#2. Comprovar si té almenys 8 caràcters.
#3. Mostrar 'Contrasenya vàlida' o 'Contrasenya no vàlida'.
contrasenya = input("Introdueix una constrasenya: ")

if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")

