def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # ejercico de numeros elevados al cuadrado
    # se lee: para cada iterador del rango de 1 a 101 quiero guardar el i **2 solo si i %3 no sean divisibles de 3
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # print(squares)

    lista = [i for i in range(1, 10001) if i % 36 == 0]

    print(lista)


if __name__ == '__main__':
    run()
