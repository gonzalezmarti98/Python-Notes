### Higher Order Functions ###

# Le pasamos una función como parámetro de otra función (f_sum_one)
def sum_one(value):
    return value + 1

def sum_two_values_and_function(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)

print(sum_two_values_and_function(5, 2, sum_one))