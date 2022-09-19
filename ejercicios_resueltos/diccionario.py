def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'argentina': 4534565,
        'brasil': 24787544,
        'colombia': 323453
    }
    # >>>>para buscar por llave
    # print(poblacion_paises['argentina'])

    # >>>>para buscar por llaves con for
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # >>>>para buscar por item la llave y su valor
    # for pais, poblacion in poblacion_paises.items():
    #     print(pais + 'tiene' + str(poblacion) + 'habitantes')

    # para buscar solo con sus valores

    for pais in poblacion_paises.values():
        print(pais)


if __name__ == '__main__':
    run()
