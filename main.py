import menus

#notas:[90,80]
#{
#"python":0}

while(True):
    opc = menus.menuprincipal()
    if(opc == 1):
        while True:
            ingreso=1234
            pasword=int(input("ingrese su coontraseña de coordinador, o ingrese 0 para sali"))
            if pasword == 0:
                menus.menuprincipal()
            else:
                if pasword==ingreso:
                    menus.menucoordinador()
                    while True:
                        opcion=int(input("\tingrese la actividad a realizar"))
                        if opcion==0:
                            break


                else:
                    print("\tno eres un coordinador campus")
    elif(opc == 4):
        print("Chao!")
        break


