import linecache


class Agenda:

    def __init__(self):
        open("file.txt", "a+")

    def anadirEntrada(self, oUsuario):
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

    def borrarEntrada(self, oUsuario):
        x = 0

        with open("file.txt", 'r') as read_obj:
            contador = 0
            for line in read_obj:
                contador += 1
                if "Nombre: " + oUsuario.nombre in line:

                    valor = (linecache.getline("file.txt", contador + 1))[:-1]

                    if "Apellido: " + oUsuario.apellido == valor:
                        x = contador
                        break

        for d in range(3):
            a_file = open("file.txt", "r")

            lines = a_file.readlines()
            a_file.close()

            del lines[x - 1]

            new_file = open("file.txt", "w+")

            for line in lines:
                new_file.write(line)

            new_file.close()