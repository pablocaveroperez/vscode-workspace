from P1.Persona import Persona
from P1.Cliente import Cliente
from P1.Vendedor import Vendedor
from P1.Pedido import Pedido

class Tienda:
    __personas = []
    __pedidos = []

    def __init__(self, personas, pedidos):
        self.__personas = personas
        self.__pedidos = pedidos

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
        if (type(cliente) == Cliente):
            self.__personas.append(cliente)
            exito = True
        return exito


    def altaVendedor(self, vendedor):
        exito = False
        if (type(vendedor) == Vendedor):
            self.__personas.append(vendedor)
            exito = True
        return exito

    def altaPedido(self, pedido):
        exito = False
        if (type(pedido) == Pedido):
            self.__pedidos.append(pedido)
            exito = True
        return exito

    def numClientes(self):
        iCantidad = 0
        for x in self.__personas:
            if (type(x) == Cliente):
                iCantidad += iCantidad
        return iCantidad
    
    def numVendedores(self):
        iCantidad = 0
        for x in self.__personas:
            if (type(x) == Vendedor):
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
            if (type(x) == Cliente):
                salida += x.__str__()
        return salida

    def listadoVendedores(self):
        salida = ""
        for x in self.__personas:
            if (type(x) == Vendedor):
                salida += x.__str__()
        return salida

    def listadoPedidosFecha(self, fecha):
        salida = ""
        for x in self.__pedidos:
            if (x.fechaPedido == fecha):
                salida += x.__str__()
        return salida
