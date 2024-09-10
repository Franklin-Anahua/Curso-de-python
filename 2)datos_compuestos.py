lista = ["frank", 15, True] #se pude modificar la lista
tupla = ("frank", 15, False) # igual que el anterios pero no se modifica    
conjunto = {"frank", 15, False, False} # no repite datos
diccionario = {
    "nombre" : "Franklin",
    "edad" : "17",
    "estado" : "soltero"
}
#aqui es key codigo y luego dato 
print(tupla, "\n")

logica={
    "V or V" : True,
    "V or F" : True,
    "F or V" : True,
    "F or F" : False,
    "V and V" : True,
    "V and F" : False,
    "F and V" : False,
    "F and F" : False,
    "V xor V" : False,
    "V xor F" : True,
    "F xor V" : True,
    "F xor F" : False,
    "not V" : False,
    "not F" : True,
    "V -> V" : True,
    "V -> F" : False,
    "F -> V" : False,
    "F -> F" : True,
    "V <=> V" : True,
    "V <=> F" : False,
    "F <=> V" : False,
    "F <=> F" : True,
    "V <= V" : True,
    "V <= F" : True,
    "F <= V" : False,
    "F <= F" : True,
    "V >= V" : True,
    "V >= F" : False,
    "F >= V" : False,
    "F >= F" : True,
    "V > V" : False,
    "V > F" : False,
    "F > V" : True,
    "F > F" : True,
    "V == V" : True,
    "V == F" : False,
    "F == V" : False,
    "F == F" : True,
    "V != V" : False,
    "V != F" : True,
    "F != V" : True,
    "F != F" : False
}
