from cuenta import Cuenta
from poo.lib import Datos
import pickle


class Cuentas:
    def __init__(self):
        self.__ac = 'cuentas.txt'
        self.__aa = 'auxiliar__cu.txt'
        self.__acl = 'clientes.txt'

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
        with open(self.__ac, 'wb') as oba, open(self.__aa, 'rb') as obx:
            try:
                while True:
                    obc = pickle.load(obx)
                    pickle.dump(obc, oba)
            except EOFError:
                pass

    def nueva(self, ncl):
        obc = Cuenta()
        nc = self.__no_cuenta()
        obc.nueva(nc, ncl)
        with open(self.__ac, 'ab') as oba:
            pickle.dump(obc, oba)
        return nc

    def cuenta_nc(self, nc):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if obc.act():
                                ban = False
                                return nc
                            else:
                                return 0
                except EOFError:
                    if ban:
                        print('No hay cuenta con ese numero...')
                        return 0
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

    def buscar_nc(self):
        try:
            nc = Datos().entero('Dame el numero de la cuenta a buscar')
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if obc.act():
                                print('<<CUENTA>>')
                                obc.títulos()
                                obc.mostrar()
                                return nc
                except EOFError:
                    print('No hay cuentas registrados con ese numero...')
        except FileNotFoundError:
            print('No hay cuentas registrados...')

    def buscar_ncl(self, ncl):
        ban = True
        lista = []
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if obc.act():
                                lista.append(obc)
                                ban = False
                except EOFError:
                    if ban:
                        return 0
                return lista
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
                        print('No hay cuentas inactivas...')
        except FileNotFoundError:
            print('No hay cuentas registrados...')

    def modificar(self):
        ban = True
        try:
            ncl = Datos().entero('Número de cuenta a modificar')
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
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
                        print(
                            'No hay clientes registrados con ese numero...')
            if not ban:
                self.__actualizar()
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def modificar_monto(self, nc, tip, mon):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            ver, ncl = obc.saldo(mon, tip)
                            ban = False
                        pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print('No hay movimientos registrados...')
            if not ban:
                self.__actualizar()
                return ver, ncl
        except FileNotFoundError:
            print('No hay clientes registrados...')
