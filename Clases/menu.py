class Menu:
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio

    def ver(self):
        print("BIENVENIDO AL SISTEMA".center(50,"*"))
        print("Laboratorio " +self.laboratorio )
        print("1. Tecnicos")
        print("2. Estudiantes")
        op=input(">>>")

        return op


class MenuTecnicos:
    def ver(self):
        print("MENU TECNICOS DE LABORATORIO".center(20,"*"))
        print("1. Registrar equipos")
        print("2. Registrar prestamo")
        print("3. Registrar mantenimiento")
        print("4. Registrar Entrega")
        print("5. Regresar al menú anterior")
        op=input(">>>")

        return op

class MenuEstudiantes:
    def ver(self):
        print("MENU ESTUDIANTES".center(20,"*"))
        print("1. Ver prestamos")
        print("2. Consultar equipo")
        print("3. Regresar al menú principal")
        op=input(">>>")

        return op

class MenuRegreso:
    def ver(self):
        print("Desea volver al menú anterior?")
        print("1. Sí")
        print("2. No")
        op=input(">>>")

        return op


if __name__=='__main__':
     m= Menu("xxx")
     m.ver()
