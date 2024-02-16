import gestion
import menus



def insertarnota():
    ingresado=gestion.cargardatos("inscripccion.json")
    print(ingresado)

    if ingresado==False:
        print("no se encontro datos del ingresado")
    else:
        documento=input("Ingresar el documento del registrado para evaluar :")

        for usuario in ingresado:

            if usuario["documento"]== documento:
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
                    print("El Usuario Aprobo y fue matriculado")
                else:
                    print("El Usiario no fue Aprobado")    
            else:
                print("Usuario no encontrado")

    gestion.guardardatos(ingresado,"inscripccion.json")
    print()
    print("\tEXITO")
    menus.menucoordinador()

                                            


 
