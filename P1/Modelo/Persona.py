class Persona:
    def __init__(self, NIF, nombre, apellidos):
        self.__NIF = str(NIF)
        self.__nombre = str(nombre)
        self.__apellidos = str(apellidos)

    @property
    def NIF(self):
        return self.__NIF

    @NIF.setter
    def NIF(self, NIF):
        self.__NIF = str(NIF)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = str(nombre)

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = str(apellidos)

    def __str__(self):
        txt = "\n**Persona**\n"
        txt += "Nombre:" + str(self.__nombre) + "\n"
        txt += "Apellidos: " + str(self.__apellidos) + "\n"
        txt += "NIF: " + str(self.__NIF) + "\n"
        return txt
