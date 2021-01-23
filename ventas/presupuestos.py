# -*- coding: utf-8 -*-
print("Modelos de presupuestos")

class ModeloDePresupuesto:
    # Datos comerciales
    

    @property
    def titulo(self):
        return self.titulo
    @titulo.setter
    def titulo(self, titulo):
        self.titulo = titulo

    @property
    def encabezado_nombre(self):
        return self.encabezado_nombre
    @encabezado_nombre.setter
    def encabezado_nombre(self, encabezado_nombre):
        self.encabezado_nombre = encabezado_nombre

    @property
    def encabezado_web(self):
        return self.encabezado_web
    @encabezado_web.setter
    def encabezado_web(self, encabezado_web):
        self.encabezado_web = encabezado_web

    @property
    def encabezado_email(self):
        return self.encabezado_email
    @encabezado_email.setter
    def encabezado_email(self, encabezado_email):
        self.encabezado_email = encabezado_email

    @property
    def cliente(self):
        return self.cliente
    @cliente.setter
    def cliente(self, cliente):
        self.cliente = cliente

    @property
    def empresa(self):
        return self.empresa
    @empresa.setter
    def empresa(self, empresa):
        self.empresa = empresa

    @property
    def fecha(self):
        return self.fecha
    @fecha.setter
    def fecha(self, fecha):
        self.fecha = fecha

    @property
    def servicio(self):
        return self.servicio
    @servicio.setter
    def servicio(self, servicio):
        self.servicio = servicio

    @property
    def importe(self):
        return self.importe
    @importe.setter
    def importe(self, importe):
        self.importe = importe

    @property
    def vencimiento(self):
        return self.vencimiento
    @vencimiento.setter
    def vencimiento(self, vencimiento):
        self.vencimiento = vencimiento

    @property
    def monto_iva(self):
        return self.monto_iva

    @property
    def divline(self):
        return self.divline

    @property
    def IVA(self):
        return self.IVA

    @property
    def neto(self):
        return self.neto

    titulo = "PRESUPUESTO"
    encabezado_nombre = "Eugenia Bahit"
    encabezado_web = "www.eugeniabahit.com.ar"
    encabezado_email = "mail@mail.com"

    
    # Datos impositivos
    IVA = 21

    # Propiedades relativas al formato
    divline = "="*80

    # Setear los datos del cliente
    def set_cliente(self, cliente, empresa):
        self.empresa = empresa
        self.cliente = cliente

    # Setear los datos basicos ́del presupuesto
    def set_datos_basicos(self, fecha, servicio, importe, vencimiento):
        self.fecha = fecha
        self.servicio = servicio
        self.importe = importe
        self.vencimiento = vencimiento

    # Calcular IVA
    def calcular_iva(self):
        self.monto_iva = self.importe*self.IVA/100
        return self.monto_iva

    # Calcula el monto total del presupuesto
    def calcular_neto(self):
        self.neto = self.importe+self.monto_iva
        return self.neto

    # Montar el presupuesto
    def montar_presupuesto(self):
        """Esta función se encarga de armar todo el presupuesto"""
        txt = '\n'+self.divline+'\n'
        txt += '\t'+self.encabezado_nombre+'\n'
        txt += '\tWeb Site: '+self.encabezado_web+' | '
        txt += 'E-mail: '+self.encabezado_email+'\n'
        txt += self.divline+'\n'
        txt += '\t'+self.titulo+'\n'
        txt += self.divline+'\n\n'
        txt += '\tFecha: '+self.fecha+'\n'
        txt += '\tEmpresa: '+self.empresa+'\n'
        txt += '\tCliente: '+self.cliente+'\n'
        txt += self.divline+'\n\n'
        txt += '\tDetalle del servicio:\n'
        txt += '\t'+self.servicio+'\n\n'
        txt += '\tImporte: €%0.2f | IVA: €%0.2f\n' % (self.importe, self.monto_iva)
        txt += '-'*80
        txt += '\n\tMONTO TOTAL: €%0.2f\n' % (self.neto)
        txt += self.divline+'\n'
        return txt

    # Metodo constructor
    def __init__(self, cliente, empresa, fecha, servicio, importe, vencimiento):
        print(self.divline)
        print("\tGENERACIÓN DEL PRESUPUESTO")
        print(self.divline)
        self.set_cliente(cliente, empresa)
        self.set_datos_basicos(fecha, servicio, importe, vencimiento)
        self.calcular_iva()
        self.calcular_neto()
        self.montar_presupuesto()

class Cliente:
    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def apellidos(self):
        return self.apellidos
    @apellidos.setter
    def apellidos(self, apellidos):
        self.apellidos = apellidos

    def setCliente(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    # Metodo constructor
    def __init__(self, nombre, apellidos):
        self.setCliente(nombre, apellidos)