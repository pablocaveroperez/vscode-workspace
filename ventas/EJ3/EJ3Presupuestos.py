from ventas.presupuestos import *

#nombreCliente = input("\nIntroduce el nombre del cliente: ")
#apellidoCliente = input("\nIntroduce los apellidos del cliente: ")

nombreCliente = "Pablo"
apellidoCliente = "Cavero"
cliente = Cliente()
cliente.nombre = nombreCliente
cliente.apellidos = apellidoCliente
empresa = input("\nIntroduce la empresa: ")
fecha = input("\nIntroduce la fecha: ")
servicio = input("\nIntroduce el servicio: ")
importe = input("\nIntroduce el importe: ")
vencimiento = input("\nIntroduce el vencimiento: ")

#empresa = "Medac"
#fecha = "Manaña"
#servicio = "transporte"
#importe = 12
#vencimiento = "Hoy"

modeloDePresupuesto = ModeloDePresupuesto(cliente, empresa, fecha, servicio, importe, vencimiento)
print(modeloDePresupuesto.montar_presupuesto())