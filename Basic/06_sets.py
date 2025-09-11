### Sets ###
"""
*Tanto sets como diccionarios los puedes crear con {}

- Un set NO es una estructura ordenada. Por lo tanto, si quieres acceder a un elemento mediante
un índice, no podrás hacerlo.

- NO admite elementos repetidos

- Es mutable. Se pueden editar los elementos de dentro.

- Lo bueno del SET es que es más óptimo que una lista o una tupla, en el caso que:
    - no queramos guardar repetidos
    - no necesitemos guardar los elementos de forma ordenada
"""
my_set = set()
my_other_set = {} # así marca que es un diccionario
print(type(my_other_set))

my_other_set = {"Martí", "González", 27} # así marcará que es un set
print(type(my_other_set))

my_other_set.add("HolaMundo")
my_other_set.add("HolaMundo")
my_other_set.add("HolaMundo")
my_other_set.add("HolaMundo")
print(my_other_set) # solo se guarda un solo "HolaMundo"

print("Martí" in my_other_set) # para comprobar si existe un elemento

my_other_set.remove("HolaMundo") # para borrar un elemento
print(my_other_set)

another_set = {"Python", "Java"}
print(another_set)

all_sets = my_other_set.union(another_set) # el union() para unir 2 sets
print(all_sets)


# difference para retirar los elementos que concuerden con otro set
print(all_sets.difference(another_set))
# En este caso, se imprimirá todo lo de all_sets excepto los elementos que TAMBIÉN se encuentren en another_set
