# consultar tipo de dato
print(type("Hola Python"))

# NO hay que usar "camel case". Ha de ser "snake case", es decir: todo minúsculas y separado por _
my_variable = "My str" #✅
myVariable = "My str" # 🛑

# CASTEOS - cambiar los tipos de variables
my_int = 5
print(my_int)
print(type(my_int)) # int
print("- - - - - ")
my_int_to_string = str(my_int)
print(my_int_to_string)
print(type(my_int_to_string)) # string
print("- - - - - ")
print(type(print(""))) # NoneType