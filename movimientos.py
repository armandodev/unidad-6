from movimiento import Movimiento
from cuentas import Cuentas
from poo.lib import Datos
import pickle


class Movimientos(Cuentas):
    obd = Datos()

    def __init__(self):
        self.__am = 'movimientos.txt'
        self.__aa = 'auxiliar__mv.txt'
        super().__init__()

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
        with open(self.__am, 'ab') as oba:
            pickle.dump(obm, oba)
        tip = obm.tipo()
        monto = obm.monto()
        super().modificar_monto(nc, tip, monto)

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
        try:
            nm_c = self.obd.entero('Número de movimiento')
            with open(self.__am, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nm() == nm_c:

                            monto = obc.monto()
                            obc.inactivo()
                            nc = obc.nc()
                            tip = obc.tipo()
                            ban = False
                            if tip == 0:
                                tip = 1
                            else:
                                tip = 0
                            ver, ncl = super().modificar_monto(nc, tip, monto)
                        pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print('No se ha encontrado el movimiento...')
            if not ban:
                self.__actualizar()
                return ver, ncl
        except FileNotFoundError:
            print('No hay movimientos registrados...')
