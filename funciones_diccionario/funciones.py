
# formas de invertir las palabras que son lo mismo al revez también


# def palindrome(string):
#     return string == string[::-1]


# print(palindrome('ana'))

# # map ::: sacar el cuadrado de valor de la lista
# my_list = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, my_list))
# print(squares)


# # para multiplicar todos los numeros
# my_list = [2, 2, 2, 2, 2]
# all_multiple = 1
# for i in my_list:
#     all_multiple = all_multiple * i

# print(all_multiple)


from functools import reduce
my_list = [5, 2, 2, 2, 2]
all_multipled = reduce(lambda a, b: a*b, my_list)

print(all_multipled)
