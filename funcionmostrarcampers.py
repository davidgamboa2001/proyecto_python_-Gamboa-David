import gestion


def mostrarcampersmatriculados():
    aprobados=list(gestion.cargardatos("campersmatriculados.json"))
    print("\tCampers matriculados")
    for i in aprobados:
       documento=i["documento"]
       nombre = i["nombre"]
       print(f"{documento}-{nombre}")
        
     
    
    