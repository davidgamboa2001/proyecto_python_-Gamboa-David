import gestion



def insertarnota():
    mostrar=(gestion.cargardatos("inscripccion.json"))
    if mostrar==False:
        print("no hay campers registrados")
    else:
        

        documento=(input("ingrese el documento del camper para aprobar"))
                
        for i in mostrar:
                if i["documento"] == documento:
                    nota = int(input("Digita la nota: "))
                    i["nota"] = nota
                else:
                    print("no es")
        

        gestion.guardardatos(mostrar,"inscripccion.json")
        print()
        print("\texito!")
        input()
