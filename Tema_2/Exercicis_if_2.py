#Exercici 1: Qualitat del senyal Wi-Fi.
#1. Demanar el nivell de senyal rebut (RSSI) en dBm i classificar la cobertura:
# - -50 dBm o superior: excel·lent.
# - Entre -67 dBm i menys de -50 dBm: bona.
# - Entre -75 dBm i menys de -67 dBm: feble.
# - Inferior a -75 dBm: molt feble.
senyal_wifi = int(input("Nivell de senyal WI-Fi (en dBm): "))

if senyal_wifi >= -50:
    print("Qualitat del senyal: excel·lent")
elif senyal_wifi >= -67:
    print("Qualitat del senyal: bona")
elif senyal_wifi >= -75:
    print("Qualitat del senyal: feble")
else:
    print("Qualitat del senyal: molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica.
#1. Demanar la potència òptica rebuda en dBm.
# Es considera acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
#2. Indicar si el nivell és massa baix, acceptable o massa alt.
potencia_optica = int(input("Potència òptica rebuda (en dBm): "))

if potencia_optica <= -27:
    print("Nivell de recepció: Massa baix!!")
elif potencia_optica <= -8:
    print("Nivell de recepció: Acceptable")
else:
    print("Nivell de recepció: Massa alt!!")


# Exercici 3: Consum mensual de dades mòbils.
#1. Demanar el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
#2. Indicar si el consum és dins del límit o si l'ha superat. 
#3. En cas d'haver superat el límit, calcula quants GB addicionals s'han consumit.
consum_mensual = float(input("Consum mensual de dades mòbils (en GB): "))

if consum_mensual > 20:
    print("Consum fora del límit del pla!!")
    Gb_addicionals = consum_mensual - 20
    print(f"Has consumit {Gb_addicionals:.2f} GB addicionals.")
else:
    print("Consum dins del límit del pla!!")


# Exercici 4: Diagnòstic d'una connexió de fibra.
#1. Demanar si l'indicador LOS del terminal òptic i l'indicador d'Internet del router estàn encèsos.
#2. Segons aquestes dues dades, indica si cal revisar el cable de fibra, comprovar el servei del proveïdor o 
# si la connexió sembla funcionar correctament.
Los_ences = input("L'indicador LOS del terminal òptic está encés (si/no): ")
Internet_ences = input("L'indicador d'Internet del router está encés (si/no): ")

if Los_ences == "si" and Internet_ences == "si":
    print("La connexió sembla funcionar correctament.")
elif Los_ences == "si" and Internet_ences == "no":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("Cal revisar el cable de fibra.")


#Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI).
#1. Demanar el percentatge de bateria disponible al SAI que alimenta un armari de comunicacions. 
#2. Indicar:
# - si el nivell és crític (menys del 20 %)
# - si el nivell és baix (del 20 % al 49 %)
# - si el nivell és suficient (50 % o més). 
# - es rebutjen els valors fora del rang del 0 % al 100 %.
percentatge_bateria = int(input("Percentatge de bateria disponible al SAI (0-100 %): "))

if percentatge_bateria < 0 or percentatge_bateria > 100:
    print("Valor fora del rang vàlid (0-100 %).")
elif percentatge_bateria < 20:
    print("Nivell de bateria: Crític!!!!!!!!!")
elif percentatge_bateria < 50:
    print("Nivell de bateria: Baix!!!")
else:
    print("Nivell de bateria: Suficient")


#Exercici 6: Qualitat d'una connexió de xarxa.
#1. Demanar la latència en mil·lisegons i el percentatge de paquets perduts.
#2. Rebutjar una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
#3. Classificar la connexió com:
# - Excel·lent si la latència és de 30 ms o menys i la pèrdua és de l'1 % o menys.
# - Bona si és de 80 ms o menys i la pèrdua és del 3 % o menys.
# - Acceptable si és de 150 ms o menys i la pèrdua és del 5 % o menys.
# - Deficient en qualsevol altre cas.
latencia = int(input("Latència de la connexió (en ms): "))
paquets_perduts = float(input("Percentatge de paquets perduts (%): "))
latencia_valida = True
paquets_perduts_valids = True

if latencia < 0:
    print("ERROR: La latència és negativa")
    latencia_valida = False

if paquets_perduts < 0 or paquets_perduts > 100:
    print("ERROR: La pèrdua està fora del rang")
    paquets_perduts_valids = False

if latencia_valida and paquets_perduts_valids:
    if latencia <= 30 and paquets_perduts <= 1:
        print("Connexió EXCEL·LENT")
    elif latencia <= 80 and paquets_perduts <= 3:
        print("Connexió BONA")
    elif latencia <= 150 and paquets_perduts <= 5:
        print("Connexió ACCEPTABLE")
    else: 
        print("Connexió DEFICIENT")


#Exercici 7: Cost mensual d'un pla de dades.
#1. Demanar el tipus de pla (bàsic o plus) i el consum mensual en GB.
# - El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# - El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
#2. Rebutjar un consum negatiu o un tipus de pla desconegut. 
#3. Calcular i mostrar el cost total. 
# - S'ha de tenir en compte que no es cobra l'excés si no se supera el límit.
tipus_pla = int(input("Tipus de pla (1 = bàsic, 2 = plus): "))
consum_mensual = int(input("Consum mensual (en GB): "))
pla_valid = True
consum_valid = True

if tipus_pla != 1 and tipus_pla != 2:
    print("Error: El tipus de pla no és vàlid.")
    pla_valid = False

if consum_mensual < 0:
    print("Error: El consum mensual no pot ser negatiu.")
    consum_valid = False

if pla_valid and consum_valid:
    gb_addicionals = 0

    if tipus_pla == 1:
        if consum_mensual > 10:
            gb_addicionals = consum_mensual - 10
        cost_total = 10 + (gb_addicionals * 1.5)
        print(f"El cost total del pla és de {cost_total} €")
    elif tipus_pla == 2:
        if consum_mensual > 30:
            gb_addicionals = consum_mensual - 30
        cost_total = 20 + (gb_addicionals * 0.75)
        print(f"El cost total del pla és de {cost_total} €")


#Exercici 8: Accés a un compte de client.
#1. Demanar si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. 
# - Demanar el codi només si el compte és actiu i la contrasenya és correcta. 
#2. Indicar si l'accés es denega perquè:
# - el compte està desactivat
# - la contrasenya és incorrecta
# - o falla el codi
#3. Si totes les comprovacions necessàries són correctes, es permet l'accés.
compte = int(input("Estat del compte (1 = Actiu, 0 = No actiu): "))
contrasenya = int(input("Estat de la contrasenya (1 = Correcta, 0 = Incorrecta): "))

if compte == 1 and contrasenya == 1:
    codi = int(input("Estat del codi de doble verificació (1 = Correcte, 0 = Incorrecte): "))
    if codi == 1:
        print("ACCÉS PERMÈS")
    else:
        print("ACCÉS DENEGAT: El codi de doble verificació es incorrecte")
elif compte == 1 and contrasenya == 0:
    print("ACCÉS DENEGAT: La contraseña és incorrecta")
elif compte == 0 and contrasenya == 1:
    print("ACCÉS DENEGAT: El compte està desactivat")
else:
    print("NO ES POT ACCEDIR AL SISTEMA") 


#Exercici 9: Diagnòstic d'un router.
#1. Demanar si el router està encès, si l'indicador LOS del terminal òptic està encès
# i si l'indicador d'Internet del router està encès. Indicar primer:
# - si cal encendre el router 
# - si ja està encès, comprovar si cal revisar el cable de fibra (LOS encès)
# - si cal contactar amb el proveïdor (Internet apagat) 
# - si la connexió funciona correctament. 
# Considera els casos en aquest ordre.
router = int(input("Estat del router (1 = Encès, 0 = Apagat): "))
indicador_los = int(input("Estat de l'indicador LOS (1 = Encès, 0 = Apagat): "))
internet = int(input("Estat de l'indicador d'internet (1 = Encès, 0 = Apagat): "))

if router == 0:
    print("Cal encendre el router")
else:
    if indicador_los == 1:
        print("Cal revisar el cable de fibra òptica")
    elif internet == 0:
        print("NO HI HA INTERNET, Cal contactar amb el proveïdor.")
    else: 
        print("LA CONNEXIÓ FUNCIONA CORRECTAMENT")


#Exercici 10: Prioritat d'una incidència de xarxa.
#1. Demanar si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. 
# - Rebutja un nombre negatiu d'usuaris. 
#2. Classifica segons:
# - Prioritat crítica: si afecta un servei crític i no hi ha
#  alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa
# - Prioritat alta: si afecta almenys 10 usuaris o un servei crític
# - Prioritat baixa: qualsevol altre cas
incidencia = (input("L'incidència afecta un servei crític? (Si o No): "))
nombre_usuaris = int(input("Nombre d'usuaris afectats: "))
alternativa = (input("Hi ha una alternativa de connexió disponible? (Si o No): "))

if nombre_usuaris > 0:
    if (incidencia == 'Si' and alternativa == 'No') or (nombre_usuaris >= 50 and alternativa == 'No'):
        print("PRIORITAT CRÍTICA")
    elif incidencia == 'Si' or nombre_usuaris >= 10:
        print("PRIORITAT ALTA")
    else:
        print("PRIORITAT BAIXA")
else:
    print("El nombre d'usuaris NO pot ser negatiu")
    