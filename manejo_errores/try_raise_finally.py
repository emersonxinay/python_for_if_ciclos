# -try:::=> y except se usa para errores  tipo Traceback
# con esto hacemos que se vea mejor el error por error de tipos de datos


# def palindromo(string):
#     return string == string[::-1]


# try:
#     print(palindromo(1))
# except TypeError:
#     print("Solo se pueden ingresar strings")


# -raise::::=>   evalua a mas detalle los errores

# def palindrome(string):
#     try:
#         if len(string) == 0:
#             raise ValueError("No se puede ingresar una cadena vacia")
#         return string == string[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False


# try:
#     print(palindrome(""))
# except TypeError:
#     print("Solo se pueden ingresar strings")


# -finally::=>   se usa al final de una estructura como para cerrar un  archivo, cerrar una base de datos

try:
    f = open("archivo.text")
    # hacer cualquier cosa con nuestro archivo

finally:
    f.close()
