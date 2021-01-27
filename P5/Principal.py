from Model.Agenda import Agenda
from Model.Usuario import Usuario
import linecache

usuario = Usuario("manuel", "x", 959331728)

x = Agenda()

print("hola " + x.buscarTelefono(usuario) + "hola")

x.borrarEntrada(usuario)