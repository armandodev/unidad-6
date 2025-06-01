from movimientos import Movimientos
from cuenta import Cuenta
from poo.lib import Datos
import pickle


class Cuentas(Movimientos):
    obd = Datos()

    def __init__(self):
        super().__init__()
        self.__ac = 'cuentas.txt'
        self.__aa = 'auxiliar.txt'

    def __no_cuenta(self):
        nc = 1
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        nc = pickle.load(oba).nc() + 1
                except EOFError:
                    return nc
        except FileNotFoundError:
            return nc

    def __actualizar(self):
        with open(self.__ac, 'wb') as oba, open(super().__aa, 'rb') as obx:
            try:
                while True:
                    obc = pickle.load(obx)
                    pickle.dump(obc, oba)
            except EOFError:
                pass

    def nueva_cuenta(self, ncl):
        obc = Cuenta()
        nc = self.__no_cuenta()
        obc.nueva(nc, ncl)
        with open(self.__ac, 'ab') as oba:
            pickle.dump(obc, oba)

    def nuevo_movimiento(self, nc=None):
        if not nc:
            nc = self.obd.entero('Ingresa el numero de la cuenta')
        ban = True
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            ban = False
                            break
                except EOFError:
                    pass
        except FileNotFoundError:
            pass
        if ban:
            print("No existe la cuenta indicada...")
            return None
        tip, mon = super().nuevo(nc)
        try:
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            try:
                                sal = obc.movimiento(mon, tip)
                            except Exception as e:
                                print(e)
                                return None
                        pickle.dump(obc, obx)
                except EOFError:
                    pass
            if sal == 0:
                ban = True
                with open(self.__ac, 'rb') as oba:
                    try:
                        while True:
                            obc = pickle.load(oba)
                            if obc.nc() == nc and obc.act():
                                ban = False
                    except EOFError:
                        pass
            self.__actualizar()
            if ban:
                return True
            else:
                return False
        except FileNotFoundError:
            print('No hay cuentas registrados...')

    def lista(self):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.act():
                            if ban:
                                obc.títulos()
                                ban = False
                            obc.mostrar()
                except EOFError:
                    if ban:
                        print('No hay clientes registrados...')
                    else:
                        print('Fin del archivo...')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def buscar(self):
        ban = True
        try:
            nc = Datos().entero('Dame el numero de la cuenta a buscar')
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if obc.act():
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

    def buscar_ncl(self, ncl):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if obc.act():
                                if ban:
                                    obc.títulos()
                                    ban = False
                                obc.mostrar()
                except EOFError:
                    if ban:
                        print('No hay cuentas para el cliente indicado...')
            return obc.nc()
        except FileNotFoundError:
            print('No hay cuentas registrados...')

    def bajas(self):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if not obc.act():
                            if ban:
                                obc.títulos()
                                ban = False
                            obc.mostrar()
                except EOFError:
                    if ban:
                        print('No hay clientes registrados...')
                    else:
                        print('Fin del archivo...')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def modificar(self):
        ban = True
        try:
            ncl = Datos().entero('Dame el numero de la cuenta a Modificar')
            with open(self.__ac, 'rb') as oba, open(super().__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == ncl:
                            if obc.act():
                                obc.títulos()
                                ban = False
                                obc.mostrar()
                                obc.modificar()
                        pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print('No hay clientes registrados...')
                    else:
                        print('Fin del archivo...')
            if not ban:
                self.__actualizar()
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def modificar_monto(self, nc, tip, mon):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba, open(super().__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:

                            obc.saldo(mon, tip)
                            ban = False
                        pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print('No hay movimientos registrados...')
                    else:
                        print('Fin del archivo...')
            if not ban:
                self.__actualizar()
        except FileNotFoundError:
            print('No hay clientes registrados...')
