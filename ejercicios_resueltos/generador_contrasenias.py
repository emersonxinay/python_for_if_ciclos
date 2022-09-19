# import random


# def generar_contrasena():
#     mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     minusculas = ['a', 'b', 'c', 'd', 'e', 'f']
#     simbolos = ['!', '#', '$', '/', '(', ')']
#     numeros = ['1', '2', '3', '6', '5', '7']
#     caracteres = mayusculas + minusculas + simbolos + numeros
#     contrasena = []

#     for i in range(15):
#         caracter_random = random.choice(caracteres)
#         contrasena.append(caracter_random)
#     contrasena = "".join(contrasena)
#     return contrasena


# def run():
#     contrasena = generar_contrasena()
#     print("tu nueva contraseña es: " + contrasena)


# if __name__ == '__main__':
#     run()


# :::::>>>>> segunda formas de generar contraseña ::::<<<<<<

import random
import string


def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits + \
        string.punctuation + string.ascii_uppercase

    contrasena = []

    while (len(contrasena) < 16):
        caracteres = random.choice(caracter)
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == "__main__":
    run()
