#a = {2, 3, 4}
#b = {4, 5, 6}
#for i in a:
#   if i in b:
#       print(i)
#print(a^b)

#Calculadora
rep=True

while rep:
    print("""
    Programa:
    1) sumando
    2) restando
    3) multiplicando
    4) diviendo
    0) salir
    """)
    op = int(input("opcion: "))
    match op:
        case 1:
            print("Sumando")
            a = input("ingrese el numero a: ")
            b = input("ingrese el numero b: ")
            print(float(a) + float(b))
        case 2:
            print("Restando")
            a = input("ingrese el numero a: ")
            b = input("ingrese el numero b: ")
            print(float(a) - float(b))
        case 3:
            print("Multiplicando")
            a = input("ingrese el numero a: ")
            b = input("ingrese el numero b: ")
            print(float(a) * float(b))
        case 4:
            print("Diviendo")
            a = float(input("ingrese el numero a: "))
            b = float(input("ingrese el numero b: "))
            if b == 0:
                print("Error: Division por cero")
            else:
                print(a*10 // b/10)
        case 0:
            print("Saliendo...")
            rep=False
        case _:
            print("Error: Opción no válida")

#Entrada de datos
num=eval(input())
print(num)

#figuras geometricas
def area_circulo(r):
    return 3.1416 * r**2

def area_triangulo(base, altura):
    return (base * altura) / 2
#triangulo = area_triangulo
#Cuadrado = area_Cuadrilatero
#Matrice y Determinantes
