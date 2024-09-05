#https://www.youtube.com/watch?v=vBgrvVY1jGo
# programa de computacion "ESTRACTEGIA"
#"RAMDON"
#"friendman" (guarda rencor) empieza comperando y si su oponenente no coopera una vez dejará de cooperar por el resto del juego
#"Joss" (astuto) empezaba cooperando pero luego copiaba lo que hacía el otro jugador en su último turno alrededor del 10% de las veces Jos se hacía el listo y no cooperaba 


#tabla de juego si y no (sisi= 3-3 sino = 5-0 nono= 1-1)
print ("""
INSTRUCCIONES DEL JUEGO: "ESTRACTEGIA"
En este juego tu objetivo sera llegar al maximo                Jugador 1           Jugador 2
puntaje posible, en cuestion te enfrentaras a                  ------------------------------
otro individuo donde ambos tendran la opcion de                            *****
elegir entre Cooperar o No cooperar.                           SI        ***   ***         SI
-Si ambos Cooperan, ambos ganaran 3puntos                              ***       ***
-Si uno Coopera y el otro No coopera, entonces                       ***    3-3    ***  
se dara 5 pts al otro y tu tendras 0 pts                           **  ***       ***  **
-Si ambos No cooperan, ambos tendran 1 pts                       **      ***   ***      **  
                                                               **    5-0   *****    0-5   **
                                                                 **      ***   ***      **  
                                                                   **  ***       ***  **
                                                                     ***    1-1    ***  
                                                                       ***       ***
                                                                NO       ***   ***         NO
                                                                           *****
                                                                           
""")
#"" ()

#"friendman" (guarda rencor)
def Friendman(J1):
    if J1 != "NO":
        return "SI"
    return "NO"
#"Joss" (astuto)
def Joss():
    if J1 == "SI":
        return "SI"
    quit
    return "NO"


#convierte la opcion en puntaje
def puntaje(J1, J2):
    puntos1 = 0
    puntos2 = 0
    if J1 == J2 and J2=="SI":
        puntos1 = 3
        puntos2 = 3
    elif J1 == "SI":
        puntos1 = 0
        puntos2 = 5
    elif J2 == "SI":
        puntos1 = 5
        puntos2 = 0 
    else:
        puntos1 = 1
        puntos2 = 1
    print(f"    {puntos1}   ,       {puntos2}")
    return puntos1, puntos2


#programa principal
n = input("Cuantas partidas vas a jugar: ")
Jugador1 = input("Ingrese su usuario: ")
partidas = int(n)

i=0
while i < partidas:
    enfrentamiento =  f"{Jugador1}      VS      BOT"
    print (enfrentamiento)
    J1 = input()
    J2 = Friendman(J1)
    puntaje(J1, J2)
    i += 1
#puntos_jugador1, puntos_jugador2 = jugar_dilema_prisionero()  
#print(f"Puntos finales: Jugador 1: {puntos_jugador1}, Jugador 2: {puntos_jugador2}")  
#def jugar_dilema_prisionero():  
    #print("Bienvenido al Dilema del Prisionero")  
    # Opciones de los jugadores  
    #opciones = ["Cooperar", "Traicionar"]  
    















