print( 1 + 1 )
print( '1' + '1' )

age = 24
# print( "Alex is " + age + "years old." ) # Error
print( "Alex is " + str(age) + "years old." )
print( "Alex is " + str( 23 ) + "years old." )

name = 'Alex'
name_and_age = "My name is {0}. I\'m {1} years old.".format( name, age )
print( name_and_age )

name_and_age = "My name is {0}. I\'m {1} years old.".format( "name", age )
print( name_and_age )

name_and_age = "My name is {}. I\'m {} years old.".format( name, age )
print( name_and_age )

name_and_age = "My name is {name_f}. I\'m {age_f} years old.".format( name_f = name, age_f = age )
print( name_and_age )



float_result = 1000/7
print( float_result )
print( "The result of division is {0:1.3f}".format( float_result ) )
print( "The result of division is {0:10.3f}".format( float_result ) )

name = 'Alex'
age  = 24

# Py = 2
print( "My name is %s. I\'m %d y.o." %( name, age ) )

# Py >= 3.6
print( f"My name is {name}. I\'m {age} y.o." )