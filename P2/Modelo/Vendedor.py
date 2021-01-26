from P1.Modelo.Persona import Persona


class Vendedor(Persona):
    def __init__(self, NIF, nombre, apellidos, usuario, password):
        super().__init__(NIF, nombre, apellidos)
        self.__usuario = usuario
        self.__password = password

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = str(usuario)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = str(password)

    def __str__(self):
        txt = super().__str__()
        txt += "Usuario: " + self.__usuario
        txt += "\nPassword: " + self.__password
        return txt
