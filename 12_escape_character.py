'''
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string 
that is surrounded by double quotes
'''
"""
Even though backslash is within triple quotes ''', 
Python still processes escape sequences inside strings unless they're marked as raw.
Thus, showing the warning!
"""

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 