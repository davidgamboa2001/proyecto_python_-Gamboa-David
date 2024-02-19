import gestion
import json
import menus
def incripcion():
    inscripccion=list(gestion.cargardatos("inscripccion.json"))
    
    documento=input("ingresa tu C.C o tu T.I: ")

    for usuario in inscripccion:
        if usuario["documento"] == documento:
            print()

            print("\teste usuario ya ah sido registrado ")
            return
        
    nombre=input("Ingresa tus dos nombres: ")
    apellido=input("Ingresa tus dos apellidos: ")
    direccion=input("Ingresa tu direccion de vivienda: ")
    acudiente=input("Nombre de acudiente para emergencias: ")
    telefono=int(input("Numero telefonico del acudiente: "))
    
    
    dicinscripcion={"documento":documento,"nombre":nombre,"apellido":apellido,"direccion":direccion,"acudiente":acudiente,"telefono":telefono,"estado":"None","ruta":"None", "nota":"None"}
    inscripccion.append(dicinscripcion)
    
    gestion.guardardatos(inscripccion,"inscripccion.json")
    print()
    print("\tInscripción exitosa!")
    input()

def mostrarcampersmatriculados():
    
    aprobados=list(gestion.cargardatos("campersmatriculados.json"))
    print()
    print("**************************************************************************")
    print("\tCAMPERS MATRICULADOS")
    print("**************************************************************************")
    for i  in aprobados:
       print()
       documento=i["documento"]
       nombre = i["nombre"]
       print(f"{documento} : {nombre}")
       print("\n\n")

       
       
        
     
def agregaruta():
    
    campers=list(gestion.cargardatos("campersmatriculados.json"))
    while(True):
        documento=input("ingrese el documento del camper: ")


        for i in campers:
            if(i["nota"] >= 60.0 and i["documento"] == documento ):
                print(json.dumps(i, indent=4))
        if(int(input("¿ Este es el camper ?\n1.Si\n0.No"))):
               break
               

    rutas=list(gestion.cargardatos("cursando.json"))

    nombre=input("nombre y apellido del estudiante: ")
    ruta=input("que ruta le asignara: ")
    horario=input("dijita dia , si el camper elijio horario de dia , por el contrario dijite tarde: ")
    salon=input("adecuacion de salon: ")
    treiner=input("ingrese el nombre del treiner: ")
    estado=input("estado del camper?: ")

    


    diccionariorutas={"documento":documento,"nombre":nombre,"ruta":ruta,"horario":horario,"salon":salon,"treiner":treiner,"estado":estado}
    listadic=[diccionariorutas]
    rutas.append(listadic)

    gestion.guardardatos(listadic,"cursando.json")
    gestion.guardardatos(ruta,"rutasnetcore.json")  

    for i in rutas:

        if ruta=="node" and horario=="dia" and salon=="sputnik":
            gestion.guardardatos(listadic,"ruta_node_sputnik_dia.json")  
        elif ruta=="node"and horario=="tarde"and salon=="sputnik":
            gestion.guardardatos(listadic,"ruta_node_sputnik_tarde.json")

        elif ruta=="node" and horario=="dia" and salon=="apolo":
            gestion.guardardatos(listadic,"ruta_node_apolo_dia.json")
        elif ruta=="node"and horario=="tarde"and salon=="apolo":
            gestion.guardardatos(listadic,"ruta_node_apolo_tarde.json")

        elif ruta=="node" and horario=="dia" and salon=="artemis":
            gestion.guardardatos(listadic,"ruta_node_artemis_dia.json") 
        elif ruta=="node"and horario=="tarde"and salon=="artemis":
            gestion.guardardatos(listadic,"ruta_node_artemis_tarde.json")
       

##################################################################################
         
        elif ruta=="java" and horario=="dia" and salon=="sputnik":
            gestion.guardardatos(listadic,"ruta_java_sputnik_dia.json")  
        elif ruta=="java"and horario=="tarde"and salon=="sputnik":
            gestion.guardardatos(listadic,"ruta_java_sputnik_tarde.json")

        elif ruta=="java" and horario=="dia" and salon=="apolo":
            gestion.guardardatos(listadic,"ruta_java_apolo_dia.json")
        elif ruta=="java"and horario=="tarde"and salon=="apolo":
            gestion.guardardatos(listadic,"ruta_java_apolo_tarde.json")

        elif ruta=="java" and horario=="dia" and salon=="artemis":
            gestion.guardardatos(listadic,"ruta_java_artemis_dia.json") 
        elif ruta=="java"and horario=="tarde"and salon=="artemis":
            gestion.guardardatos(listadic,"ruta_java_artemis_tarde.json")

    ############################################################################################333
         
        elif ruta=="netcore" and horario=="dia" and salon=="sputnik":
            gestion.guardardatos(listadic,"ruta_netcore_sputnik_dia.json")  
        elif ruta=="netcore"and horario=="tarde"and salon=="sputnik":
            gestion.guardardatos(listadic,"ruta_netcore_sputnik_tarde.json")

        elif ruta=="netcore" and horario=="dia" and salon=="apolo":
            gestion.guardardatos(listadic,"ruta_netcore_apolo_dia.json")
        elif ruta=="netcore"and horario=="tarde"and salon=="apolo":
            gestion.guardardatos(listadic,"ruta_netcore_apolo_tarde.json")

        elif ruta=="netcore" and horario=="dia" and salon=="artemis":
            gestion.guardardatos(listadic,"ruta_netcore_artemis_dia.json") 
        elif ruta=="netcore"and horario=="tarde"and salon=="artemis":
            gestion.guardardatos(listadic,"ruta_netcore_artemis_tarde.json")
        break
          
    menus.menucoordinador()
                                

def controlcampers():
    controlcampers=list(gestion.cargardatos("cursando.json"))
    while(True):
        documento=input("ingrese el documento del camper")
        ususario=False
        for i in controlcampers:
            
            if(i["documento"] == documento):
                    print(json.dumps(i,indent=4))
                    ususario=True
                    break
        if not ususario:
                print("usuario no encontrado")
                print()
                opc=input("dijita:   0      para volver al menu coordinador, 1 para buscar otro camper ")
                if opc=="0":
                    menus.menucoordinador()
                    break
                elif opc=="1":
                    continue
                else:
                    print("opcion no valida.volviendo al menu coordinador")
                    menus.menucoordinador()
                    break      
                    

        break
   






   # control=list(gestion.cargardatos("inscripccion.json"))   
    #print()
    #print("*****************************************************")  
    #print("\tcontrol de campers")
    #print("*****************************************************")
    #for campers  in control:  
                
        
       # print(campers)
        #print("\n\n")
  
           
        
################################################################################################################################33

      
def agregartreiner():

    agregar=list(gestion.cargardatos("trainer.json"))

    trainer=input("nombre del nuevo trainer: ")
    documento=input("documento del treiner: ")
    salon=input("salon a dictar clase: ")
    ruta=input("ruta a enseñar: ")

    diccionariotrainer={"trainer":trainer,"documento":documento,"salon":salon,"ruta":ruta}
    agregar.append(diccionariotrainer)
    gestion.guardardatos(agregar,"trainer.json")   
    print()
    print("**********************************") 
    print("\tTRAINER AGREGADO")    
    print("**********************************") 



def actualizarcampers():
    actualizar=list(gestion.cargardatos("cursando.json"))
    while(True):
        documento=input("ingresa su documento: ")
        for i in actualizar:
            if(i["documento"] == documento):
                camper_encontrado=i

        if camper_encontrado:
            print("camper encontrado")
            print(json.dumps(camper_encontrado, indent=4))
            opc=input("""\tque quieres hacer?
                      (actualizar/elminar/salir)""")
            
            if opc=="actualizar":
                opcion=input("""que deseas modificarle alcamper?
                             (documento/nombre/estado)""")
                
                if opcion=="documento":
                    nuevo_documento=input("ingresa el documento a corregir: ")
                    camper_encontrado["documento"]=nuevo_documento
                    print("correcion actualizada")
                    menus.menucoordinador()

                elif opcion=="nombre":                    
                    nuevo_nombre=input("ingresa el nombre a corregir: ")
                    camper_encontrado["documento"]=nuevo_nombre
                    print("correcion actualizada")
                    menus.menucoordinador()

                elif opcion=="salir":
                    menus.menucoordinador()

            elif opc=="eliminar":
                actualizar.remove(camper_encontrado)  
                print(f"\tcamper: {camper_encontrado},Eliminado correctamente")
                print("correcion actualizada")
                gestion.guardardatos(actualizar,"cursando.json")
                menus.menucoordinador()

            elif opc=="salir":
                        break
            
            else:
                print("opcion no valida intentalo nuevamente")

        else:
            print("\tcamper no encontrado")

    gestion.guardardatos(actualizar,"cursando.json")







def dejarvernotascampers():
    dejarver=gestion.cargardatos("cursando.json")
    documento=input("incresa tu documento")
    for i in dejarver:
        if( i["documento"]==documento):
            camper=i
            print(camper)
        break









#def asignarnotastrainer():