'''
Booleans represent one of two values: True or False.
Almost any value is evaluated to True if it has some sort of content.
There are not many values that evaluate to False, 
except empty values, such as (), [], {}, "", the number 0 and the value None. 
And of course the value False evaluates to False.

'''
print(bool("abc"))
print(bool(-23))

print("Empty values give False:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = 200
# Python also has many built-in functions that return a boolean value, like
# isinstance(): which can be used to determine if an object is of a certain data type
print(isinstance(x, int))
