usuario = "Franklin"
usuar = input()

# os.system("cls") # para windows

if usuario == usuar:
    print("se ha ingresado correctamente el usuario")
elif usuario != usuar:
    print("Intente de nuevo")
    usuar = input()
    #continue
else:
    print("usuario incorrecto")
