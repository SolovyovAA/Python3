# Immutable (неизменяемые)
first_name = 'Jake'
print( first_name[ 2 ] )

# In this we'll get errors cuz it's impossible in Py. The line first_name is immutable
##
#Traceback (most recent call last):
# k
# File "C:/Users/Professional/IdeaProjects/PythonLessons/IntroductionToStrings/string_properties_and_methods.py", line 5, in <module>
# first_name[ 2 ] = 'n'
# TypeError: 'str' object does not support item assignment
##
#first_name[ 2 ] = 'n'
#print( first_name )

first_two_letters = first_name[ :2 ]
print( first_two_letters )
last_letter = first_name[-1:]
print( last_letter )

# Concantenable
new_first_name = first_two_letters + 'n' + last_letter
print( new_first_name )

greeting = "Hello"
greeting = greeting + " Python!"
print( greeting )

# Multiplication
yummy = "Yum "
print( yummy*3 )

# Methods
print( yummy.upper() )
print( yummy.lower() )
print( yummy ) # By the upper and lower methods we don't change the source string. this methods make a new strings

long_string = "This is a long string"
print( long_string.split() ) # split by default - by spaces
print( long_string.split( 's' ) ) # split by 's' character
