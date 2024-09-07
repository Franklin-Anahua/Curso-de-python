usuario = "Franklin"
usuar = input("Ingresa tu Nombre de usuario: ")

# os.system("cls") # para windows
while usuar != "Franklin":
    print("usuario incorrecto")
    print("Intente de nuevo")
    usuar = input()
print("se ha ingresado correctamente el usuario")

#Año bisiesto
op=True
while op:
    fecha=int(input("Ingrese el año(bisiesto o no): "))
    if fecha == 0:
        print("Saliendo...")
        op=False
    elif (fecha%4==0 and fecha%100==0) or fecha%400==0:
        print(f"{fecha} es un año bisiesto")
    else:
        print(f"{fecha} no es un año bisiesto")
    