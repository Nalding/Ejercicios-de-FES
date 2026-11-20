#Exercici 3 - Intermedi. Fitxer absent i finalització.
#1. Dins de TemporaryDirectory crear només una ruta a 'absent.txt' amb Path.
#2. Intentar obrir-la en mode lectura, amb encoding='utf-8'.
#3. Capturar FileNotFoundError i mostrar 'Fitxer absent'.
#4. Utilitzar finally per mostrar 'Intent acabat' tant si hi ha error com si no.
# - Sortida esperada: Fitxer absent / Intent acabat.
#5. Segona prova: crear un fitxer temporal que contingui 'T1=21.5' i repetir el procés.
# - Sortida esperada: T1=21.5 / Intent acabat.
#S'han de mantenir tots els fitxers dins de la carpeta temporal.
# TODO: importa Path i TemporaryDirectory i prova els dos camins.
from tempfile import TemporaryDirectory
with TemporaryDirectory() as fitxer: