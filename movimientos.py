from movimiento import Movimiento
from poo.lib import Datos
import pickle


class Movimientos:
    def __init__(self):
        self.__am = 'movimientos.txt'
        self.__aa = 'auxiliar.txt'

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
        return obm.tipo(), obm.monto()

    def mostrar(self, nc):
        ban = True
        try:
            with open(self.__am, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if ban:
                                obc.títulos()
                                ban = False
                            obc.mostrar()
                except EOFError:
                    if ban:
                        print('No hay cuentas registrados...')
                    else:
                        print('Fin del archivo...')
        except FileNotFoundError:
            print('No hay cuentas registrados...')

    def cancelar(self):
        ban = True
        try:
            ncm = Datos().entero('Dame el numero del movimiento a cancelar')
            with open(self.__am, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obm = pickle.load(oba)
                        if obm.nm() == ncm:
                            nc = obm.nc()
                            mon = obm.monto()
                            ban = False
                            obm.inactivo()
                        pickle.dump(obm, obx)
                except EOFError:
                    if ban:
                        print('No se encontró el movimiento, busca de nuevo...')
            if not ban:
                self.__actualizar()
                return nc, mon
            else:
                return self.cancelar()
        except FileNotFoundError:
            print('No hay cuentas registrados...')
