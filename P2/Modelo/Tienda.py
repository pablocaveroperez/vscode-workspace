from P1.Modelo.Cliente import Cliente
from P1.Modelo.Pedido import Pedido
from P1.Modelo.Vendedor import Vendedor
import sqlite3


class Tienda:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()

    def altaCliente(self, cliente):
        exito = False
        if isinstance(cliente, Cliente):
            self.__personas.append(cliente)
            exito = True
        return exito

    def altaVendedor(self, vendedor):
        exito = False
        if isinstance(vendedor, Vendedor):
            self.__personas.append(vendedor)
            exito = True
        return exito

    def altaPedido(self, pedido):
        exito = False
        if isinstance(pedido, Pedido):
            self.__pedidos.append(pedido)
            exito = True
        return exito

    def numClientes(self):
        iCantidad = 0
        for x in self.__personas:
            if isinstance(x, Cliente):
                iCantidad += 1
        return iCantidad

    def numVendedores(self):
        iCantidad = 0
        for x in self.__personas:
            if isinstance(x, Vendedor):
                iCantidad += 1
        return iCantidad

    def numPedidos(self):
        return int(len(self.__pedidos))

    def importeTotalPedidos(self):
        importeTotal = float(0)
        for x in self.__pedidos:
            importeTotal += float(x.total)
        return importeTotal

    def listadoClientes(self):
        salida = ""
        for x in self.__personas:
            if isinstance(x, Cliente):
                salida += x.__str__()
        return salida

    def listadoVendedores(self):
        salida = ""
        for x in self.__personas:
            if isinstance(x, Vendedor):
                salida += x.__str__()
        return salida

    def listadoPedidosFecha(self, fecha):
        salida = ""
        for x in self.__pedidos:
            if x.fechaPedido == fecha:
                salida += x.__str__()
        return salida

    def crearTablaCliente(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cliente(dni text PRIMARY KEY, nombre text, apellidos text, telefono integer, direccion text)")
        self.conn.commit()

    def crearTablaVendedor(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS vendedor(dni text PRIMARY KEY, nombre text, apellidos text, usuario text, password text)")
        self.conn.commit()

    def crearTablaPedido(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS pedido(oCliente text PRIMARY KEY, oVendedor text PRIMARY KEY, fechaPedido text, total real)")
        self.conn.commit()