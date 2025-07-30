"""
Set of built-in methods that can be used on strings:
upper(): returns the string in upper case
lower(): returns the string in lower case
strip(): removes any whitespace from the beginning and/or the end
replace(): replaces a string with another string
split(): splits the string into substrings if it finds instances of the separator

"""

a = " HI! Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

text = "banana"
print(text.replace("a", "o"))         # Output: "bonono"
print(text.replace("a", "o", 2))      # Output: "bonona"
'''
Only replaces the first two "a"s. 
The method doesn't change the original string, 
since strings in Python are immutable; it returns a new string
'''