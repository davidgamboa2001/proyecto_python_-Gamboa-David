import gestion


def incripcion():
    inscripccion=list(gestion.cargardatos("inscripccion.json"))
    
    documento=input("ingresa tu C.C o tu T.I")
    nombre=input("Ingresa tus dos nombres")
    apellido=input("Ingresa tus dos apellidos")
    direccion=input("Ingresa tu direccion de vivienda")
    acudiente=input("Nombre de acudiente para emergencias")
    telefono=int(input("Numero telefonico del acudiente"))
    
    
    dicinscripcion={"documento":documento,"nombre":nombre,"apellido":apellido,"direccion":direccion,"acudiente":acudiente,"telefono":telefono,"estado":"inscricto", "nota":"None"}
    inscripccion.append(dicinscripcion)
    
    gestion.guardardatos(inscripccion,"inscripccion.json")
    print()
    print("\tInscripción exitosa!")
    input()
    
