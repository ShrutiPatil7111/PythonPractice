x, y, z = "Orange", "Banana", "Cherry" 
# can assign values to multiple variables in one line
print(x,  y, z)
# can use the , operator to output multiple variables

x = y = z = "Orange"
# can assign the same value to multiple variables in one line
print(x + y + z)
# can also use the + operator to output multiple variables
# Imp: space character is not there after vari

x = 5
y = 10
print(x + y)
# For numbers, the + character works as a mathematical operator

y = "Python"
print(x + y)
# but will get an error, when try to combine string & number with the + operator

"""
Unpacking:
splitting up the elements of a collection (like a list, tuple or set) 
into individual variables
"""
# tuple:
point = (4, 5)
x, y = point
print(x)  # Output: 4
print(y)  # Output: 5

#list
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

# Using the Asterisk *: to grab the "rest" of the values

print(middle)  # Output: [2, 3, 4]
