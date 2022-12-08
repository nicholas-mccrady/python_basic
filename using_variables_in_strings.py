# this demostrates how to use a variable in a string

# first name the variables and assign them values
first_name = "nick"
last_name = "mccrady"

# next we will add a f to use a fstring , f standing for format because python formats the 
# string by replacing the name of the variable with its value and the braces denote a variable 
full_name = f"{first_name} {last_name}"


print(full_name)