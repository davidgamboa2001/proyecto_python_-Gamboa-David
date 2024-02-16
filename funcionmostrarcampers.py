import gestion


def mostrarcampersmatriculados():
    aprobados=list(gestion.guardardatos("campersmatriculados.json"))
    gestion.guardardatos(aprobados, "campersmatriculados.json")
    return aprobados