#Exercici 7: Corrent en resistències.
#En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# - resistencies = [100, 220, 470, 1000]
#Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcular i imprimir
#el corrent que circula per cada resistència, en ampers.
resistencies = [100, 220, 470, 1000]
intensitat = 0

for idx, r in enumerate(resistencies):
    intensitat = 12 / r
    print(f"Per la {idx} resistencia la intensitat és: {intensitat:.2f}")
