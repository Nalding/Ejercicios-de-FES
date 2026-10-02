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
  