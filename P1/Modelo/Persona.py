class Persona:
    def __init__(self, NIF, nombre, apellidos):
        self.NIF = str(NIF)
        self.nombre = str(nombre)
        self.apellidos = str(apellidos)

    @property
    def NIF(self):
        return self.NIF
    @NIF.setter
    def NIF(self, NIF):
        self.NIF = str(NIF)

    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = str(nombre)

    @property
    def apellidos(self):
        return self.apellidos
    @apellidos.setter
    def apellidos(self, apellidos):
        self.apellidos = str(apellidos)

    def __str__(self):
        txt = "**Persona**\n"
        txt += "Nombre:" + str(self.nombre) + "\n"
        txt += "Apellidos: " + str(self.apellidos) + "\n"
        txt += "NIF: " + str(self.NIF) + "\n"
        return txt
    