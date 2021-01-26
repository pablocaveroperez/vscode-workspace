from P1.Persona import Persona

class Vendedor(Persona):
    def __init__(self, NIF, nombre, apellidos, usuario, password):
        super().__init__(NIF, nombre, apellidos)
        self.telefono = usuario
        self.direccion = password

    @property
    def usuario(self):
        return self.usuario
    @usuario.setter
    def telefono(self, usuario):
        self.usuario = str(usuario)

    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, password):
        self.password = str(password)
    
    def __str__(self):
        txt = super().__str__()
        txt += "Usuario: " + self.usuario
        txt += "\Password: " + self.password
        return txt