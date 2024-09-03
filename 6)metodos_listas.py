
#LIST - crea una lista
lista = list([1, False, "Fulgrin", "Perturabo", 5])

#LEN - cuenta la cantidad de elementos de una lista
lista1 = len(lista)

#APPEND - agrega un elemento a la lista
lista.append("Leman")

#INSERT - agrega un elemento a la lista en el indice especificado
lista.insert(6, "Rogal")

#EXTEND - agrega varios elementos a la lista
lista.extend(["Corvus Corax", "Sanguinius", "Ferrus Manus"])

#POP - elimina un elemento de una lista, pide indice y devuelve valor
lista.pop(-1)

#REMOVE - remueve un elemento de una lista, pide valor
lista.remove(False)

#CLEAR - elimina todos los elementos de una lista, pide valor
#lista.clear()

#SORT - ordena una lista de forma ascendente a descendente
#lista.sort()

#REVERSE - invierte los elementos de una lista
lista.reverse()

print(lista)