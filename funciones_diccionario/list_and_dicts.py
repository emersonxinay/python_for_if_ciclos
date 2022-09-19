def run():
    mi_list = [1, "hello", True, 4.5]
    my_dict = {"firtname": "emerson", "lastanme": "Espinoza"}

    super_list = [
        {"firtname": "emerson", "lastanme": "Espinoza"},
        {"firtname": "susana", "lastanme": "Mendoza"},
        {"firtname": "jsoe", "lastanme": "Castro"},
        {"firtname": "junior", "lastanme": "aguirre"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6],
        "interger_nums":  [-1, -3, 0, 1, 3],
        "floating_nums": [1.3, 4.3, 5.6, 4.7]
    }

    for key, values in super_dict.items():
        print(key, "-", values)


if __name__ == '__main__':
    run()
