a = "Hello, World!"
# Square brackets can be used to access elements of the string
print(a[1])
# Since strings are arrays, we can loop through the characters in a string
for x in a:
  print(x)
# To get the length of a string, use the len() function
print("Length of string a is", len(a))

'''
print("Length of string a is " + len(a))
TypeError: can only concatenate str (not "int") to str
'''

txt = "The best things in life are free!"
# To check if a certain phrase or character is present in a string, 
# we can use the keyword in.
print("free" in txt)
# To check if a certain phrase or character is NOT present in a string, 
# we can use the keyword not in.
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")