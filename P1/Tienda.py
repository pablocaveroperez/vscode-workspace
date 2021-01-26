from P1.Persona import Persona

class Tienda:
    __personas = []
    __pedidos = []

    def __init__(self, personas, pedidos):
        self.__personas = personas
        self.__pedidos = pedidos
    
    def altaCliente(self, cliente):
        self.__personas.append(cliente)

    def altaVendedor(self, ):
        