#Exercici 2 - Bàsic. Conversions reutilitzables.
#1. Importar conversions amb l'àlies conv i utilitza les seves funcions.
#2. Convertir cada temperatura a kelvins i cada tensió a volts.
#Entrades següents. Sortides esperades en el mateix ordre:
# - [263.15, 273.15, 298.15] i [0.0, 3.3, 5.0].
# - Amb una llista buida, el resultat corresponent ha de ser [].
#3. Obtenir i mostrar dues llistes amb les conversions.
import conversions as conv

temperatures = [-10.0, 0.0, 25.0]
tensions_mv = [0, 3300, 5000]
temperatures_k = []
tensions_v = []

for temp in temperatures:
    temperatures_k.append(conv.celsius_a_kelvins(temperatures))

for tensio in tensions_mv:
    tensions_v.append(conv.milivolts_a_volts(tensions_mv))

print(temperatures_k)
print(tensions_v)