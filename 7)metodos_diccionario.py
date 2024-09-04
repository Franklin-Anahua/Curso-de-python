diccionario = {
    "Primarca" : "Semidioses",
    "Xeno" : "Alien",
    "Hereje" : "Traicion",
    "Coraje" : "Valentia"
}
#devuelve las claves
claves = diccionario.keys()
#devuelve el valor de la clave
valor1 = diccionario["Primarca"]
valor2 = diccionario.get("mo hay nad")
#elimina todo los elementos
#diccionario.clear()
#elimimina un elemento
elim=diccionario.pop("Primarca")
#obtiene un elemento iterable
iterable=diccionario.items()
print(iterable)
