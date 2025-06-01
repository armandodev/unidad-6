import datetime
import locale


class Datos:
    def entero(self, msj="Ingresa un número entero"):
        while True:
            try:
                return int(input(f"{msj}: "))
            except ValueError:
                print("Error: Debe ingresar un número")

    def real(self, msj="Ingresa un número decimal"):
        while True:
            try:
                return float(input(f"{msj}: "))
            except ValueError:
                print("Error: Debe ingresar un número real")

    def carácter(self, msj="Ingresa un carácter"):
        while True:
            try:
                return input(f"{msj}: ")[0]
            except IndexError:
                print("Error: Debe ingresar un carácter")

    def cadena(self, msj="Ingresa una cadena de texto", emp=False):
        while True:
            try:
                cad = input(f"{msj}: ")
                if not len(cad) and not emp:
                    raise ValueError
                return cad
            except ValueError:
                print("Error: Debe ingresar una cadena de texto")

    def pausa(self, msj="Oprime enter para continuar..."):
        input(msj)


class FechaHora:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
        self.__obf = datetime.datetime.now()

    def fecha_l(self):
        print(self.__obf.strftime("%A, %d de %B del %Y").capitalize())

    def fecha(self):
        return self.__obf.strftime("%d/%m/%Y")

    def hora(self):
        print(self.__obf.strftime("%H:%M:%S"))

    def edad(self, dia=1, mes=1, año=1900):
        obf = datetime.datetime(año, mes, dia)
        edad = self.__obf.year - obf.year
        if obf.month > self.__obf.month or (obf.month == self.__obf.month and obf.day > self.__obf.day):
            edad -= 1
        return edad


class Formato:
    def izq(self, msj, tc):
        return str(msj)[:tc].ljust(tc)

    def der(self, msj, tc):
        return str(msj)[:tc].rjust(tc)

    def cen(self, msj, tc):
        return str(msj)[:tc].center(tc)

    def mon(self, can):
        return f"$ {can:,.2f}"


class Menu:
    obd = Datos()

    def __init__(self, titulo='Menú Principal', opciones=None):
        self.__tit = titulo.upper()
        self.__op = ["" for _ in range(len(opciones) + 1)]

        for i in range(len(opciones)):
            self.__op[i] = f"{i + 1}.- {opciones[i].upper()}"

        self.__op[len(opciones)] = f"{len(opciones) + 1}.- SALIR"

    def __mostrar(self):
        print(f"<<{self.__tit}>>")
        for opcion in self.__op:
            print(opcion)

    def opcion(self):
        op = 0
        while op < 1 or op > len(self.__op):
            self.__mostrar()
            op = self.obd.entero("Selecciona una opción")
        return op

    def salir(self):
        return len(self.__op)
