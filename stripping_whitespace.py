# extra whitespace in your program can be confusing to the readability of your code
# an example of this is 'Python' and 'Python ' are two very different things
# as such python has methods to look for extra white space on the right and left sides of a string

# here we will use the rstrip() method to ensure that no whitespace exists on the right end of a string
favorite_language = 'python '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language)

# as you can start to see how parenthesis work by taking in information such as the variable we 
# have just did a few things to
# the method that we just executed has taken the white space off of the right side of our variable

# same operation but on the left side of the variable
favorite_language.lstrip

# note that the r and l strip methods only temporarily remove the white space and to permanently remove
# them you will have to associate the stripping operation with the variable name

favorite_language = "python"
# note the parenthesis for the method 
favorite_language = favorite_language.rstrip()
favorite_language
'python'

# finally there is a .strip() method to strip the white space from both sides at once
# here is an example of striping

# as you can see when you execute the program I put a ton of white space in the string and on our second
# operation the strip method has removed the space and the print shows the space removed
strip_example = "         striping"
print(strip_example)
input()
striping_the_strip = strip_example.lstrip()
print(striping_the_strip)