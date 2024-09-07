a=5
b=3
suma = a + b
resta = a - b
multiplicar = a*b
dividir = a/b #devuelve siempre flotantes
potencia = a**b
division_baja = a//b #enteros  int redondeo  hacia abajo
resto = a%b #resto

tipo_de_dato = type(division_baja)#type(dato) indica que tipo de dato es.
print(tipo_de_dato)

#Numeros aleatorios
from random import randint
def genera(a=None):
    if a == None:
        a = randint(1, 100)
    return a
print(genera())
print(genera(), genera())
print(a)