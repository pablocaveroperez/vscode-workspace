from P1.Modelo.Cliente import Cliente
from P1.Modelo.Pedido import Pedido
from P1.Modelo.Vendedor import Vendedor
import sqlite3


class Tienda:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
        self.crearTablaCliente()
        self.crearTablaVendedor()
        self.crearTablaPedido()

    def altaCliente(self, cliente):
        exito = False
        if isinstance(cliente, Cliente):
            self.cursor.execute(
                "INSERT INTO cliente VALUES('" + cliente.NIF + ", '" + cliente.nombre + "', '" + cliente.apellidos + "', " + cliente.telefono + ", '" + cliente.direccion + "' )")
            self.conn.commit()
            exito = True
        return exito

    def altaVendedor(self, vendedor):
        exito = False
        if isinstance(vendedor, Vendedor):
            self.cursor.execute(
                "INSERT INTO vendedor VALUES('" + vendedor.NIF + ", '" + vendedor.nombre + "', '" + vendedor.apellidos + "', '" + vendedor.usuario + "', '" + vendedor.password + "' )")
            self.conn.commit()
            exito = True
        return exito

    def altaPedido(self, pedido):
        exito = False
        if isinstance(pedido, Pedido):
            self.cursor.execute(
                "INSERT INTO pedido VALUES('" + pedido.oCliente + ", '" + pedido.oVendedor + "', '" + pedido.fechaPedido + "', " + pedido.total + ")")
            self.conn.commit()
            exito = True
        return exito

    def numClientes(self):
        iCantidad = self.cursor.execute('SELECT COUNT(*) FROM cliente').fetchall()
        return iCantidad

    def numVendedores(self):
        iCantidad = self.cursor.execute('SELECT COUNT(*) FROM vendedor').fetchall()
        return iCantidad

    def numPedidos(self):
        iCantidad = self.cursor.execute('SELECT COUNT(*) FROM pedido').fetchall()
        return iCantidad

    def importeTotalPedidos(self):
        importeTotal = self.cursor.execute('SELECT SUM(total) FROM pedido')
        return importeTotal

    def listadoClientes(self):
        salida = ""
        self.cursor.execute('SELECT * FROM cliente')
        rows = self.cursor.fetchall()

        for row in rows:
            salida += row

        return salida

    def listadoVendedores(self):
        salida = ""
        self.cursor.execute('SELECT * FROM vendedor')
        rows = self.cursor.fetchall()

        for row in rows:
            salida += row

        return salida

    def listadoPedidosFecha(self, fecha):
        salida = ""
        self.cursor.execute('SELECT * FROM pedido WHERE fechaPedido = ' + fecha + ' ')
        rows = self.cursor.fetchall()

        for row in rows:
            salida += row

        return salida

    def crearTablaCliente(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cliente(dni text PRIMARY KEY, nombre text, apellidos text, "
                            "telefono integer, direccion text)")
        self.conn.commit()

    def crearTablaVendedor(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS vendedor(dni text PRIMARY KEY, nombre text, apellidos text, usuario text, "
            "password text)")
        self.conn.commit()

    def crearTablaPedido(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS pedido(idPedido integer PRIMARY KEY AUTOINCREMENT , oCliente text, oVendedor "
            "text, fechaPedido "
            "text, total real, FOREIGN KEY (oCliente) REFERENCES cliente(dni), FOREIGN KEY (oVendedor) REFERENCES "
            "vendedor(dni))")
        self.conn.commit()

    def cerrarConexion(self):
        self.conn.close()
