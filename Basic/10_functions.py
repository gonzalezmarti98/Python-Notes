### Functions ###
"""
Las funciones en Python son de tipado:
    - débil
    - dinámico
Es decir, que no podemos forzar que entre un tipo de dato concreto

Ejemplo:
def sum_two_values(first_num:int, second_num:int):
    print(first_num + second_num)

    ---> aunque pongamos :int, si metemos un String, se lo comerá igualmente
"""

def sum_two_values(first_num, second_num):
    print(first_num + second_num)

sum_two_values(5, 1)
sum_two_values("5","1") # los strings los suma poniendo uno junto al otro --> 51


def print_info(name, age):
    print(f"Me llamo {name} y tengo {age} años")


print_info(age=27, name="Martí")

# Valores x DEFECTO: 
def print_with_default(name, age, alias = "No existe"):
    print(f"Me llamo {name} y tengo {age} años. Mi alias es: {alias}")

print_with_default("Martí", 27) # el alias será "No existe"(por defecto).
print_with_default("Martí", 27, "mgonzalez98")

# Valores dinámicos. Puedes poner tantos como quieras. Solo hay que poner un "*" en la variable
def print_text(*text):
    print(text)

print_text("Hola")
print_text("Hola", "Martí")
print_text("Hola", 27, "Maria guapota")

