from P1.Modelo.Cliente import Cliente
from P1.Modelo.Pedido import Pedido
from P1.Modelo.Tienda import Tienda
from P1.Modelo.Vendedor import Vendedor

nif = "27582722b"
nombre = "Isnasi"
apellidos = "Rodriguez Barato"
telefono = 678945123
direccion = "calle santa rita s/n"
cliente = Cliente(nif, nombre, apellidos, telefono, direccion)
print(cliente)

nif = "28564258a"
nombre = "Manolin"
apellidos = "del Bosque"
usuario = "MaBosque"
password = "123456789"
vendedor = Vendedor(nif, nombre, apellidos, usuario, password)
print(vendedor)

fechaPedido = "Manana"
total = float(12.2)
pedido = Pedido(cliente, vendedor, fechaPedido, total)

tienda = Tienda()

print(tienda.numClientes())

tienda.altaCliente(cliente)

print(tienda.numClientes())

print(tienda.numVendedores())

tienda.altaVendedor(vendedor)

print(tienda.numVendedores())

print(tienda.numPedidos())

tienda.altaPedido(pedido)

print(tienda.numPedidos())

print("Listados")

print(tienda.listadoClientes())

print(tienda.listadoVendedores())

print(tienda.listadoPedidosFecha("Manana"))

print("Importe total")

print(tienda.importeTotalPedidos())
