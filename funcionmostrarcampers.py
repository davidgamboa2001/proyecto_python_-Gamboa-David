import gestion


def mostrarcampersmatriculados():
    aprobados=list(gestion.cargardatos("campersmatriculados.json"))
    print("\tCampers matriculados")
    gestion.guardardatos(aprobados, "campersmatriculados.json")
    