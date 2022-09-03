from Clases.menu import *
from Clases.equipo import *
from Clases.prestamo import *

def main():
    menu = Menu("Escuela de Ingenieria")
    op=menu.ver()
    if op =="1":
        menu2=MenuTecnicos()
        op2=menu2.ver()
        if op2 =="1":
            e=CEquipo()
            e.verDatos()
            e.save()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass

        elif op2 =="2":
            p=CPrestamo()
            p.save()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass
        
        elif op2 =="3":
            registroMantenimiento()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass

        elif op2 =="4":
            registroEntrega()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass

        elif op2 =="5":
            main()
        
        else:
            print("Opción inválida")
            main()

    elif op =="2":
        menu2=MenuEstudiantes()
        op2=menu2.ver()
        if op2 =="1":
            ConsultarPrestamos()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass
        elif op2 =="2":
            consultarEquipo()
            menu3 = MenuRegreso()
            op3=menu3.ver()
            if op3 =="1":
                main()
            elif op3=="2":
                pass
        
        elif op2 =="3":
            main()
        
        else:
            print("Opción inválida")
            main()
    

if __name__=='__main__':
    main()
