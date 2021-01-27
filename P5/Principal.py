from Model.Agenda import Agenda
from Model.Usuario import Usuario
import linecache

usuario = Usuario("sara", "z", 959331728)

x = Agenda()

print("hola " + x.buscarTelefono(usuario) + "hola")

archivo = open("file.txt", "r+")

# with open("file.txt", "r") as f:
#    lines = f.readlines()
# with open("file.txt", "w") as f:
#    print(len(f.readlines()))
#    for line in lines:
#        if line.strip("\n") != "Nombre: jose ":
#            f.write(line)
