# assert se lee de la siguiente manera
# afirmo que es condición es verdadera sino lee el mensaje de error
# assert condicion, mensaje de error

# # ejemplo normal
# def palindrome(string):
#     return string == string[::-1]


# print(palindrome(""))

# # ejemplo aplicando assert

# def polindrome(string):
#     assert len(string) > 0, "no se puede ingresar una cadena vacia "
#     return string == string[::-1]


# print(polindrome(""))

# aplicando assert en ejercicio pasado

def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():

    num = input("ingrese un numero: ")
    # isnumeric  es para saber si es numero o no
    assert num.isnumeric() and int(num) >= 0, "debes ingresar un número positivo"
    # si pasa, convertimos el numero a entero caso contrario saldra el mensaje de assert
    print(divisor(int(num)))
    print("Muy bien funciono todo ok")


if __name__ == '__main__':
    run()
