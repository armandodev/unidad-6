from poo.lib import Datos, FechaHora
import datetime


class Lanzadora:
    obd = Datos()

    def fecha(self):
        try:
            fec = self.obd.cadena(
                "Ingresa tu fecha de nacimiento (dd/mm/aaaa)")
            dia, mes, año = fec.split('/')
            dia, mes, año = int(dia), int(mes), int(año)
            val = [4, 6, 9, 11]
            if mes > 12 or mes < 1:
                raise Exception("El mes debe ir de 01 - 12")
            if dia < 1:
                raise Exception("El día no puede ser negativo o 0")
            if mes == 2:
                if año % 4 == 0 and dia > 29:
                    raise Exception(
                        "Febrero en año bisiesto no tiene más de 29 días")
                elif dia > 28:
                    raise Exception("Febrero solo tiene 28 días")
            if mes in val and dia > 30:
                raise Exception("El mes indicado no tiene más de 30 días")
            elif dia > 31:
                raise Exception("El mes indicado no tiene más de 31 días")
            if año < 1900:
                raise Exception("El año ingresado en inválido")
            edad = FechaHora().edad(dia, mes, año)
            if edad < 18:
                raise Exception("Debes ser mayor de edad")
            return datetime.datetime(año, mes, dia).strftime("%d/%m/%Y"), edad
        except Exception as e:
            print(e)
            return self.fecha()
        except ValueError:
            print("Formato de fecha invalido")
            return self.fecha()

    def teléfono(self):
        try:
            tel = self.obd.cadena("Ingresa un número telefónico de 10 dígitos")
            if len(tel.strip()) != 10:
                raise Exception(
                    "El número telefónico debe contener 10 dígitos")
            tel = int(tel)
            return tel
        except Exception as e:
            print(e)
            return self.teléfono()
        except ValueError:
            print("Formato de número telefónico incorrecto")
            return self.teléfono()

    def rfc(self, ap_p, ap_m, nm, fec_nac):
        dia, mes, año = fec_nac.split('/')
        return f"{ap_p[:2]}{ap_m[0]}{nm[0]}{año[2:]}{mes}{dia}XXX"

    def sexo(self):
        sexo = ['M', 'F']
        while True:
            self.__sexo = self.obd.carácter("Sexo (M/F)").upper()
            if self.__sexo in sexo:
                break
        return self.__sexo
