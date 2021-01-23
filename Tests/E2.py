cuentas = [(300,450),(400,300),(500,350),(450,300)]
# el primer numero indica ingresos, el segundo gastos.

impares = cuentas[::2]
print(impares)

pares = cuentas[1::2]
print(pares)

dosPrimeros = cuentas[:2]
print(dosPrimeros)

dosUltimos = cuentas[len(cuentas)-2:]
print(dosUltimos)

primeroYultimo = cuentas[::len(cuentas)-1]
print(primeroYultimo)