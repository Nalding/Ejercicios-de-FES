#Exercici 1: Determinar el més gran de dos nombres enters.
#1. Demanar a l'usuari que introdueixi dos nombres. 
#2. Mostrar un missatge que indiqui quin és més gran o si són iguals.
num1 = int(input("Introdueix un nombre enter:"))
num2 = int(input("Introdueix un altre nombre enter: "))

if num1 > num2:
    print(f"El nombre més gran és: {num1}")
elif num2 > num1:
    print(f"El nombre més gran és: {num2}")
else:
    print("Els dos nombres són iguals.")


#Exercici 2: Calculadora senzilla.
#1. Demanar a l'usuari dos nombres i una operació (+, -, *, /).
#2. Fer l'operació i mostrar el resultat (s'ha de gestionar la divisió per zero).
num1 = float(input("Introdueix un nombre: "))
num2 = float(input("Introdueix un altre nombre: "))
operacio = input("Introdueix una operació (+, -, *, /): ")

if operacio == "+":
    resultat = num1 + num2
    print("El resultat de sumar els dos nombres és: ", resultat)
elif operacio == "-":
    resultat = num1 - num2
    print("El resultat de restar els dos nombres és: ", resultat)
elif operacio == "*":
    resultat = num1 * num2
    print("El resultat de multiplicar els dos nombres és: ", resultat)
elif operacio == "/":
    if num2 != 0:
        resultat = num1 / num2
        print("El resultat de dividir els dos nombres és: ", resultat)
    else:
        print("Error: No es por dividir per zero.")
else:
    print("Operació no vàlida.")


#Exercici 3: Any de traspàs.
#1. Demanar a l'usuari que introdueixi un any i determinar si és de traspàs.
#Un any és de traspàs si és divisible per 4, excepte si és divisible per 100 però no per 400.
any = int(input("Introdueix un any per veure si és de traspàs: "))

if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
    print(f"L'any {any} és de traspàs.")
else:
    print(f"L'any {any} no és de traspàs.")


#Exercici 4: Classificar edats.
#1. Demanar a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edat = int(input("Introdueix una edat:"))

if 0 <= edat <= 2:
    print("Classificació: Nadó")
elif 3 <= edat <= 12:
    print("Classificació: Infant")
elif 13 <= edat <= 17:
    print("Classificació: Adolescent")
elif 18 <= edat <= 64:
    print("Classificació: Adult")
elif edat >= 65:
    print("Classificació: Persona gran")
else:
    print("Edat no vàlida.")
    