from poo.lib import Datos, Formato, Menu
from lanzadora import Lanzadora


class Cliente:
    obd = Datos()

    def nuevo(self, ncl):
        obl = Lanzadora()

        print("\n<<DATOS DEL CLIENTE>>")
        print(f"No. de cliente: {ncl}")
        self.__ncl = ncl
        self.__ap = self.obd.cadena("Apellido paterno").upper().strip()
        self.__am = self.obd.cadena("Apellido materno").upper().strip()
        self.__nm = self.obd.cadena("Nombre(s)").upper().strip()
        self.__fec_n, self.__edad = obl.fecha()
        self.__dir = self.obd.cadena("Dirección").upper().strip()
        self.__tel = obl.teléfono()
        print(f"Edad: {self.__edad}")
        self.__sex = obl.sexo()
        self.__rfc = obl.rfc(self.__ap, self.__am, self.__nm, self.__fec_n)
        print(f"RFC: {self.__rfc}")
        self.__cc = 0
        print("Cantidad de cuentas: 0")
        self.__act = 1
        print("Estado: Activo")
        return ncl

    def títulos(self):
        obf = Formato()
        print(f"| {obf.izq('NO.', 3)} | {obf.izq('AP. PAT', 10)} | {obf.izq('AP. MAT', 10)} | {obf.izq('NOMBRE(s)', 20)} | {obf.cen('FEC. NAC.', 12)} | {obf.izq('DIRECCIÓN', 30)} | {obf.der('TELÉFONO', 10)} | {obf.der('SEXO', 4)} | {obf.der('EDAD', 3)} | {obf.cen('RFC', 13)} | {obf.der('CUENTAS', 7)} | {obf.cen('ESTADO', 10)} |")

    def mostrar(self):
        obf = Formato()
        print(f"| {obf.izq(self.__ncl, 3)} | {obf.izq(self.__ap, 10)} | {obf.izq(self.__am, 10)} | {obf.izq(self.__nm, 20)} | {obf.cen(self.__fec_n, 12)} | {obf.izq(self.__dir, 30)} | {obf.der(self.__tel, 10)} | {obf.der(self.__sex, 4)} | {obf.der(self.__edad, 3)} | {obf.cen(self.__rfc, 13)} | {obf.der(self.__cc, 7)} | {obf.cen('ACTIVO' if self.__act else 'INACTIVO', 10)} |")

    def modificar(self):
        obl = Lanzadora()
        print("\n<<MODIFICAR DATOS DEL CLIENTE>>")
        print("<<DATOS ACTUALES>>")
        self.títulos()
        self.mostrar()
        obm = Menu(f"CLIENTE {self.__ncl}", [
                   "NOMBRE(s)/APELLIDOS", 'DIRECCIÓN', 'TELÉFONO', 'SEXO'])
        op = 0
        while op != obm.salir():
            match op := obm.opcion():
                case 1:
                    self.__ap = self.obd.cadena(
                        "Apellido paterno").upper().strip()
                    self.__am = self.obd.cadena(
                        "Apellido materno").upper().strip()
                    self.__nm = self.obd.cadena("Nombre(s)").upper().strip()
                    self.__rfc = obl.rfc(
                        self.__ap, self.__am, self.__nm, self.__fec_n)
                case 2:
                    self.__dir = self.obd.cadena("Dirección").upper().strip()
                case 3:
                    self.__tel = obl.teléfono()
                case 4:
                    self.__sex = obl.sexo()

    def act(self):
        return self.__act

    def ncl(self):
        return self.__ncl

    def inactivo(self):
        self.__act = 0

    def activo(self):
        self.__act = 1

    def incrementar_cuentas(self):
        self.__cc += 1

    def decrementar_cuentas(self):
        if self.__cc > 0:
            self.__cc -= 1

    def cantidad_cuentas(self):
        return self.__cc
