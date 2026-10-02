#Exercici 1:
#Crear variables per desar el nom d'un encaminador, la seva ubicació, el nombre de ports i si està encès. 
#Després, mostrar les dades en una frase utilitzant una f-string.
encaminador = "Router"
ubicació = "Casa"
nombre_ports = 5
encaminador_activat = True
print(f"Encaminador: {encaminador}; Ubicació: {ubicació}; Nombre de ports: {nombre_ports}; Encès: {encaminador_activat}")


#Exercici 2:
#Crear variables per desar els GB inclosos en un pla de dades mòbils i els GB consumits. 
#Calcular quants GB queden i mostrar el resultat.
#Després, actualitzar el consum amb un valor nou i tornar a calcular quants GB queden.
gb_inclosos = 10
gb_consumits = 4
gb_restants = gb_inclosos - gb_consumits
print(f"GB restants: {gb_restants} GB")

gb_consumits = 8
gb_restants = gb_inclosos - gb_consumits
print(f"GB restants després de l'actualització: {gb_restants} GB")
