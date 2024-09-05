#Ejercicio 2
#a) Pedirle al usuario que diga cualquier texto real y:
#-calcular cuanto tardaria en decir esa frase
#¿cuantas palabras dijo?
#b) Si se tarda mas de un minuto: 
#-decirle: "para amigo tampoco te pedi un testameto"
#c) Dhor habla un 30% mas rapido:
#¿Cuanto tardara en decirlo?

frase=input("Escribe una frase, y te calcule el tiemo que te tardarias: ")
p_separadas=frase.split(" ")
cantidad_p=len(p_separadas)
print(f"""
Dijistes {cantidad_p} palabras, tardarias {cantidad_p/2} segundos en decirlo
Dhor lo diria en {(cantidad_p/2*1.3)*100//1/100} segundos en decirlo""")