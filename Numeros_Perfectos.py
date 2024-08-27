#Un número perfecto es un número entero positivo que es igual a la suma de sus divisores 
#propios positivos. Este concepto está relacionado con los números primos de Mersenne, y 
# se pueden generar usando la fórmula
#2**(p−1) * (2**p−1), donde p y 2**p−1son primos.
a = {6, 28, 496, 8128, 2096128}
p = 11

#Generando número perfecto
b = 2**(p-1) * (2**p -1)
print(b)

#objetivo encontrar el numero perfecto impar