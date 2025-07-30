'''
we cannot combine strings and numbers like this:
txt = "My name is John, I am " + age

To specify a string as an f-string, 
simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations.

'''

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)