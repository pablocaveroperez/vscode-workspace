import linecache


class Agenda:

    def __init__(self):
        open("file.txt", "a+")

    def añadirEntrada(self, oUsuario):
        archivo = open("file.txt", "a+")
        lines = archivo.read()
        lines += "\nNombre: {nombre} \nApellido: {apellido} \nTelefono: {telefono}\n "
        archivo.write(lines.format(nombre=oUsuario.nombre, apellido=oUsuario.apellido, telefono=oUsuario.telefono))

    def buscarTelefono(self, oUsuario):
        x = ""
        contador = 0

        with open("file.txt", 'r') as read_obj:
            for line in read_obj:
                contador += 1
                if "Nombre: " + oUsuario.nombre in line:

                    valor = (linecache.getline("file.txt", contador + 1))[:-1]

                    if "Apellido: " + oUsuario.apellido == valor:
                        x = (linecache.getline("file.txt", contador + 2))
                        break

        return x
