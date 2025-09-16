### Error Types ###
"""Razonamiento de los errores"""

# --- SyntaxError ---
"""error de escritura"""
#print "Hola comunidad"
print("Hola comunidad")

# --- NameError ---
"""Cuando falta definir algo que quieres usar"""
#print(lenguaje)

# --- IndexError ---
"""Te equivocas en la escritura de los índices. Fuera de rango por ejemplo."""
my_list = ["Python", "Swift", "Java"]
#print(my_list[3])

# --- ModuleNotFoundError ---
""" Cuando intentas importar un modulo que no existe"""
#import mathS
import math

# --- AttributeError ---
"""Equivocación al escribir un atributo"""
#print(math.PI)
print(math.pi)

# --- KeyError ---
my_other_dict = {"Nombre":"Martí", "Apellido":"González", "Edad":27, 1:"Python"}
#print(my_other_dict["Nommbbrre"])
print(my_other_dict["Nombre"])

# --- TypeError ---
"""Los indices han de ser ints.
En el caso de una lista, se filtra por indices no por nombres de elementos"""
my_new_list = ["hola", "botella"]
#print(my_new_list["hola"])
print(my_new_list[0])

# --- ImportError ---
"""Equivocación al importar. Debido a equivocación de nombre"""
#from math import PI
from math import pi

# --- ValueError ---
"""Error transformando ints, strings, etc"""
#my_int = int("10 años") # esto no se puede transformar en int
#print(type(my_int))

# --- ZeroDivisionError
#print(4/0) 
print(4/2)