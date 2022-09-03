from tabulate import tabulate

class Prestamo:

    file = "C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 2/Database/prestamos.csv"

    def __init__(self,Nombre_E,Carnet,Equipo,F_Prestamo,F_Entrega):
        self.Nombre_E = Nombre_E
        self.Carnet =  Carnet
        self.Equipo = Equipo
        self.F_Prestamo = F_Prestamo
        self.F_Entrega = F_Entrega
        

    def save(self):
        file=open(self.file,'a')
        prestamo=";".join([self.Nombre_E, self.Carnet, self.Equipo, self.F_Prestamo, self.F_Entrega])
        file.write(prestamo +"\n")
        file.close()



def CPrestamo():
    print("Registrar el prestamo de un equipo")
    Nombre_E = input("Nombre de la persona: ")
    Carnet = input("Carnet: ")
    Equipo = input("Equipo: ")
    F_Prestamo = input("Fecha del prestamo (AA-MM-DD): ")
    F_Entrega = input("Fecha de la entrega (AA-MM-DD): ")


    p = Prestamo(Nombre_E,Carnet,Equipo,F_Prestamo,F_Entrega)


    return p

def registroEntrega():
    listaPrestamos = getAllPrestamos()
    n_carnet = input("Numero de Carnet: ")
    equipo_p = input("Equipo que regresa: ")


    pos= 0
    for p in listaPrestamos:
        if n_carnet in p:
            if equipo_p in p:
                datosEquipo = p.split(";")
                datosEquipo.clear()
                listaPrestamos[pos] = ";".join(datosEquipo)

        pos +=1

    saveAllPrestamos(listaPrestamos)

def saveAllPrestamos(equipos):
    ar = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 2/Database/prestamos.csv", "w")
    for p in equipos:
        ar.write(p)
    ar.close()


def getAllPrestamos():
    ar = open("C:/Users/lala_/OneDrive/Documentos/Octavo Semestre/DABM/Lab 2/Database/prestamos.csv", "r")
    datos = ar.readlines()
    return datos

def ConsultarPrestamos():
    consulta= getAllPrestamos()
    nombre = input("Nombre: ")
    carnet = input("Numero de Carnet: ")

    info=[]
    encabezado=["Equipo","Fecha de Prestamo","Fecha de Entrega"]
    for p in consulta:
        if nombre in p:
            if carnet in p:
                p= p[:-2]
                datosPrestamo = p.split(";")
                info.append(datosPrestamo[2:])
    print(tabulate(info,encabezado,tablefmt="grid"))
             
    
