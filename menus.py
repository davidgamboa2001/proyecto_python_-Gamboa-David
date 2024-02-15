def menuprincipal():
    print("")
    print("\t.:BIENVENIDO:.")
    print(".........A CAMPUSLANDS.........")
    print("")
    print("""
    1-> Coordinador

    2-> Trainer

    3-> Camper
        
    4-> salida
          """)

    opc=int(input("\telije tu categoria"))
    return opc



def menucoordinador():

    print("")
    print("\t.:CAMPUSLANDS:.")
    print("..........COORDINADOR.........")
    print("")

    print("""

    1-> nota para campers y cambio de estado
    2-> control del camper 
    3-> control de treiner
    0-> atras
    """)

