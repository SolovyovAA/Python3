#1 Lesson 1: Hello World
# print("Hello Python!")

#2 Lesson 2: Math ops
# print(2+2)
# print(2-2)
# print(2*2)
# print(2**3) #Степень
# print(2/2)
# print(2//2) #Деление с округлением (до меньшего а-ля Py2)
# print(2%2)
# print(2&2)

#3 Lesson 3: Variables and PEP8 conv.
# x - int
# x = 5
# print(x)

# x - let's change x var type to str (cuz Py has dynamically typed variables)
# x = "Some string"
# print(x)

# In Py name of variables should be in snake_case
# type_of_variable_x = type( x )
# print(type_of_variable_x)

# Some math ops, but now we will use variables
# x = 2
# y = 3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x**y) #Степень
# print(x/y)
# print(x//y) #Деление с округлением (до меньшего а-ля Py2)
# print(x%y)
# print(x&y)

#4 Lesson 4: String variables
greeting = "Hello"
first_name = "Alex"
last_name  = "Solovyev"
exclamation_sign = "!"
print( greeting + ' ' + first_name + ' ' + last_name + exclamation_sign )

# Long string
long_string = "This is the long string"
print( long_string )

# Whole sentence string
whole_sentence = greeting + ' ' + first_name + ' ' + last_name + exclamation_sign
print( whole_sentence )

# Escaping
some_string = 'I\'m a programmer'
print( some_string )

another_string = "I want to learn \"Python\""
print( another_string )

string_with_new_line = "Hello\nMy name is Alex"
print( string_with_new_line )

# \r - возврат каретки
string_with_new_line2 = "Hello\n\rMy name is Alex"
print( string_with_new_line2 )

# Triple quotes
string_with_triple_quotes = """ This is text with "triple quotes" """
print( string_with_triple_quotes )