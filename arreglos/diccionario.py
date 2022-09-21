# # listas
# variable = ["string", 49, 34.5, True]
# variable[1]

# # diccionario

# variable2 = { "clave1": "emerson", "clave2": 45 }
# print(variable2["clave2"])

# print(variable2["clave1"])

# notas = {"Camila": 7, "Antonio": 5, "Antonia": 20, "Felipe": 6, "Antonio2": 50}
# print("tiene nota de: ", notas["Antonio"])

# print(notas)
# notas["emerson"]=20

# print(notas)

# # elimnado datos del diccionario
# eliminando_dato = notas.pop("Camila")
# print(eliminando_dato)


# print(notas)

# uniendo diccionarios

# diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
# diccionario_b = {"mascota": "miti", "ejercicio": "bicicleta"}
# diccionario_c = {"mascota": "miti", "ejercicio": "juan"}

# diccionario_a.update(diccionario_b)

# union = diccionario_a | diccionario_b | diccionario_c


# # print(diccionario_a)

# print(union)


# tuplas
# tupla_ej = ("Abril", 2021, "15:30")
# dato = "string"


# print(type(tupla_ej))
# print(type(dato))


# # sets

# muchos_animales = {
#     "Gato",
#     "Perro",
#     "Tortuga",
#     "Gato",
#     "Perro",
#     "Tortuga",
#     "Gato",
#     "Perro",
#     "Tortuga",
#     "Gato",
#     "Perro",
#     "Tortuga",
#     "Hurón",
#     "Hamster",
#     "Erizo de Tierra",
# }

# print(set(muchos_animales))

# hacer un programa que en tu diccionario tengas como clave fechas exactas de dias festivos
# y tu valor tenga lo que se celebra ese día
# El programa tiene que permitir ingresar fecha exacta caso contrario dira que no existe esa fecha

# Diccionario
efemerides = {
    "1 de enero": "Anio Nuevo",
    "27 de febrero": "Terremoto en Chile",
    "8 de marzo": "Dia de la Mujer",
    "21 de mayo": "Glorias Navales",
    "18 de septiembre": "Fiestas Patrias",
    "19 de septiembre": "Glorias del Ejercito",
    "25 de diciembre": "Navidad",
}

fecha = input("Ingrese una fecha: ").lower()

print(f'Efemerides: {efemerides.get(fecha, "No hay eventos para esta fecha")}')

a = 15
b = 30
print(f"el numero es {a} y {b} ")
