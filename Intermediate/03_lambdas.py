### Lambdas ###
"""
Una lambda es una función anónima (sin nombre) que se escribe en una sola línea.
Se usa para definir funciones rápidas y cortas, sin necesidad de usar def.
"""

# Creación de una lambda
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_values(2, 2))


#Lambda dentro de una función
def sum_three_values(value_fun):
    return lambda first_value, second_value: first_value + second_value + value_fun

print(sum_three_values(5)(2, 3))

