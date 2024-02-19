import notacampers
import menus
import definiciones

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
                
#############  ingreso dentro del menu del coordinador   ##########################                
                if pasword==ingreso:
                                       
                    while True:
                        menus.menucoordinador()     
                        opcion=int(input("\tingrese la actividad que vas a realizar: "))
                        if opcion==1:
                            notacampers.insertarnota()
                            
                            
                        elif opcion==2:
                            definiciones.mostrarcampersmatriculados()
                            print()
                            opc=input("marque S(si) para agregarles una ruta y salon o N(no)para devolver al menu ")
                        
                            if opc.lower()=="s":
                                definiciones.agregaruta()
                            elif opc.lower()=="n":
                                continue


                        elif opcion==3:
                                definiciones.controlcampers()
                                opc=input("deseas modificar algun camper?: ")
                                if opc=="si":
                                    definiciones.actualizarcampers()
                                

                        
                        elif opcion==4:
                                definiciones.agregartreiner()

            print("\tno eres un coordinador campus")   
                            
                       
                    
                            
    elif(opc == 2):
        while True:
            ingreso=456
            pasword=int(input("ingrese su contraseña de trainer, o ingrese 0 para salir: "))
            if pasword==0:
                menus.menuprincipal()
            else:
                if pasword == ingreso:
                    menus.menutrainer()
            

    elif (opc ==3):
        
        menus.menucampers()
        opc=int(input("elije tu objetivio a realizar"))
        if opc == 1:    
            definiciones.dejarvernotascampers()

        else:
            menus.menuprincipal()    

    
    
    elif (opc == 4):
        definiciones.incripcion()
        
        
            
                


