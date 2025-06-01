from poo.lib import FechaHora, Datos, Formato, Menu


class Cuenta:
    obd = Datos()

    def nueva(self, nc, ncl):
        print(f"<<DATOS DE LA CUENTA>>")
        self.__nc = nc
        print(f"No. cuenta: {nc}")
        self.__nm = self.obd.cadena("Nombre de la cuenta").upper()
        self.__suc = 0
        while self.__suc < 1 or self.__suc > 10:
            self.__suc = self.obd.entero("Sucursal")
        self.__fa = FechaHora().fecha()
        print(f"Fecha de apertura: {self.__fa}")
        self.__sal = 0
        while self.__sal < 1:
            self.__sal = self.obd.real("Saldo inicial")
        self.__act = 1
        print(f"Estado: Activo")
        self.__ncl = ncl
        print(f"Número de cliente: {ncl}")

    def títulos(self):
        obf = Formato()
        print(f"| {obf.izq('NO.', 3)} | {obf.cen('NOMBRE', 30)} | {obf.der('SUC', 3)} | {obf.izq('FEC. AP', 12)} | {obf.der('SALDO', 15)} | {obf.cen('ESTADO', 10)} | {obf.der('No.C Asociado', 20 )} |")

    def mostrar(self):
        obf = Formato()
        print(f"| {obf.izq(self.__nc, 3)} | {obf.cen(self.__nm, 30)} | {obf.der(self.__suc, 3)} | {obf.izq(self.__fa, 12)} | {obf.der(obf.mon(self.__sal), 15)} | {obf.cen('ACTIVO' if self.__act else 'INACTIVO', 10)} | {obf.der(self.__ncl, 20 )} |")

    def movimiento(self, mon, tip):
        si = self.__sal
        sal = self.__sal
        if tip:
            mon *= -1
        sal += mon
        if sal == 0:
            print('Cuenta inactiva, saldo cero')
            self.__act = 0
            self.__sal = sal
        elif sal < 0:
            self.__sal = si
            raise Exception(
                'El saldo no puede ser negativo, operación cancelada')
        else:
            self.__act = 1
            self.__sal = sal
        return self.__sal

    def modificar(self):
        obm = Menu('Menu de Cliente', [
                   'Nombre de la cuenta', 'Sucursal', 'Fecha'])
        op = 0
        while op != obm.salir():
            match op := obm.opcion():
                case 1:
                    self.__nm = self.obd.cadena("Nombre de la cuenta").upper()
                case 2:
                    self.__suc = 0
                    while self.__suc < 1 or self.__suc > 10:
                        self.__suc = self.obd.entero("Sucursal")
                case 3:
                    obfe = FechaHora()
                    self.__fa = obfe.fecha()
                    print('Fecha actualizada')

    def nc(self):
        return self.__nc

    def ncl(self):
        return self.__ncl

    def act(self):
        return self.__act
