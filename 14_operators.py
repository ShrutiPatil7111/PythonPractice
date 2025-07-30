x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
'''
Identity operators: 
Used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location
'''
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

'''
Membership operators:
Used to test if a sequence is presented in an object
'''
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
