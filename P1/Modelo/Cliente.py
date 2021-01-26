from P1.Modelo.Persona import Persona

class Cliente(Persona):
    def __init__(self, NIF, nombre, apellidos, telefono, direccion):
        super().__init__(NIF, nombre, apellidos)
        self.telefono = telefono
        self.direccion = direccion

    @property
    def telefono(self):
        return self.telefono
    @telefono.setter
    def telefono(self, telefono):
        self.telefono = int(telefono)

    @property
    def direccion(self):
        return self.direccion
    @direccion.setter
    def direccion(self, direccion):
        self.direccion = str(direccion)
    
    def __str__(self):
        txt = super().__str__()
        txt += "Telefono: " + int(self.telefono)
        txt += "\nDireccion: " + self.direccion
        return txt