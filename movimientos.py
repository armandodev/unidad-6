from movimiento import Movimiento
from cuentas import Cuentas
from poo.lib import Datos
import pickle


class Movimientos:
    obd = Datos()

    def __init__(self):
        self.__am = 'movimientos.txt'
        self.__aa = 'auxiliar_mv.txt'
        self.__cuentas = Cuentas()

    def __actualizar(self):
        with open(self.__am, 'wb') as oba, open(self.__aa, 'rb') as obx:
            try:
                while True:
                    obc = pickle.load(obx)
                    pickle.dump(obc, oba)
            except EOFError:
                pass

    def __no_movimiento(self):
        nm = 1
        try:
            with open(self.__am, 'rb') as oba:
                try:
                    while True:
                        nm = pickle.load(oba).nm() + 1
                except EOFError:
                    return nm
        except FileNotFoundError:
            return nm

    def nuevo(self, nc):
        obm = Movimiento()
        obm.nuevo(self.__no_movimiento(), nc)

        # Validar que el movimiento sea válido antes de guardarlo
        tip = obm.tipo()
        monto = obm.monto()

        # Verificar el saldo antes de realizar el movimiento
        ver, _ = self.__cuentas.modificar_monto(nc, tip, monto)

        if ver:
            # Solo guardar el movimiento si fue exitoso
            with open(self.__am, 'ab') as oba:
                pickle.dump(obm, oba)
            print("Movimiento realizado exitosamente")
        else:
            print("Movimiento cancelado: saldo insuficiente")

    def mostrar(self, nc):
        ban = True
        try:
            with open(self.__am, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if ban:
                                obc.titulos()
                                ban = False
                            obc.mostrar()
                except EOFError:
                    if ban:
                        print('No hay movimientos registrados a esa cuenta...')
        except FileNotFoundError:
            print('No hay movimientos registrados...')

    def cancelar(self):
        ban = True
        ver = 0
        ncl = 0
        try:
            nm_c = self.obd.entero('Número de movimiento a cancelar')
            with open(self.__am, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nm() == nm_c and obc.act():
                            # Obtener datos del movimiento
                            monto = obc.monto()
                            nc = obc.nc()
                            tip = obc.tipo()

                            # Invertir el tipo de movimiento
                            if tip == 0:  # Si fue depósito, hacer retiro
                                tip = 1
                            else:  # Si fue retiro, hacer depósito
                                tip = 0

                            # Intentar revertir el movimiento
                            ver, ncl = self.__cuentas.modificar_monto(
                                nc, tip, monto)

                            if ver:
                                obc.inactivo()
                                ban = False
                                print("Movimiento cancelado exitosamente")
                            else:
                                print(
                                    "No se puede cancelar el movimiento: saldo insuficiente")

                        pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print(
                            'No se ha encontrado el movimiento o ya está cancelado...')

            if not ban:
                self.__actualizar()

            return ver, ncl
        except FileNotFoundError:
            print('No hay movimientos registrados...')
            return 0, 0
