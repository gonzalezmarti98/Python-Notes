### Clases ###
"""
- Las clases se escriben en camel-case.
- Se puede llamar a la clase tanto con como sin paréntesis: Person | Person()
- para hacer PRIVADO un atributo, en el constructor se le pone "__" antes del nombre
    ejemplo: self.__name = name --> esto es un atributo privado
"""
class EmptyPerson:
    pass

# CONSTRUCTOR DE UNA CLASE:
class Person:
    def __init__(self, name, surname):
        self.__name = name # privada
        self.surname = surname # pública
    #función de una clase. Hay que pasarle el "self" para poder acceder a sus atributos
    def walk(self):
        print(f"{self.get_name()} {self.surname} está caminando")
    
    def get_name(self):
        return self.__name


my_person = Person("Martí", "González")
print(f"Mi nombre es {my_person.get_name()} {my_person.surname}")
my_person.walk()

#Recordatorio: Python es de tipado débil, por lo tanto puedes cambiar totalmente lo de dentro de los atributos
#sean Strings, ints...
#my_person.name = 6666
#print(f"Mi nombre es {my_person.name} {my_person.surname}") # imprimirá: 666 González