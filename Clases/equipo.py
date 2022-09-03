from tabulate import tabulate
from .prestamo import *

global datos
datos=[]

class Equipo:

    file = "C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 2/Database/equipos.csv"

    def __init__(self,Nombre,Referencia,Proveedor,CMantenimiento,Cantidad,UFecha):
        self.Nombre = Nombre
        self.Referencia = Referencia
        self.Proveedor = Proveedor
        self.CMantenimiento = CMantenimiento
        self.Cantidad = Cantidad
        self.UFecha = UFecha

    def verDatos(self):
        header =["NOMBRE", "REFERENCIA", "PROVEEDOR", "CMANTENIMIENTO", "CANTIDAD","UFECHA"]
        datos=[[self.Nombre, self.Referencia, self.Proveedor, self.CMantenimiento, self.Cantidad,self.UFecha]]
        print(tabulate(datos,header, tablefmt="grid"))


    def save(self):
        file=open(self.file,'a')
        equipo=";".join([self.Nombre, self.Referencia, self.Proveedor, self.CMantenimiento, self.Cantidad,self.UFecha])
        file.write(equipo +"\n")
        file.close()



def CEquipo():
    print("Registrar un nuevo equipo")
    Nombre = input("Nombre del equipo: ")
    Referencia = input("Referencia del equipo: ")
    Proveedor = input("Proveedor: ")
    CMantenimiento = input("Ciclo del mantenimiento (días): ")
    Cantidad = input("Cantidad de equipos: ")
    UFecha = input("Fecha del último mantenimiento (AA-MM-DD): ")


    e = Equipo(Nombre,Referencia,Proveedor,CMantenimiento,Cantidad,UFecha)
    return e

def consultarEquipo():
    print("Consulta de equipos")
    Encabezado_disp =["Equipo","Cantidades disponibles"]
    consulta= getAllEquipos()
    Nombre_Eq=input("Nombre del equipo: ")

    for e in consulta:
        if Nombre_Eq in e:
            numeroEquipos = e.split(";")
            n_equipos = int(numeroEquipos[4])

    consulta_2= getAllPrestamos()

    Numero=[]
    for p in consulta_2:
        if Nombre_Eq in p:
            Numero.append(1)
 
    total=sum(Numero)

    disponibles=n_equipos-total
    disponibles=str(disponibles)

    data=[[Nombre_Eq,disponibles]]
    print(tabulate(data,Encabezado_disp,tablefmt="grid"))
            


def registroMantenimiento():
    listaEquipos = getAllEquipos()
    equipo = input("Nombre del equipo: ")
    UFecha = input("Fecha del último mantenimiento (AA-MM-DD): ")

    pos= 0
    for e in listaEquipos:
        if equipo in e:
            datosEquipo = e.split(";")
            datosEquipo[5]= UFecha + "\n"
            listaEquipos[pos] = ";".join(datosEquipo)

        pos +=1

    saveAllEquipos(listaEquipos)

def saveAllEquipos(equipos):
    a = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 2/Database/equipos.csv", "w")
    for e in equipos:
        a.write(e)
    a.close()


def getAllEquipos():
    a = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 2/Database/equipos.csv", "r")
    datos = a.readlines()
    return datos



