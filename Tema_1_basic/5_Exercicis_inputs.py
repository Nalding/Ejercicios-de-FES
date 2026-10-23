#Exercici 1:
#Demanar el nom d'un tècnic i el nom de la xarxa que està instal·lant.
#Després mostra un missatge amb aquesta informació.
tecnic = input("Nom del tècnic: ")
xarxa = input("Nom de la xarxa: ")

print(f"El tècnic {tecnic} està instal·lant la xarxa {xarxa}.")


#Exercici 2:
#Demanar la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
#en Gbps. Després mostrar quants segons caldrien per transmetre 1 GB de dades.
#Suposem que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_fibra = float(input("Longitud de la fibra (en km): "))
velocitat_transmissio = float(input("Velocitat de transmissió (en Gbps): "))

temps_total = 8 / velocitat_transmissio

print(f"Es necessiten {temps_total:.2f} segons per transmetre 1 GB.")


#Exercici 3:
#Demanar el nombre d'hores de feina, el preu per hora d'una instal·lació de xarxa i el preu del material.
#Després mostrar el cost total de la instal·lació.
hores_feina = float(input("Hores de feina: "))
preu_hora = float(input("Preu per hora (en euros): "))
preu_material = float(input("Preu del material (en euros): "))

cost_total = (hores_feina * preu_hora) + preu_material

print(f"El cost total de la instal·lació és de {cost_total} euros.")