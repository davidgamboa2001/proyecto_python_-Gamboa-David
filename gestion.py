import json


def cargardatos(archivo):
    try:
        with open(archivo,"r")as file:
            respuesta=json.load(file)
            return respuesta
    except Exception:
        return[]
    
def guardardatos(datos,archivo):
    with open(archivo,"w")as file:
        escritura=json.dumps(datos,indent=4)
        file.write(escritura)


