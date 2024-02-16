import gestion



def insertarnota():
    ingresado=gestion.cargardatos("inscripcion.json")
    if ingresado==False:
        print("no se encontro datos del ingresado")
    else:
        documento=int(input("Ingresar el documento del registrado para evaluar"))

        for usuario in ingresado:

            if usuario["documento"]== documento:
                print("\tevaluar")
                nota1=int(input("nota teorica"))
                print("........................")
                nota2=int(input("nota practica"))
                print("-------------------------")
                notatotal= (nota1+nota2)/2
                usuario["nota"]=notatotal

                if notatotal>= 60 :
                    aprobado=list(gestion.cargardatos("campersmatriculados.json"))
                    aprobado.append(usuario)
                    gestion.guardardatos(aprobado,"campersmatriculados.json")
                    print("El Usuario Aprobo y fue matriculado")
                else:
                    print("El Usiario no fue Aprobado")    
            else:
                print("Usuario no encontrado")

    gestion.guardardatos(ingresado,"inscripcion.json")
    print()
    print("\tEXITO")

                                            


 
