
class Usuario:

    def __init__(self,nombre,apellido,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono



    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre  

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self,telefono):
        self.__telefono = telefono


    def __str__(self):
        x = ""

        x+= "Nombre: "+self.__nombre+"\n"
        x+= "Apellido: "+self.__apellido+"\n"
        x+= "Telefono: "+self.__telefono+"\n"

        return x