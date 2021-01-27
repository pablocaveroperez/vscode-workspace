import linecache


class Agenda:

    def __init__(self):
        open("file1.txt", "a+")

    def añadirEntrada(self, oUsuario):
        archivo = open("file1.txt", "a+")
        lines = archivo.read()
        lines += "\nNombre: {nombre} \nApellido: {apellido} \nTelefono: {telefono}\n "
        archivo.write(lines.format(nombre=oUsuario.nombre, apellido=oUsuario.apellido, telefono=oUsuario.telefono))

    def buscarTelefono(self, oUsuario):
        x = ""
        contador = 0

        with open("file1.txt", 'r') as read_obj:
            for line in read_obj:
                contador += 1
                if "Nombre: " + oUsuario.nombre in line:

                    valor = (linecache.getline("file1.txt", contador + 1))[:-1]

                    if "Apellido: " + oUsuario.apellido == valor:
                        x = (linecache.getline("file1.txt", contador + 2))
                        break

        return x
