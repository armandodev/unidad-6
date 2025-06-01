from cliente import Cliente
from cuentas import Cuentas
from poo.lib import Datos
import pickle


class Clientes(Cuentas):
    def __init__(self):
        super().__init__()
        self.__ac = 'clientes.txt'
        self.__aa = 'auxiliar.txt'

    def __no_cliente(self):
        ncl = 1
        try:
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        ncl = pickle.load(oba).ncl() + 1
                except EOFError:
                    return ncl
        except FileNotFoundError:
            return ncl

    def __actualizar(self):
        with open(self.__ac, 'wb') as oba, open(self.__aa, 'rb') as obx:
            try:
                while True:
                    obc = pickle.load(obx)
                    pickle.dump(obc, oba)
            except EOFError:
                pass

    def nuevo(self):
        obc = Cliente()
        ncl = self.__no_cliente()
        obc.nuevo(ncl)
        super().nueva_cuenta(ncl)
        obc.nuevo_cuenta()
        ina = super().nuevo_movimiento()
        obc.movimiento(ina)
        with open(self.__ac, 'ab') as oba:
            pickle.dump(obc, oba)

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
                        print('No hay clientes activos...')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def buscar(self):
        ban = True
        obc = Cuentas()
        obm = Movimientos()
        try:
            ncl = Datos().entero('Número de cliente a buscar')
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obd = pickle.load(oba)
                        if obd.ncl() == ncl:
                            if obd.act():
                                print("<<CLIENTE>>")
                                obd.títulos()
                                obd.mostrar()
                                print("<<CUENTAS>>")
                                nc = obc.buscar_ncl(ncl)
                                print("<<MOVIMIENTOS>>")
                                obm.mostrar(nc)
                                ban = False
                except EOFError:
                    if ban:
                        print('No se ha encontrado el cliente.')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def modificar(self):
        ban = True
        try:
            ncl = Datos().entero('Dame el numero de cliente a modificar')
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if obc.act():
                                obc.títulos()
                                ban = False
                                obc.mostrar()
                                obc.modificar()
                            pickle.dump(obc, obx)
                except EOFError:
                    if ban:
                        print('No se ha encontrado el cliente.')
            if not ban:
                print('Cliente modificado correctamente.')
                self.__actualizar()
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def borrar(self):
        ban = True
        try:
            ncl = Datos().entero('Dame el numero de cliente a eliminar')
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if obc.act():
                                obc.títulos()
                                obc.mostrar()
                                obc.act_des()
                                ban = False
                        pickle.dump(obc, obx)
                except EOFError:
                    pass
            if not ban:
                self.__actualizar()
        except FileNotFoundError:
            print('No hay clientes registrados...')

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
                        print('No hay clientes activos...')
        except FileNotFoundError:
            print('No hay clientes registrados...')
