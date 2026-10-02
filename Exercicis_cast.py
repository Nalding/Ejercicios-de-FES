#Exercici 1:
#Demanar a l'usuari quants paquets ha rebut un encaminador i convertir-lo a un nombre enter.
#Sumar 1200 paquets i mostra el total.
paquets = int(input("Quants paquets ha rebut l'encaminador?: "))
total_paquets = paquets + 1200
print(f"El total de paquets és: {total_paquets}")


#Exercici 2:
#Demanar a l'usuari la velocitat d'una connexió en Mbps i convertir-lo a nombre decimal.
#Calcular la velocitat equivalent en MB/s dividint-la per 8 i després mostrar el resultat.
velocitat_connexio = float(input("Quina és la velocitat de la connexió en Mbps?: "))
velocitat_MBs = velocitat_connexio / 8
print(f"Velocitat equivalent: {velocitat_MBs:.2f} MB/s")
