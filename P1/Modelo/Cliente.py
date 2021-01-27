from P1.Modelo.Persona import Persona


class Cliente(Persona):
    def __init__(self, NIF, nombre, apellidos, telefono, direccion):
        super().__init__(NIF, nombre, apellidos)
        self.__telefono = telefono
        self.__direccion = direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = int(telefono)

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = str(direccion)

    def __str__(self):
        txt = super().__str__()
        txt += "Telefono: " + str(self.__telefono)
        txt += "\nDireccion: " + self.__direccion
        return txt
