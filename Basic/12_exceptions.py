### Exception Handling ###
"""
TRY - EXCEPT - ELSE - FINALLY
- el ELSE y FINALLY son opcionales
- ELSE: se ejecuta si NO entramos en el EXCEPT
"""

number_one, number_two = 1, 2

try:
    print(number_one + number_two)
except:
    print("Except: Ha habido un error")
else:
    #se ejecuta si NO entramos en el except
    print("No hemos entrado en el 'except'. La ejecución del programa continúa.")
finally:
    print("Entramos en finally. Esto SIEMPRE se ejecuta")


# EXCEPTIONS POR TIPO:
number_two = "2"

try:
    print(number_one + number_two)
except TypeError as e:
    print("Error de tipo TypeError")
    print(e)
except ValueError:
    print("Error de tipo ValueError")
except Exception as error: # esto es para capturar el error general que se haya dado
    print(error)

# Si no queremos capturar el error genérico, simplemente ponemos "except:" y ya
