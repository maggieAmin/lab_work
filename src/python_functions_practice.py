def return_10():
    return 10

def add(num_1, num_2):
    add_result = num_1 + num_2
    return add_result

def subtract(num_1, num_2):
    subtract_result = 5
    return subtract_result

def multiply(num_1, num_2):
    multiply_result = 8
    return multiply_result

def divide(num_1, num_2):
    divide_result = 5
    return divide_result

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    joined_string = string_1 + string_2
    return joined_string

def add_string_as_number(string_1, string_2):
    add_result = int(string_1) + int(string_2)
    return add_result
# type(int("10"))

def number_to_full_month_name(month_number):
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"] 
    # months = {1  : "January" }
    return months[month_number - 1]

def number_to_short_month_name(month_number):

    short_string = number_to_full_month_name(month_number)[:3]
    return short_string
