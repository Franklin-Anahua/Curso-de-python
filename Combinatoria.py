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
import itertools
def generar_combinaciones(elementos, r):
    """Genera combinaciones de r elementos de la lista."""
    return list(itertools.combinations(elementos, r))

def generar_permutaciones(elementos, r):
    """Genera permutaciones de r elementos de la lista."""
    return list(itertools.permutations(elementos, r))
# Ejemplo de uso
if __name__ == "__main__":
    elementos = ['A', 'B', 'C', 'D']
    r = 2
    combinaciones = generar_combinaciones(elementos, r)
    print(f"Combinaciones de {r} elementos: {combinaciones}")
    permutaciones = generar_permutaciones(elementos, r)
    print(f"Permutaciones de {r} elementos: {permutaciones}")


#Cambio de base
#dia/mes/año
#capicua