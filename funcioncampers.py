import gestion


def incripcion():
    inscripccion=list(gestion.cargardatos("inscripccion.json"))
    
    documento=input("ingresa tu C.C o tu T.I")
    nombre=input("Ingresa tus dos nombres")
    apellido=input("Ingresa tus dos apellidos")
    direccion=input("Ingresa tu direccion de vivienda")
    acudiente=input("Nombre de acudiente para emergencias")
    telefono=int(input("Numero telefonico del acudiente"))
    
    
    dicinscripcion={"documento":documento,"nombre":nombre,"apellido":apellido,"direccion":direccion,"acudiente":acudiente,"telefono":telefono,"estado":"inscricto","ruta":"", "nota":"None"}
    inscripccion.append(dicinscripcion)
    
    gestion.guardardatos(inscripccion,"inscripccion.json")
    print()
    print("\tInscripción exitosa!")
    input()

def mostrarcampersmatriculados():
    
    aprobados=list(gestion.cargardatos("campersmatriculados.json"))
    print("\tCampers matriculados")
    for i in aprobados:
       documento=i["documento"]
       nombre = i["nombre"]
       print(f"{documento} : {nombre}")
       
        
     
def agregaruta():
    ruta=list(gestion.cargardatos("rutas.json"))

    nombre=input("ingrese el nombre del camper: ")
    rutas=input("que ruta le asignara: ")
    horario=input("si el horario lo quiere en mañana de 6:15 am a 10 pm dijite mañana: si desea el horario en la tarde dijite tarde: ")
    salon=input("adecuacion de salon: ")

    diccionariorutas={"nombre":nombre,"ruta":rutas,"horario":horario,"salon":salon}
    ruta.append(diccionariorutas)

    gestion.guardardatos(ruta,"rutas.json")     
    input()


def controlcampers():
    control=list(gestion.cargardatos("rutas.json"))   
    print()
    print("\tcontrol de campers")
    name=input("ingrese el documento para poder revisar el control del camper: ")
                            
    
    if name==name:
        for name in control:
        
         print(control)
   

  
           
        
      
      