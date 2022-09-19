import math


def run():
    # diccionario = {}
    # for i in range(1, 100):
    #     if i % 3 != 0:
    #         diccionario[i] = i**3
    # print(diccionario)
    # los primeros 100 llaves y valores no multiplos de 3
    # diccionario = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(diccionario)

    diccinario = {i: math.sqrt(i) for i in range(1001)}

    print(diccinario)


if __name__ == ('__main__'):
    run()
