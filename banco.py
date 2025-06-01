from clientes import Clientes
from movimientos import Movimientos
from cuentas import Cuentas
from poo.lib import Menu, Datos


def main():
    ob_cl = Clientes()
    ob_cu = Cuentas()
    ob_mv = Movimientos()
    obm = Menu("BANCO", ["CLIENTES", "CUENTAS", "MOVIMIENTOS"])
    obm_cl = Menu("CLIENTES", ["NUEVO", "LISTA",
                  "BUSCAR", "MODIFICAR", "BORRAR", "BAJAS"])
    obm_cu = Menu("CUENTAS", ["NUEVA", "LISTA",
                  "BUSCAR", "MODIFICAR", "BAJAS"])
    obm_mv = Menu("MOVIMIENTOS", ["NUEVO", "CANCELAR"])
    op = 0
    while op != obm.salir():
        match op := obm.opcion():
            case 1:
                op_cl = 0
                while op_cl != obm_cl.salir():
                    match op_cl := obm_cl.opcion():
                        case 1:
                            ob_cl.nuevo()
                        case 2:
                            ob_cl.lista()
                        case 3:
                            ob_cl.buscar()
                        case 4:
                            ob_cl.modificar()
                        case 5:
                            ob_cl.borrar()
                        case 6:
                            ob_cl.bajas()

            case 2:
                op_cu = 0
                while op_cu != obm_cu.salir():
                    match op_cu := obm_cu.opcion():
                        case 1:
                            ncl = ob_cl.cliente_ncl()
                            if ncl != 0:
                                ob_cu.nueva(ncl)
                        case 2:
                            ob_cu.lista()
                        case 3:
                            nc = ob_cu.buscar_nc()
                            print('<<MOVIMIENTOS>>')
                            ob_mv.mostrar(nc)
                        case 4:
                            ob_cu.modificar()
                        case 5:
                            ob_cu.bajas()

            case 3:
                op_mv = 0
                while op_mv != obm_mv.salir():
                    match op_mv := obm_mv.opcion():
                        case 1:
                            nc = Datos().entero('Dame el numero de la cuenta a buscar')
                            nc = ob_cu.cuentas_nc(nc)
                            if nc <= 0:
                                print('La cuenta esta inactiva o no existe')
                            else:
                                ob_mv.nuevo(nc)
                        case 2:
                            ver, ncl = ob_mv.cancelar()
                            ob_cl.modificar_estado(ver, ncl)


if __name__ == "__main__":
    main()
