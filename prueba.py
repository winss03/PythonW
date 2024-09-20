import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10.")

    while True:
        intento = input("Adivina el número: ")

        # Validar si la entrada es un número
        if not intento.isdigit():
            print("Por favor, ingresa un número válido.")
            continue

        intento = int(intento)
        intentos += 1

        # Verificar si el número adivinado es correcto
        if intento < numero_secreto:
            print("El número es más alto.")
        elif intento > numero_secreto:
            print("El número es más bajo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

# Ejecutar el juego
adivina_el_numero()
