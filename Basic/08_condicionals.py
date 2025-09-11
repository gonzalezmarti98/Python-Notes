### Conditionals ###
"""
- no hacen falta () ni {}
- se usan los ":"
- dentro del IF o del ELSE hay lo que esté tabulado
"""
my_condition = 5 * 2
print("Resultado exacto:",my_condition)
print(type(my_condition))

if my_condition > 10 and my_condition < 20:
    print("El resultado está entre 10 y 20")
elif my_condition == 1:
    print("El resultado = 1")
else:
    print("Resultado es menor de 10 o mayor de 20, excepto 1")

my_condition = "Hola"

if my_condition == "Hola":
    print("Concuerda el string")