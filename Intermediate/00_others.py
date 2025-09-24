
# --- abs() ---
"""Devuelve el resultado absoluto de una operación"""
result = abs(7 - 10)
print(result)
print("--------------")


# --- zip(list_1(), list_2(), *) ---
"""El zip() sirve para iterar varias listas al mismo tiempo, comparando
los elementos con el mismo índice"""

lista_1 = [0,1,2,3]
lista_2 = ["zero", "uno", "dos", "tres"]

for num, str in zip(lista_1, lista_2):
    print(num, str)

