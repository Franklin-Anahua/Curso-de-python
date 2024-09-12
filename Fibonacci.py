
#Programa principal

#lo mismo pero con una funcion
def finonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return finonacci(n-1) + finonacci(n-2)
    
#como hacerlo un triangulo de fibonacci
def fibonacci(n):  
    """Genera una lista de los primeros n números de Fibonacci."""  
    fib = [0, 1]  
    for i in range(2, n):  
        fib.append(fib[i-1] + fib[i-2])  
    return fib[:n]  
def triangulo_fibonacci(n):  
    """Genera un triángulo de Fibonacci con n filas."""  
    fib_numbers = fibonacci(n * (n + 1) // 2)  # Total de números necesarios  
    index = 0  
    for i in range(1, n + 1):  
        for j in range(i):  
            print(fib_numbers[index], end=' ')  
            index += 1  
        print()  # Nueva línea después de cada fila 
        
#como hacerlo un triangulo de fibonacci

def fibonacci2(n):  
    """Genera un número de Fibonacci."""  
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
def triangulo_fibonacci2(n):
    """Genera un triángulo de Fibonacci con n filas."""  
    for i in range(1, n + 1):
        print(" ".join(str(fibonacci(j)) for j in range(i)))
        

#escribe los numeros de fibonaci en orden
a=0
b=1
i =0
n = input()
#triangulo_fibonacci2(n)
try:
    entero = int(n)
    print("entero")
except ValueError:
    print("no entero")
while i<entero:
    i +=1
    c=a+b
    a=b
    print(b)
    b=c
    
#FIBONACI
def FIBONACI_CUADRADO():
    """Genera los primeros n números de Fibonacci cuadrados."""
    fib_numbers = fibonacci(n * (n + 1) // 2)  # Total de números necesarios
    index = 0
    for i in range(1, n + 1):
        for j in range(i):
            print(fib_numbers[index] ** 2, end=' ')
            index += 1
        print()  # Nueva línea después de cada fila
    