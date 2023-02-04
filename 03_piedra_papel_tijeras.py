from random import randint

player = 0
cpu = 0

def result(choose, choose_cpu):
    if (choose == 1 and choose_cpu == 3) or (choose == 2 and choose_cpu == 1) or (choose == 3 and choose_cpu == 2):
        print("Has ganado")
        return 1
    elif (choose_cpu == 1 and choose == 3) or (choose_cpu == 2 and choose == 1) or (choose_cpu == 3 and choose == 2):
        print("Has perdido")
        return -1
    else:
        print("Empate")
        return 0

while True:
    print("Selecciona tu movimiento")
    choose = int(input("1.Piedra \t 2.Papel \t 3.Tijeras \n"))

    choose_cpu = randint(1, 3)

    if choose < 1 or choose > 3:
        print("Ingresa una opción válida")
        continue
    else:
        puntaje = result(choose, choose_cpu)
        if puntaje < 0:
            cpu = cpu + 1
        elif puntaje > 0:
            player = player + 1

    if input("Quieres seguir jugando? \t yes/no \n").lower() == "no":
        print("Puntaje obtenido:")
        print(f"CPU = {cpu} \t\t Jugador = {player}")
        break