cadena1 = "hola, soy Franklin"
cadena2 = "Bienbenido"
cadena3 = "2356253"
cadena4 = "naranja,platano,coco,uva,manzana"
cadena5 = "lol,platano,coco,uva,manz"

#DIR- devuelve la lista de atributos validos del objeto pasado
text =dir(cadena1)

#UPPER- convierte a mayuscula
text = cadena1.upper()
text = "Bienbenido".upper()

#LOWER- convierte a minuscula
text = cadena1.lower()

#CAPITALIZE- primera letra en mayuscula
text = cadena1.capitalize()

#FIND- buscamos una cadena de otra returna en la posicion y -1 si no existe
text = cadena1.find("soy")

#INDEX- lo mismo que find pero sino encuentra lanza una epcecion
text = cadena1.index("soy")

#ISNUMERIC- si es numerico devuelve true
text = cadena3.isnumeric()

#ISALPHA- si es alpha numerico(solo letras) devuelve true
text = cadena2.isalpha()

#COUNT- devuelve el numero de ocurrencias de una subcadena en la cadena dada
text = cadena1.count("a")

#LEN- cuenta los caracteres de una cadena
text = len(cadena1)

#ENDSWITH- verifica si una cadena termina con
text = cadena1.endswith("benido")

#STARTSWITH- verifica si una cadena empieza con
text = cadena1.startswith("Bien")

#REPLACE- remplaza un valor por otro
text = cadena1.replace("la", "hoho")

#SPLIT- separa por el parametro dado, crea una lista
text = cadena4.split(",")

print(text)