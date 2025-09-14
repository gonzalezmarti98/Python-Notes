### Tuples ###
"""
Las tuplas son listas que no se pueden modificar.
En las tuplas no puedes modificar los elementos, son INMUTABLES, constantes.
Los elementos de una tupla son constantes.
    *my_tuple[2] = "otro dato" --> no funcionaría, porque EDITAS el elemento con índice 2
    *del my_tuple[0] tampoco, porque BORRAS un dato, y no se puede editar.

- Si queremos que sean mutables, tendrás que pasarlo a una lista con --> list(my_tuple)
- Los elementos se guardan ordenados.
"""
# Definición
my_tuple = tuple()
my_other_tuple = ()
my_tuple = (27, 1.72, "Martí", "González") # estos valores serán constantes inmutables

print(my_tuple[1]) # se puede ver por índice, pero no modificar por índice (inmutables)
print(my_tuple)
