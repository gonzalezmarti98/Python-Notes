### Loops ###
"""
Un ELSE después de un búcle, ya sea WHILE o FOR, hace que se ejecute lo de dentro cuando termina el bucle
"""

# WHILE
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
    if my_condition == 2:
        print("ahora es 2")
        continue # detiene la ejecución a éste punto y vuelve al inicio del while
else:
    print("Hemos salido del while") # éste ELSE pertenece al WHILE realmente


# FOR
print("\nFOR")
my_list = [35, 24, 44, 7, 22, 6, 0]
for e in my_list:
    print(e)

# En un diccionario, se imprimen las CLAVES, no los valores
my_dict = {"Nombre":"Marti", "Apellido":"Gonzalez", "Edad":27, "cm de picha":111}
for element in my_dict: 
    print(element)

# Para imprimir los VALORES, hay que acceder a ellos con values():
for element in my_dict.values():
    print(element)
else:
    print("El FOR ha finalizado")