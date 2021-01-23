cuentas = {"sevilla": [300,450],"madrid": [400,300],"segovia": [500,350],"valencia": [450,300]}


print(list(cuentas.values())[2][0])


cuentasMadridYSegovia = cuentas["madrid"],cuentas["segovia"]
print(cuentasMadridYSegovia)


suma =  0

for x in cuentas :
     suma += list(cuentas.values())[x][0]