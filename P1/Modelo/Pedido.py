class Pedido:
    def __init__(self, cliente, vendedor, fechaPedido, total):
        self.__oCliente = cliente
        self.__oVendedor = vendedor
        self.__fechaPedido = fechaPedido
        self.__total = total

    @property
    def oCliente(self):
        return self.__oCliente

    @oCliente.setter
    def oCliente(self, oCliente):
        self.__oCliente = oCliente

    @property
    def oVendedor(self):
        return self.__oVendedor

    @oVendedor.setter
    def oVendedor(self, oVendedor):
        self.__oVendedor = oVendedor

    @property
    def fechaPedido(self):
        return self.__fechaPedido

    @fechaPedido.setter
    def fechaPedido(self, fechaPedido):
        self.__fechaPedido = fechaPedido

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total == total

    def __str__(self):
        txt = "\n**Pedido**"
        txt += "\nFecha pedido: " + self.__fechaPedido
        txt += "\nTotal: " + str(self.__total) + "\n"
        txt += "Cliente: " + self.__oCliente.NIF
        txt += "Vendedor: " + self.__oVendedor.NIF
        return txt