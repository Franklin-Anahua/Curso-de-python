#Ejercicio 2
#a) Pedirle al usuario que diga cualquier texto real y:
#-calcular cuanto tardaria en decir esa frase
#¿cuantas palabras dijo?
#b) Si se tarda mas de un minuto: 
#-decirle: "para amigo tampoco te pedi un testameto"
#c) Dhor habla un 30% mas rapido:
#¿Cuanto tardara en decirlo?

#pides una frase
frase=input("Escribe una frase, y te calcule el tiemo que te tardarias: ")
#creamos una lista
p_separadas=frase.split(" ")
#len() cantidad de elementos
cantidad_p=len(p_separadas)
#cuanto tiempo demora
print(f"""
Dijistes {cantidad_p} palabras, tardarias {cantidad_p/2} segundos en decirlo
Dhor lo diria en {(cantidad_p/2*1.3)*100//1/100} segundos en decirlo""")
#en caso de que tarde mas de un minuto
if cantidad_p > 120:
    print("para flaco no te pedi que escribieras tu testamento...")