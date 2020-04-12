#5 Lesson 5: Length
greeting = "Hello Python!"
greeting_length = len( greeting )
print( greeting_length )

#6 Lesson 5: Print at index
print( greeting[ 4 ] ) # forward indexing
print( greeting[ -4 ]) # backward indexing

#7 Lesson 5: Slicing
print( greeting[ 2:5 ] )
print( greeting[ 6:10 ] )
print( greeting[ -5:-2 ] )
print( greeting[ 2: ] )
print( greeting[ :5 ] )
print( greeting[ : ] )

# Slicing with steps
print( greeting[ ::2 ] )
print( greeting[ ::1 ] )
print( greeting[ ::3 ] )

print( greeting[ 2::2 ] )
print( greeting[ 1::3 ] )
print( greeting[ 1:9:3 ] )

print( greeting[ ::-1 ] ) # backward print