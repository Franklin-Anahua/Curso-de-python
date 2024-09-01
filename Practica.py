#a = {2, 3, 4}
#b = {4, 5, 6}
#for i in a:
#   if i in b:
#       print(i)
#print(a^b)

#Calculadora
print("""
    Programa:
    1) sumando
    2) restando
    3) multiplicando
    4) diviendo
    0) salir
""")
op = int(input("opcion: "))


if op != 0:
    a = input("ingrese el numero a: ")
    b = input("ingrese el numero b: ")
    if op == 1:
        print(int(a) + int(b))
    elif op == 2:
        print(int(a) - int(b))
    elif op == 3:
        print(int(a) * int(b))
    elif op == 4:
        if int(b) == 0:
            print("Error: Division por cero")
        else:
            print(int(a) / int(b))
    else:
        print("Error: Opción no válida")



