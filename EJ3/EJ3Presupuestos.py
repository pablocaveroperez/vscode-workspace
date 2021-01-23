from ventas.presupuestos import Cliente, ModeloDePresupuesto


cliente = Cliente(input("\nIntroduce el nombre del cliente: "), input("\nIntroduce los apellidos del cliente: "))
empresa = input("\nIntroduce la empresa: ")
fecha = input("\nIntroduce la fecha: ")
servicio = input("\nIntroduce el servicio: ")
importe = input("\nIntroduce el importe: ")
vencimiento = input("\nIntroduce el vencimiento: ")

modeloDePresupuesto = ModeloDePresupuesto(cliente, empresa, fecha, servicio, importe, vencimiento)