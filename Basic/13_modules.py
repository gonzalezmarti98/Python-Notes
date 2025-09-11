### Modules ###
"""
- Se puede importar una clase entera
- Se puede SOLO una función, dentro de una clase
"""
#CLASE ENTERA

import ejemplos_funciones

ejemplos_funciones.sum_value(1,2)

#FUNCIÓN CONCRETA
#***También podemos renombrar una funcion que importamos

from ejemplos_funciones import sum_value, print_value as imprime_Valor

sum_value(2,3) #cuando es una función concreta, se llama como si estuviera en esta misma clase
imprime_Valor("ahs")


from math import pi as PI_VALUE

print(PI_VALUE)