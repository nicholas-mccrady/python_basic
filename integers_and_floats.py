# when you divide any two numbers even if they are integers that result in a whole number
# you will always get a float. if you mix an integer in any other operation that uses a float you will get
# a float as well, python defaults to a float in any operation that uses a float even if the output is a
# whole number
example_float_number_1 = 1
example_float_number_2 = 2.0
first_example_result = example_float_number_1 / example_float_number_2
print ("result of 1 / 2.0:",first_example_result)
# as you can see our output was changed to a float
# here are a few more examples
example_float_number_3 = 2
example_float_number_4 = 3.0
second_example_result = example_float_number_3 * example_float_number_4
print("result of 2 * 3.0:",second_example_result)
example_float_number_5 = 3.0
example_float_number_6 = 2
third_example_result = example_float_number_5 ** example_float_number_6
print("result of 3.0 ** 2",third_example_result)