from cliente import Cliente
from cuentas import Cuentas
from movimientos import Movimientos
from poo.lib import Datos
import pickle


class Clientes:
    def __init__(self):
        self.__ac = 'clientes.txt'
        self.__aa = 'auxiliar_cl.txt'

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
        obd = Cuentas()
        obm = Movimientos()
        ncl = self.__no_cliente()
        obc.nuevo(ncl)
        with open(self.__ac, 'ab') as oba:
            pickle.dump(obc, oba)
        nc = obd.nueva(ncl)
        self.actualizar_contador_cuentas(ncl, 1)
        obm.nuevo(nc)

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

    def cliente_ncl(self):
        try:
            ncl = Datos().entero('Número de cliente')
            with open(self.__ac, 'rb') as oba:
                try:
                    while True:
                        obc = pickle.load(oba)
                        nc = obc.ncl()
                        if nc == ncl:
                            if obc.act():
                                return nc
                            else:
                                print('Cliente inactivo')
                                return 0
                except EOFError:
                    print('No hay clientes registrados con ese numero...')
                    return 0
        except FileNotFoundError:
            print('No hay clientes registrados...')
            return 0

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
                                lista = obc.buscar_ncl(ncl)
                                if lista:
                                    for i in lista:
                                        print("<<CUENTAS>>")
                                        i.títulos()
                                        i.mostrar()
                                        print("<<MOVIMIENTOS>>")
                                        obm.mostrar(i.nc())
                                ban = False
                except EOFError:
                    if ban:
                        print('No se ha encontrado el cliente.')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def modificar(self):
        ban = True
        try:
            ncl = Datos().entero('Número de cliente a modificar')
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if obc.act():
                                ban = False
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
        cuentas = Cuentas()
        try:
            ncl_b = Datos().entero('Número de cliente a eliminar')
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obd = pickle.load(oba)
                        ncl = obd.ncl()
                        if obd.act() and ncl == ncl_b:
                            lista = cuentas.buscar_ncl(ncl)
                            cuentas_activas = False
                            if lista:
                                for cuenta in lista:
                                    if cuenta.act():
                                        cuentas_activas = True
                                        break

                            if not cuentas_activas:
                                obd.inactivo()
                                print(f"Se ha eliminado el cliente correctamente")
                            else:
                                print(
                                    f"No se puede eliminar el cliente {ncl} porque tiene cuentas activas.")
                            ban = False
                        pickle.dump(obd, obx)
                except EOFError:
                    pass
            if not ban:
                self.__actualizar()
            elif ban:
                print('No se ha encontrado el cliente o ya está inactivo.')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def modificar_estado(self, ver, ncl):
        try:
            ban = True
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if ver:
                                ban = False
                                obc.activo()
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
                        print('No hay clientes inactivos...')
        except FileNotFoundError:
            print('No hay clientes registrados...')

    def actualizar_contador_cuentas(self, ncl, incremento):
        try:
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl:
                            if incremento == -999:
                                while obc.cantidad_cuentas() > 0:
                                    obc.decrementar_cuentas()
                            elif incremento > 0:
                                obc.incrementar_cuentas()
                            else:
                                obc.decrementar_cuentas()
                        pickle.dump(obc, obx)
                except EOFError:
                    pass
            self.__actualizar()
        except FileNotFoundError:
            pass

    def eliminar_cliente_directo(self, ncl):
        ban = True
        try:
            with open(self.__ac, 'rb') as oba, open(self.__aa, 'wb') as obx:
                try:
                    while True:
                        obc = pickle.load(oba)
                        if obc.ncl() == ncl and obc.act():
                            obc.inactivo()
                            while obc.cantidad_cuentas() > 0:
                                obc.decrementar_cuentas()
                            ban = False
                            print(
                                f"Cliente {ncl} eliminado automáticamente (sin cuentas activas)")
                        pickle.dump(obc, obx)
                except EOFError:
                    pass
            if not ban:
                self.__actualizar()
        except FileNotFoundError:
            pass
