"""
Python has the following data types built-in by default, in these categories:

   - Text Type:	str
   - Numeric Types:	int, float, complex
   - Sequence Types: list, tuple, range
   - Mapping Type: dict
   - Set Types:	set, frozenset
   - Boolean Type:	bool
   - Binary Types:	bytes, bytearray, memoryview
   - None Type:	NoneType

"""

# data type is set when you assign a value to a variable:
x = None
# can get the data type of any object by using the type() function:
print(x, type(x))

# can set the specific data type by constructor functions:
x = complex(1j)
print(x, type(x))
