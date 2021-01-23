cuentas = {("sevilla", 41013): [300, 450, True], ("madrid", 18650): [
    400, 300, False], ("segovia", 28901): [500, 350, False], ("segovia", 28902): [450, 500, True]}

balancesPositivos = []

for x in cuentas.values():
    if x[0] > x[1]:
        balancesPositivos.append(x[0] - x[1])

print("Balances positivos:", balancesPositivos)
umbral = int(input("Indique umbral minimo de balance positivo para buscar:"))

encontrado = False
i = 0
while encontrado == False and i < balancesPositivos.__len__():
    if balancesPositivos[i] >= umbral:
        encontrado = True
    else:
        i += 1

if encontrado:
    print("Se ha encontrado este balance: " + str(balancesPositivos[i]))
else:
    print("No se ha encontrado ningun balance superior al umbral.")
