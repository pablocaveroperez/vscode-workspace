# -*- coding: utf-8 -*-
print("Modelos de presupuestos")

class ModeloDePresupuesto:
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
    def 

    # Datos comerciales
    titulo = "PRESUPUESTO"
    encabezado_nombre = "Eugenia Bahit"
    encabezado_web = "www.eugeniabahit.com.ar"
    encabezado_email = "mail@mail.com"

    # Datos impositivos
    IVA = 21

    # Propiedades relativas al formato
    divline = "="*80

    # Setear los datos del cliente
    def set_cliente(self):
        self.empresa = input('\tEmpresa: ')
        self.cliente = Cliente()
    # Setear los datos basicos ́del presupuesto

    def set_datos_basicos(self):
        self.fecha = input('\tFecha: ')
        self.servicio = input('\tDescripción del servicio: ')
        importe = input('\tImporte bruto: €')
        self.importe = float(importe)
        self.vencimiento = input('\tFecha de caducidad: ')

    # Calcular IVA
    def calcular_iva(self):
        self.monto_iva = self.importe*self.IVA/100

    # Calcula el monto total del presupuesto
    def calcular_neto(self):
        self.neto = self.importe+self.monto_iva

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
        print(txt)

    # Metodo constructor
    def __init__(self):
        print(self.divline)
        print("\tGENERACIÓN DEL PRESUPUESTO")
        print(self.divline)
        self.set_cliente()
        self.set_datos_basicos()
        self.calcular_iva()
        self.calcular_neto()
        self.montar_presupuesto()

class Cliente:
    def setCliente(self):
        self.nombre = input("\nIntroduzca su nombre: ")
        self.apellidos = input("\nIntroduzca sus apellidos: ")

    # Metodo constructor
    def __init__(self):
        self.setCliente()