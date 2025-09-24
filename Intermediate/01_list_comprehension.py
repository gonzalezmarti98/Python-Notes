### List Comprehension ###
"""
Puedes hacer operaciones a partir de una lista que ya tengas.
Modificamos el valor antes de ponerlo.
"""

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in my_original_list]
my_list = [i for i in range(8)] # los 2 imprimen lo mismo
print(my_list)

#Me puedo crear una lista a partir de otra, añadiendo algo. Sumando +1 a todo por ejemplo
my_plus_one_list = [i + 1 for i in my_original_list]
print(my_plus_one_list)

#Se puede también juntarlo con funciones
def sum_five(element):
    return element +5

my_list = [sum_five(i) for i in range(8)]
print(my_list)
