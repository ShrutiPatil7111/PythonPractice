def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
By default, any variable defined within a function is local to that function 
and cannot be accessed outside of it.

However, if we want the variable to be global — 
meaning accessible throughout the entire program,
we can declare it using the global keyword inside the function.

"""