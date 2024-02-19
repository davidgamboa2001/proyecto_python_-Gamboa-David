


#################################################################################                       MENU PRINCIPAL

def menuprincipal():
    print("...............................")
    print(chr(27)+"[1;33m"+"\t.:BIENVENIDO A:."+'\033[0;m') 
    print(chr(27)+"[1;33m"+"\t.:CAMPUSLAND:."+'\033[0;m')
    print("...............................")
    print("""
    1-> Coordinador
    2-> Trainer
    3-> Camper
    4-> inscribite   
    """)
    opc=int(input("\telije tu categoria: "))
    return opc

###############################################################################   menu coordinador

def menucoordinador():

    print("..............................")
    print("\t.:CAMPUSLANDS:.")
    print("..........COORDINADOR.........")
    print("")

    print("""

    1-> nota para nuevos campers y cambio de estado
    2-> mostrar campers matriculados
    3-> control del camper 
    4-> agregar treiner
    5-> control de treiners
    0-> atras
    """)
    
################################################################################  menu trainer
def menutrainer():
    
    print("..............................")
    print("\t.:CAMPUSLANDS:.")
    print("............TREINER...........")
    print("")

    print("""

    1-> mi horario
    2-> control del camper 
    0-> atras
    """)


##############################################################################    menu camper


def menucampers():
    print("..............................")
    print("\t.:CAMPUSLANDS:.")
    print("..........CAMPERS.........")
    print("")

    print("""

    1-> mi control
    0-> atras
    """)










