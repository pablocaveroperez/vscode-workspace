from P1.Modelo.Persona import Persona
from P1.Modelo.Cliente import Cliente
from P1.Modelo.Vendedor import Vendedor
from P1.Modelo.Pedido import Pedido


class Tienda:
    __personas = []
    __pedidos = []

    @property
    def personas(self):
        return self.__personas

    @personas.setter
    def personas(self, personas):
        self.__personas = personas

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos

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
                iCantidad += iCantidad
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
