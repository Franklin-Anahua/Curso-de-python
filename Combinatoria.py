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
def cambiar_base(numero, base):  
    if base < 2 or base > 36:  
        raise ValueError("La base debe estar entre 2 y 36")  
    
    if base == 10:  
        return str(numero)  
    
    # Convertir a base deseada  
    resultado = ""  
    while numero > 0:  
        resultado = str(numero % base) + resultado  
        numero //= base  
    
    return resultado  
# Ejemplo de uso  
numero_base_10 = 42  
base_deseada = 2  
numero_en_base_dos = cambiar_base(numero_base_10, base_deseada)  
print(f"El número {numero_base_10} en base {base_deseada} es: {numero_en_base_dos}")  
# Convertir de base 2 a base 10  
numero_base_2 = "101010"  
numero_en_base_diez = int(numero_base_2, 2)  
print(f"El número {numero_base_2} en base 10 es: {numero_en_base_diez}")


#dia/mes/año
#capicua