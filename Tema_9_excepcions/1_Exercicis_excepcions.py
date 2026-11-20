#Exercici 1 - Bàsic. Conversió segura de tensions.
#1. Per a cada text de tensions, intentar convertir-lo amb float.
#2. Capturar ValueError i mostra 'Tensió incorrecta' en aquest cas.
#3. Utilitzar else per mostrar la conversió quan sigui correcta.
# - Sortida esperada, una línia per entrada: 3.3 / Tensió incorrecta / 0.0.
# - Cas límit: '0' és una mesura vàlida.
tensions = ["3.3", "avaria", "0"]
for text in tensions:
    try:
        tensio = float(text)
    except ValueError:
        print("Tensió incorrecta")
    else:
        print(tensio)


#Exercici 2 - Bàsic. Humitat amb contracte.
#1. Definir validar_humitat(text) que retorni un float finit dins [0, 100].
#2. Generar ValueError per a text no numèric, valors no finits o fora de rang.
#3. Utilitza math.isfinite després de convertir el text.
# - Entrades: '0', '100', '45.5', '-1', '101', 'nan', 'inf', 'error'.
# - Retorns esperats per a les tres primeres: 0.0, 100.0 i 45.5.
#La resta han de produir ValueError, gestionat en les demostracions.
entrades_humitat = ["0", "100", "45.5", "-1", "101", "nan", "inf", "error"]
import math

def validar_humitat(text):
    humitat = float(text)

    if not math.isfinite(humitat):
        raise ValueError("La humitat ha de ser finita")
    if humitat < 0 or humitat > 100:
        raise ValueError("El valor está fora del rang")
        
    return humitat

for text in entrades_humitat:
    try:
        humitat = validar_humitat(text)
    except ValueError as error:
        print(f"S'ha rebujat {text}: {error}")
    else:
        print(humitat)


# Exercici 3 - Intermedi. Fitxer absent i finalització
# Dins de TemporaryDirectory crea només una ruta a 'absent.txt' amb Path.
# Intenta obrir-la en mode lectura, amb encoding='utf-8'.
# Captura FileNotFoundError i mostra 'Fitxer absent'.
# Utilitza finally per mostrar 'Intent acabat' tant si hi ha error com si no.
# Sortida esperada: Fitxer absent / Intent acabat.
# Segona prova: crea un fitxer temporal que contingui 'T1=21.5' i repeteix.
# Sortida esperada: T1=21.5 / Intent acabat.
# Mantén tots els fitxers dins de la carpeta temporal.
# TODO: importa Path i TemporaryDirectory i prova els dos camins.

# Exercici 4 - Repte opcional. Filtrar lectures de temperatura
# Defineix filtrar_temperatures(textos) que retorni (valides, rebutjades).
# valides és la llista de floats finits dins del rang simulat [-40, 85] °C.
# rebutjades és el nombre d'entrades que no es poden acceptar.
# Crea una funció validar_temperatura(text) i reutilitza-la al bucle.
# Entrada següent. Retorn esperat: ([-40.0, 21.5, 85.0], 3).
# Amb [] ha de retornar ([], 0). Amb ['nan', 'inf'] ha de retornar ([], 2).
textos = ["-40", "21.5", "85", "86", "avaria", "nan"]
# TODO: captura ValueError per cada lectura i continua amb les següents.