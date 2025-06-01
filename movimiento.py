from poo.lib import FechaHora, Datos, Formato


class Movimiento:
    obd = Datos()

    def nuevo(self, nm, nc):
        print(f"\n<<DATOS DEL MOVIMIENTO>>")
        self.__nm = nm
        print(f"Numero de deposito: {nm}")
        self.__fec = FechaHora().fecha()
        self.__tip = -1
        while self.__tip < 0 or self.__tip > 1:
            self.__tip = self.obd.entero(
                "Tipo de movimiento\n1) Deposito\n2) Retiro\nSelecciona una opción") - 1
        self.__mon = 0
        while self.__mon <= 0:
            self.__mon = self.obd.real("Monto")
        self.__act = 1
        print("Estado: Activo")
        self.__nc = nc
        print(f"No. cuentas: {nc}")

    def títulos(self):
        obf = Formato()
        print(f"| {obf.izq('No.', 5)} | {obf.cen('Fecha', 15)} | {obf.der('Tip', 10)} | {obf.izq('Monto', 15)} | {obf.der('Estado', 10)} | {obf.cen('No. cuenta', 15)} |")

    def mostrar(self):
        obf = Formato()
        print(f"| {obf.izq(self.__nm, 5)} | {obf.cen(self.__fec, 15)} | {obf.der('Deposito' if not self.__tip else 'Retiro', 10)} | {obf.izq(self.__mon, 15)} | {obf.der('Estado' if self.__act == 1 else 'Inactivo', 10)} | {obf.cen(self.__nc, 15)} |")

    def nc(self):
        return self.__nc

    def nm(self):
        return self.__nm

    def act(self):
        return self.__act

    def tipo(self):
        return self.__tip

    def monto(self):
        return self.__mon

    def inactivo(self):
        self.__act = 0
