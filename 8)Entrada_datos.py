#Cadena de nombres
nombre=input("Nombre: ")
print(f"Bienvenido {nombre}")
print("Bienvenido ",nombre)
#numerico
numero=input("Numero: ")
resultado=numero*2
print(resultado)
resultado=int(numero)*2
print(resultado)
resultado=float(numero)*1.5
print(resultado)

#ejemplo "EVAL()" Evalúa la expresión ingresada como código Python.
num=input("Ingrese un operador(ej. 6*2):")
rpta=eval(num)
print(rpta)

#Matrices y estructuras
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

        
