class ModeloDePresupuesto:
    # Datos comerciales

    # Metodo constructor
    def __init__(self, cliente, empresa, fecha, servicio, importe, vencimiento):
        print(self.divline)
        print("\tGENERACIÓN DEL PRESUPUESTO")
        print(self.divline)
        self.cliente = cliente
        self.empresa = empresa
        self.fecha = fecha
        self.servicio = servicio
        self.importe = importe
        self.vencimiento = vencimiento
        self.calcular_iva()
        self.calcular_neto()

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def encabezado_nombre(self):
        return self.__encabezado_nombre

    @encabezado_nombre.setter
    def encabezado_nombre(self, encabezado_nombre):
        self.__encabezado_nombre = encabezado_nombre

    @property
    def encabezado_web(self):
        return self.__encabezado_web

    @encabezado_web.setter
    def encabezado_web(self, encabezado_web):
        self.__encabezado_web = encabezado_web

    @property
    def encabezado_email(self):
        return self.__encabezado_email

    @encabezado_email.setter
    def encabezado_email(self, encabezado_email):
        self.__encabezado_email = encabezado_email

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self, servicio):
        self.__servicio = servicio

    @property
    def importe(self):
        return self.__importe

    @importe.setter
    def importe(self, importe):
        self.__importe = importe

    @property
    def vencimiento(self):
        return self.__vencimiento

    @vencimiento.setter
    def vencimiento(self, vencimiento):
        self.__vencimiento = vencimiento

    @property
    def monto_iva(self):
        return self.__monto_iva

    @property
    def divline(self):
        return self.divline

    @property
    def IVA(self):
        return self.IVA

    @property
    def neto(self):
        return self.__neto

    __titulo = "PRESUPUESTO"
    __encabezado_nombre = "Eugenia Bahit"
    __encabezado_web = "www.eugeniabahit.com.ar"
    __encabezado_email = "mail@mail.com"

    # Datos impositivos
    IVA = 21

    # Propiedades relativas al formato
    divline = "=" * 80

    # Calcular IVA
    def calcular_iva(self):
        self.__monto_iva = float(self.__importe) * float(self.IVA / 100)

    # Calcula el monto total del presupuesto
    def calcular_neto(self):
        self.__neto = float(self.__importe) + float(self.__monto_iva)

    # Montar el presupuesto
    def montar_presupuesto(self):
        """Esta función se encarga de armar todo el presupuesto"""
        txt = '\n' + self.divline + '\n'
        txt += '\t' + self.__encabezado_nombre + '\n'
        txt += '\tWeb Site: ' + self.__encabezado_web + ' | '
        txt += 'E-mail: ' + self.__encabezado_email + '\n'
        txt += self.divline + '\n'
        txt += '\t' + self.__titulo + '\n'
        txt += self.divline + '\n\n'
        txt += '\tFecha: ' + self.__fecha + '\n'
        txt += '\tEmpresa: ' + self.__empresa + '\n'
        txt += '\tCliente: ' + self.__cliente.nombre + '\n'
        txt += self.divline + '\n\n'
        txt += '\tDetalle del servicio:\n'
        txt += '\t' + self.__servicio + '\n\n'
        txt += '\tImporte: €%0.2f | IVA: €%0.2f\n' % (float(self.__importe), float(self.__monto_iva))
        txt += '-' * 80
        txt += '\n\tMONTO TOTAL: €%0.2f\n' % (float(self.__neto))
        txt += self.divline + '\n'
        return txt

    def compararPresupuestos(self, presupuesto):
        exito = False
        if isinstance(presupuesto, ModeloDePresupuesto):
            if self.__neto == presupuesto.__neto:
                exito = True
        return exito