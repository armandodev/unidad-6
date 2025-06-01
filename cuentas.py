from cuenta import Cuenta
from poo.lib import Datos
import pickle


class Cuentas:
    def __init__(self):
        self.__ac = 'cuentas.txt'
        self.__aa = 'auxiliar_cu.txt'

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

    def cuentas_nc(self, nc):
        """Verifica si una cuenta existe y está activa"""
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if obc.act():
                                return nc
                            else:
                                return -1  # Cuenta inactiva
                except EOFError:
                    return 0  # Cuenta no encontrada
        except FileNotFoundError:
            return 0

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
                        print('No hay cuentas activas...')
        except FileNotFoundError:
            print('No hay cuentas registradas...')

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
                            else:
                                print('La cuenta está inactiva')
                                return 0
                except EOFError:
                    print('No hay cuentas registradas con ese numero...')
                    return 0
        except FileNotFoundError:
            print('No hay cuentas registradas...')
            return 0

    def buscar_ncl(self, ncl):
        """Busca todas las cuentas de un cliente"""
        lista = []
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            lista.append(obc)
                except EOFError:
                    return lista
        except FileNotFoundError:
            return lista

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
            print('No hay cuentas registradas...')

    def modificar(self):
        ban = True
        try:
            nc = Datos().entero('Número de cuenta a modificar')
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.nc() == nc:
                            if obc.act():
                                ban = False
                                obc.modificar()
                        pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print('No hay cuentas registradas con ese numero...')
            if not ban:
                print('Cuenta modificada correctamente.')
                self.__actualizar()
        except FileNotFoundError:
            print('No hay cuentas registradas...')

    def modificar_monto(self, nc, tip, mon):
        """Modifica el saldo de una cuenta según el tipo de movimiento"""
        ban = True
        ver = 0
        ncl = 0
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
                        print('No se encontró la cuenta...')
            if not ban:
                self.__actualizar()
            return ver, ncl
        except FileNotFoundError:
            print('No hay cuentas registradas...')
            return 0, 0
