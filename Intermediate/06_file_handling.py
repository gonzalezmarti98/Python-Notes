### File Handling ###
"""Manejo de ficheros"""

# ----- .txt file ----- ##

import os

txt_file = open("Intermediate/my_file.txt", "w+")
"""w+ --> escritura y lectura. Si el archivo existe, lo sobrescribe
   r+ --> para lectura y escritura. No borra el contenido existente. Si el archivo no existe, lanza un error."""

txt_file.write("Me llamo Marti\nMi apellido es Gonzalez\nTengo 27 años")
#print(txt_file.read())
print(txt_file.read(15))
print(txt_file.readline()) # para leer una línea
print(txt_file.readline()) # la siguiente
print(txt_file.readlines()) # devuelve una lista con las líneas
for line in txt_file.readlines():
    print(line)

txt_file.write("\nMe gusta Java")

txt_file.close() # para cerrar el archivo, liberar recursos del sistema y asegurar los cambios realizados

#os.remove("Intermediate/my_file.txt") ---> para ELIMINARLO


# ----- .json file ----- ##

import json

json_file = open("Intermediate/my_jason_file.json", "w+") #creo este fichero si no existe

json_text = {
    "name": "Marti",
    "surname":"Gonzalez",
    "age":27,
    "languages":["Python", "Java", "Swift"],
    "website":"https://github.com/gonzalezmarti98"
    }

# Para ESCRIBIR, solo se pueden pasar strings. Con el dump() podemos pasarle otras variables
json.dump(json_text, json_file, indent = 2)
# si hacemos otro dump(), lo escribirá debajo

# Lectura de líneas
json_file.close()

with open("Intermediate/my_jason_file.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)

