#Promedio de duracion
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_prom=4
Dhor=1.5

#Duracion de crudos
crudo_prom=5
crudo_Dhor=3.5

#Diferencia de duracion
diferencia_con_min=100-Dhor/otros_cursos_min*100
diferencia_con_max=100-(Dhor*1000//otros_cursos_max) /10 
diferencia_con_prom=100-Dhor/otros_cursos_prom*100

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_prom=100-otros_cursos_prom*1000//crudo_prom/10
tiempo_vacio_Dhor=100-Dhor*1000//crudo_Dhor/10

#Mostrando las diferencias de duracion(Ej-A)
print("----------------------------------------------------------------")
print(f"El Curso de Dhor dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El Curso de Dhor dura un {diferencia_con_max}% menos que el mas lento")
print(f"El Curso de Dhor dura un {diferencia_con_prom}% menos que el mas promedio")
print("----------------------------------------------------------------")

#Mostrando la cantidad
print(f"Un curso promedio elimina un {tiempo_vacio_prom}% de tiempo vacio")
print(f"Este curso elimino el {tiempo_vacio_Dhor}% de tiempo vacio")
print("----------------------------------------------------------------")

#Mostrando diferencias si los recursos duraran 10horas
print(f"""ver 10 horas de este curso equivale a ver {otros_cursos_prom*100//Dhor/10} horas de otro curso
ver 10 horas de otros curso equivale a ver {Dhor*100//otros_cursos_prom/10} horas de otro curso""")
print("----------------------------------------------------------------")

#

