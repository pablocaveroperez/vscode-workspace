from P4.modeloDePresupuestos import ModeloDePresupuesto
from ventas.presupuestos import Cliente

nombreCliente = "Pablo"
apellidoCliente = "Cavero"
cliente = Cliente()
cliente.nombre = nombreCliente
cliente.apellidos = apellidoCliente

empresa = "Medac"
fecha = "Lunes"
servicio = "Tecnico"
importe = 12
vencimiento = "Dentro de dos dias"

modeloDePresupuesto1 = ModeloDePresupuesto(cliente, empresa, fecha, servicio, importe, vencimiento)

empresa = "Medac"
fecha = "Martes"
servicio = "transporte"
importe = 10
vencimiento = "Hoy"

modeloDePresupuesto2 = ModeloDePresupuesto(cliente, empresa, fecha, servicio, importe, vencimiento)


empresa = "Medac"
fecha = "Miercoles"
servicio = "transporte"
importe = 12
vencimiento = "Terminado"

modeloDePresupuesto3 = ModeloDePresupuesto(cliente, empresa, fecha, servicio, importe, vencimiento)

modelos = [modeloDePresupuesto1, modeloDePresupuesto2, modeloDePresupuesto3]

print(modelos[0].compararPresupuestos(modelos[2]))
print(modelos[1].compararPresupuestos(modelos[2]))
print(modelos[0].compararPresupuestos(modelos[1]))

