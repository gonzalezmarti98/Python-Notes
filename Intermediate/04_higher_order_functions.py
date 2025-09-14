### Higher Order Functions ###

#----------- Closures -----------#
"""
Una closore es una función anidada dentro de otra que recuerda y puede acceder
a las variables de su función externa y que puede seguir usándolas incluso después
de que la función externa haya finalizado.
"""

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


# 1a forma de llamarlo
add_closure = sum_ten(5)
print(add_closure(6))

# 2a y 3a forma
print(sum_ten(5)(6))
print((sum_ten(5)(6)))


#----------- Built-in Higher Order Functions -----------#

## 1 - Map ##
"""
Un map necesita:
- un listado iterable
- una función / lambda
El map devolverá otro listado iterable el cual cada uno de los elementos
habrá sido modificado por la función que le hemos pasado"""

numbers = [2, 5, 10, 21]

def multiply_two(number):
    return number * 2

my_map = map(multiply_two, numbers)
print(list(my_map))
# En este caso devuelve la misma lista de números pero multiplicado * 2: [4, 10, 20, 42]

my_map = list(map(lambda number: number * 2, numbers))
print(my_map)
# también se pueden pasar lambdas al map()


## 2 - Filter ##
"""
El filter() recorre todos los valores y ejecuta una función / lambda que retorna True o False
para saber como filtrar los valores del iterable"""

def greater_than_ten(number):
    if number > 10:
        return True
    return False

my_filter = list(filter(greater_than_ten, numbers))
print(my_filter)
# Aquí solo se imprimirán los que sean True

my_filter = list(filter(lambda number: number > 10, numbers))
print(my_filter)
# lo mismo con lambdas, y solo se imprimen los True


## 3 - Reduce ##
"""
Hay que importarlo de "functools".

reduce() reduce el iterable que le pasamos a un solo número. La función que le
pasamos debe aceptar dos argumentos:
- el acumulador (resultado parcial),
- y el siguiente elemento del iterable.



"""
from functools import reduce

numbers = [2, 5, 10, 21]

def sum_two_values(first_v, second_v):
    print(first_v)
    print(second_v)
    return first_v + second_v

print(reduce(sum_two_values, numbers))