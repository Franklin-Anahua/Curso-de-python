#Factorial
import math  
numero = 4
print(f"El factorial de {numero} es {math.factorial(numero)}")

def factorial_iterative(n):  
    resultado = 1  
    for i in range(2, n + 1):  
        resultado *= i  
    return resultado  

# Ejemplo de uso  
numero = 4  
print(f"El factorial de {numero} es {factorial_iterative(numero)}")


#permutación
from itertools import permutations  
elementos = ['A', 'B', 'C']  
permutaciones = list(permutations(elementos))  
for p in permutaciones:  
    print(p)
    
#combinatoria
#Cambio de base
#dia/mes/año
#capicua