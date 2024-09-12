#Creando a la tupla
d_tupla = ("Dhor", "Adous", 18)
d_lista = ["Dhor", "Adous", 18]
#desempaquetado
nombre,apellido,edad = d_tupla
nombre,apellido,edad = d_lista
#mostrando resultado
print(f"Mi nombre es {nombre} {apellido} con {edad} años")
#desempaquetado
nombre,apellido,edad = d_lista


#Creando tuplas
tuplas = tuple(["dato1", "dato2"])
tuplas1 = "Dato1", "Dato2"
tuplas2 = "Dato",
print(tuplas2, "\n")


#Creando conjunto con set
conjuntos = set(["Var1", "Var2"])
print(conjuntos, "\n")
#metiendo un conjunto dentro de otro conjunto
conjunto1=frozenset(["vari1", "vari2"])
conjunto2={conjunto1,"vari 3"}
print(conjunto2, "\n")
#teoria de conjuntos
conjunt1={1,2,3,7}
conjunt2={1,2,7}
#verificando si es un subconjunto
resultado=conjunt2.issubset(conjunt1)
resultado=conjunt2<=conjunt1
print(resultado, "\n")#true or false
#verificando si es un superconjunto
resultado=conjunt2.issuperset(conjunt1)
resultado=conjunt2>conjunt1
print(resultado, "\n")#true or false
#verificar si hay algun numero en comun
resultado=conjunt2.isdisjoint(conjunt1)
print(resultado, "\n")#true or false

