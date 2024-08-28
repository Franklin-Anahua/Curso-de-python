#escribe los numeros de fibonaci en orden
a=0
b=1
i =0
n = input()
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
    
#lo mismo pero con una funcion
def finonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return finonacci(n-1) + finonacci(n-2)
    
#como hacerlo un triangulo de fibonacci
    