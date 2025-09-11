### Lists ###

# formas de crear listas
my_list = list()
my_other_list = [1, 5, "Holaaa"]

"""En Python se pueden guardar diferentes tipos de datos
en una sola lista: string, int, float, string ...
"""
list_diff_data = ["hola", 2, "mundo", 1.89, 2]

print(list_diff_data.count(1.89)) # ver las veces que se repite un elemento en una lista

print(list_diff_data + my_other_list)
print("\n")

# Añadir a la lista:
list_diff_data.append("AZUL") # append para añadir (al final de la lista)
print(list_diff_data)

list_diff_data.insert(0, "ROJO") # con el insert elijo posición
print(list_diff_data)

list_pop = list_diff_data.pop(1) # el pop sirve para eliminar un elemento pero quedárselo
print(list_pop)                  # por lo tanto list_pop tendrá lo del índice 1 ("hola")

del list_diff_data[0] # del para eliminar un elemento de la lista
print(list_diff_data)

list_diff_data.clear() # el clear()  deja la lista vacía. NO la elimina
print(list_diff_data)

num_list = [10, 66, 3, 22]
num_list.sort() # el sort() ordena la lista (deben de ser todo numeros)
print(num_list)

word_list = ["hola", "a", "aaaaaaaaaaaaaaaaaaa", "x"]
word_list.sort() # los String se ordenan alfabéticamente, NO por longitud
print(word_list)