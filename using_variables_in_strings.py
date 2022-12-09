# this demonstrates how to use a variable in a string

# first name the variables and assign them values
first_name = "nick"
last_name = "mccrady"

# next we will add a f to use a fstring , f standing for format because python formats the 
# string by replacing the name of the variable with its value and the braces denote a variable 
full_name = f"{first_name} {last_name}"
print(full_name)

# we can also compose a complete message using f-strings
myFirst_name = "nicholas"
myLast_name = "mcCrady"
myFull_name = f"{myFirst_name} {myLast_name}"
# next we can use a method on the variable to capitalize the title remember the braces are used to denote a 
# variable and the parenthesis is to give information to the method
print(f"Hello, {myFull_name.title()}!")

# we can also use f-strings to to compose a message and then assign the whole thing to a variable
msgFirst_name = "nick"
msgLast_name = "mccrady"
msgFull_name = f"{msgFirst_name} {myLast_name}"
message = f"hello, {msgFull_name.title()} !"
print(message)
# note that f-strings were first introduced in version 3.6 of python if you are using an older version 
# you will need to use the format() method
# ex. full_name = "{}{}".format(first_name,last_name)

