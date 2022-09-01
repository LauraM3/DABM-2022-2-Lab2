
from dataclasses import dataclass
from tabulate import tabulate
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
    Nombre=input("Nombre del equipo: ")

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



