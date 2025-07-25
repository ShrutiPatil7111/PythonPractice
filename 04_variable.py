'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

'''

x1 = 5
y_2 = "John" 
_z3 = float(3) # Casting: can specify the data type of a variable
print(x1, type(x1)) # type() function: can get the data type of a variable
x1 = "Sunny"
print(x1, type(x1))
print(y_2, type(y_2))
print(_z3, type(_z3))

"""
Rules for Python variables:
- start: letter, underscore _ , NOT digit
- can't contain: special symbols, spaces, keywords
- case-sensitive (age, Age and AGE are three different variables)
"""