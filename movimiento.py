from poo.lib import FechaHora, Datos, Formato


class Movimiento:
    obd = Datos()

    def nuevo(self, nm, nc):
        print(f"\n<<DATOS DEL MOVIMIENTO>>")
        self.__nm = nm
        print(f"Numero de movimiento {nm}")
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
        print(f"No. cuenta: {nc}")

    def títulos(self):
        obf = Formato()
        print(f"| {obf.izq('NO.', 5)} | {obf.cen('FECHA', 10)} | {obf.der('TIPO', 10)} | {obf.izq('MONTO', 10)} | {obf.der('ESTADO', 10)} |")

    def mostrar(self):
        obf = Formato()
        print(f"| {obf.izq(self.__nm, 5)} | {obf.cen(self.__fec, 10)} | {obf.der('DEPOSITO' if not self.__tip else 'RETIRO', 10)} | {obf.izq(obf.mon(self.__mon), 10)} | {obf.der('ACTIVO' if self.__act else 'CANCELADO', 10)} |")

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
