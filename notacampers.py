import gestion
import menus
import json


def insertarnota():
    ingresado=gestion.cargardatos("inscripccion.json")
    

    if ingresado==False:
        print("no se encontro datos del ingresado: ")
    else:
        documento=input("Ingresar el documento del registrado para evaluar: ")
        
        for usuario in ingresado:
            

            if usuario["documento"]== documento:
                print(json.dumps(usuario,indent=4))           
                print("\tevaluar")
                nota1=int(input("nota teorica :"))
                print("........................")
                nota2=int(input("nota practica :"))
                print("-------------------------")
                notatotal= (nota1+nota2)/2
                usuario["nota"]=notatotal

                if notatotal>= 60:
                    aprobado=list(gestion.cargardatos("campersmatriculados.json"))
                    aprobado.append(usuario)
                    gestion.guardardatos(aprobado,"campersmatriculados.json")
                    print()
                    print("**************************************************************************")
                    print("\t.:EL USUARIO APROBO Y FUE MATRICULADO:. ")
                    print("**************************************************************************")
                else:
                     print("**************************************************************************")
                     print("USUARIO NO APROBADO")    
                     print("**************************************************************************")
       
                     print(menus.menucoordinador)

    gestion.guardardatos(ingresado,"inscripccion.json")
    print()
    print("\tEXITO")
    menus.menucoordinador()

                                            


 
