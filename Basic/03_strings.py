### Strings ###

print("Linea con\nsalto de línea") # saltos de línea con \n
print("Linea con\ttabulación") # tabulación con \t

# Formateo
name, surname, age = "Marti", "González", 27
print("Mi nombre es", name, surname,"y mi edad",age) # primera posible forma. Al programa le cuesta más leerlo
print("Mi nombre es %s %s y mi edad %d"%(name, surname, age)) # segunda forma. Mejor para formatear datos como "%d"
print("Mi nombre es {} {} y mi edad {}".format(name, surname, age)) # tercera forma
print(f"Mi nombre es {name} {surname} y mi edad {age}") # ✅cuarta forma. La mejor y más rápida

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f, = language # cada variable será una letra
print(a)
print(b)
print(c,"\n")

# División
language_slice = language[0:3] #des del índice 0 al 3: Pyt (el último no incluido)
print(language_slice)

language_slice = language[1:3] #del 1 al 3: yt (el último no incluido)
print(language_slice)

language_slice = language[2:] # des del índice 2 al final: thon
print(language_slice)

language_slice = language[-2] #penúltima: o
print(language_slice)

language_slice = language[1:2:4] # y
print(language_slice)

reversed_language = language[::-1] # Reverse
print(reversed_language)

print("\n")

# Funciones
print(language.capitalize()) # Python
print(language.upper()) # PYTHON
print(language.count("t")) # 1
print(language.isnumeric()) # False
print("1".isnumeric()) # True
print(language.lower()) # python
print(language.startswith("py")) # False
print(language.startswith("Py")) # True