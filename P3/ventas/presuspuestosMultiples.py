from P3.ventas.presupuestos import ModeloDePresupuesto


class ModeloDePresupuestoMultiple(ModeloDePresupuesto):
    def __int__(self):
        self.servicios = []

    def buscarServicio(self, servicio):
        exito = False
        i = 0
        while i < len(self.servicios) and exito:
            if self.servicios[i] == servicio:
                exito = True
            else:
                i += 1
        if not exito:
            i = -1
        return i

    def modificarServicio(self, servicio):
        posicion = self.buscarServicio(servicio)
        if posicion != -1:
            self.servicios.insert(posicion, servicio)
        return posicion

    def eliminarServicio(self, servicio):
        posicion = self.buscarServicio(servicio)
        if posicion != -1:
            self.servicios.pop(posicion)
        return posicion

    def addServicio(self, servicio):
        exito = False
        if self.buscarServicio(servicio) == -1:
            self.servicios.append(servicio)
            exito = True
        return exito

    def listarServicios(self):
        salida = "\n" + self.divline
        salida += "\nLista de servicios"
        salida += "\n" + self.divline
        for servicio in self.servicios:
            salida += servicio
        salida += "\n" + self.divline
        return salida

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
        txt += '\t' + self.listarServicios() + '\n\n'
        txt += '\tImporte: €%0.2f | IVA: €%0.2f\n' % (float(self.__importe), float(self.__monto_iva))
        txt += '-' * 80
        txt += '\n\tMONTO TOTAL: €%0.2f\n' % (float(self.__neto))
        txt += self.divline + '\n'
        return txt
