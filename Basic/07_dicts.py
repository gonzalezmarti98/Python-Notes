### Dictionaries ###
"""
En un diccionario podemos guardar los datos de tipo clave valor
    *Para acceder a un elemento NO necesitas el índice, llamas al nombre del elemento:
    print(my_dict["Lenguajes"])✅
    print(my_dict[2])🛑
"""

my_dict = dict()
my_other_dict = {} # un SET tmb se define así, pero por ahora, esto es un type(dict)

my_other_dict = {"Nombre":"Martí", "Apellido":"González", "Edad":27, 1:"Python"}
my_dict = {
    "Nombre":"Martí",
    "Apellido":"González",
    "Edad":27,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.72
    }

# para búsquedas de valores a traves de su CLAVE
print(my_dict["Lenguajes"])

# para cambiar valores a partir de una clave
my_dict["Nombre"] = "MGM"

# forma para agregar una nueva clave/valor al diccionario. Se guarda al final x defecto
my_dict["Calle"] = "Om"
print(my_dict)

# para eliminar clave/valor? --> a través de la CLAVE
del my_dict["Calle"]
print(my_dict)

# buscar por CLAVE
print("MGM" in my_dict) # --> dará False pq Martí es un VALOR, no una clave
print("Nombre" in my_dict) # --> True porque Nombre es una CLAVE

print(my_dict.keys()) # retorna solo las CLAVES
print(my_dict.values()) # retorna solo los VALORES

# FROMKEYS --> Crear un diccionario VACÍO
my_new_dict = dict.fromkeys(("Nombre", "Apellido", 1))
print(my_new_dict)

# Aquí creamos un diccionario que será igual al que le pases pero VACÍO
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

print("\n")
print(list(my_new_dict)) # imprime las CLAVES en los 3 casos
print(tuple(my_new_dict))
print(set(my_new_dict)) # desordenado pq es un SET

