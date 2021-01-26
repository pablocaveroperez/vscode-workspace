from P1.Cliente import Cliente
from P1.Vendedor import Vendedor

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