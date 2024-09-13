#Dirreccionales
op=input("brujula")
match(op):
    case "w":
        print("Norte")
    case "s":
        print("Sur")
    case "a":
        print("Este")
    case "d":
        print("Oeste")
    case _:
        print("No es una direccion valida")
