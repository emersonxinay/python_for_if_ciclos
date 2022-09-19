# programar un juego que adivina un numero
import random  # funciones que tiene datos aleatorios


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numeor de 1 al 100: '))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un numero mas grande ')
        else:
            print('Busca numero mas pequeño')
        numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste!!! 🙌')


if __name__ == '__main__':
    run()
