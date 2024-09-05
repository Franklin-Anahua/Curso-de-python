
import keyboard

colores = ["Rojo", "Verde", "Azul", "Amarillo", "Blanco", "Negro"]
indice = 0  # Índice del color seleccionado

def mostrar_color_actual():
    print("\nElige un color usando las teclas de flecha. Pulsa 'q' para salir.")
    for i, color in enumerate(colores):
        if i == indice:
            print(f"> {color}")  # Indicar el color seleccionado
        else:
            print(f"  {color}")

mostrar_color_actual()

while True:
    if keyboard.is_pressed('up'):
        if indice > 0:
            indice -= 1
        mostrar_color_actual()
        keyboard.wait('up')  # Espera que se suelte la tecla
    elif keyboard.is_pressed('down'):
        if indice < len(colores) - 1:
            indice += 1
        mostrar_color_actual()
        keyboard.wait('down')  # Espera que se suelte la tecla
    elif keyboard.is_pressed('q'):
        print("Has salido del programa.")
        break
