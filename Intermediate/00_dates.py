### Dates ###
"""
Tenemos el datetime dentro de la librería datetime, que engloba la fecha y hora, pero tmb tenemos:
- datetime
- timestamp
- time
- date
"""
# hay un datetime dentro de datetime, por eso la línea de: from datetime import datetime
import datetime
from datetime import datetime

# DATETIME:
# El datetime() tiene tanto la fecha como la hora
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print("- - - - ")

# TIMESTAMP - - - - - - - - - - - 
# Este número indica cuántos segundos han pasado desde el 1 de enero de 1970 hasta el momento actual.
# Se usa para: comparar fechas fácilmente, para almacenar marcas de tiempo de manera estándar...

timestamp = now.timestamp() 
print(timestamp)
print("- - - - ")

year_2025 = datetime(2025, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)

print("date_now:")
print_date(now)
print("year_2025:")
print_date(year_2025)

# TIME - - - - - - - - - - - - - - - - - - - - - 
# El time es para representar tiempo (horas, min, seg...)
from datetime import time

current_time = time() # esto está vacío, hay que rellenarlo
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# DATE - - - - - - - - - - - - - - - - - - - - - 
# Para representar la fecha
from datetime import date

#current_date = date() # esto está vacío, hay que rellenarlo
#print(current_date.year) --> Esto daría error pq date() está vacío

current_date = date.today() # así nos da la fecha actual
print(current_date)

current_date = date(2025, 8, 7) # también podemos definir nosotros un date concreto
print(current_date.day) # dará 7

# Cómo cambiamos la fecha?
current_date = date(current_date.year, current_date.month, current_date.day + 10)
print(current_date.day) # Ahora da 17

# DIFERENCIA entre 2 fechas - - - - - - - - -
# Esto nos imprimirá cuánto tiempo hay entre 2 fechas.
# Para que se pueda hacer, las variables han de ser del mismo tipo
diff = now - year_2025
print(diff) # --> se puede porque los 2 son del mismo tipo (datetime)

other_diff = current_date - year_2025.date()
print(other_diff)

#TIMEDELTA - - - - - - - - - - - - - - - - - - - 
# Nos sirve para trabajar con franjas de fechas
from datetime import timedelta

start_timedelta = timedelta(200, 10, 100, weeks=10)
end_timedelta = timedelta(300, 10, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
