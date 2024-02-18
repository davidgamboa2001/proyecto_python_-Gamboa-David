import funcioncampers,notacampers,funcioncampers
import menus


################################################################################################# opcciones del menu principal
while(True):
    opc = menus.menuprincipal()
    if(opc == 1):               
        while True:
            ingreso=1234
            pasword=int(input("\tingrese su coontraseña de coordiland , o ingrese 0 para sali: "))
            if pasword == 0:
                menus.menuprincipal()
            else:
##############################  ingreso dentro del menu del coordinador   ##########################                
                if pasword==ingreso:
                    menus.menucoordinador()                    
                    while True:
                        opcion=int(input("\tingrese la actividad que vas a realizar"))
                        if opcion==1:
                            notacampers.insertarnota()
                            input()
                            
                        elif opcion==2:
                            funcioncampers.mostrarcampersmatriculados()
                            opc=input("marque S(si) para agregarles una ruta y salon").upper
                            funcioncampers.agregaruta()

                        elif opcion==3:
                                funcioncampers.controlcampers()

                            
                        
                else:
                    print("\tno eres un coordinador campus")
                    
                    
                            
    elif(opc == 2):
        while True:
            ingreso=456
            pasword=int(input("ingrese su contraseña de trainer, o ingrese 0 para salir"))
            if pasword==0:
                menus.menuprincipal()
            else:
                if pasword == ingreso:
                    menus.trainer()   
            

    elif (opc ==3):
        print("")
    
    
    
    elif (opc == 4):
        funcioncampers.incripcion()
        print(" EXITO ")
        
            
                


