from poo.lib import FechaHora, Datos, Formato, Menu


class Cuenta:
    obd = Datos()

    def nueva(self, nc, ncl):
        print(f"<<DATOS DE LA CUENTA>>")
        self.__nc = nc
        print(f"No. cuenta: {nc}")
        self.__nm = self.obd.cadena("Nombre de la cuenta").upper().strip()
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
        print(f"| {obf.izq('NO.', 3)} | {obf.cen('NOMBRE', 30)} | {obf.der('SUC', 3)} | {obf.izq('FEC. AP.', 12)} | {obf.der('SALDO', 15)} | {obf.cen('ESTADO', 10)}")

    def mostrar(self):
        obf = Formato()
        print(f"| {obf.izq(self.__nc, 3)} | {obf.cen(self.__nm, 30)} | {obf.der(self.__suc, 3)} | {obf.izq(self.__fa, 12)} | {obf.der(self.__sal, 15)} | {obf.cen('ACTIVO' if self.__act else 'INACTIVO', 10)}")

    def saldo(self, mon, tip):
        sal = self.__sal
        if tip:
            mon *= -1
        sal += mon
        if sal == 0:
            self.__act = 0
            self.__sal = sal
            return 0, 0
        elif sal < 0:
            print('No se realizo la operación')
            self.__sal = 0
            return 0, 0
        else:
            self.__act = 1
            self.__sal = sal
            return 1, self.__ncl

    def modificar(self):
        print("\n<<MODIFICAR DATOS DE LA CUENTA>>")
        print("<<DATOS ACTUALES>>")
        self.títulos()
        self.mostrar()
        obm = Menu(f"CUENTA {self.__ncl}", [
                   "NOMBRE", 'SUCURSAL', 'FECHA DE APERTURA'])
        op = 0
        while op != obm.salir():
            match op := obm.opcion():
                case 1:
                    self.__nm = self.obd.cadena(
                        "Nombre de la cuenta").upper().strip()
                case 2:
                    self.__suc = 0
                    while self.__suc < 1 or self.__suc > 10:
                        self.__suc = self.obd.entero("Sucursal")
                case 3:
                    obf = FechaHora()
                    self.__fa = obf.fecha()
                    print('Fecha actualizada')

    def nc(self):
        return self.__nc

    def ncl(self):
        return self.__ncl

    def act(self):
        return self.__act
