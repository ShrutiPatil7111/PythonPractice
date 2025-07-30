'''
There are four collection data types in the Python:

1. List :       ordered,    changeable.                 Allows duplicate members.
2. Tuple:       ordered,    unchangeable.               Allows duplicate members.
3. Set  :       unordered,  unchangeable* & unindexed.  No duplicate members.
4. Dictionary:  ordered**,  changeable.                 No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. 
In Python 3.6 and earlier, dictionaries were unordered.
'''

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("List is:", thislist)
print("Number of items in the list:", len(thislist))
print("Type of thislist:", type(thislist)) # lists are defined as objects with the data type 'list'
print("Acess 2nd element:", thislist[1])
print("Acess 2nd element by -ve indexing:", thislist[-4])
print("-4:-1:", thislist[-4:-1])

list1 = ["abc", 34, True, 40, "male"] # list can contain different data types
print("List is:", list1)
print("Type of list1:", type(list1))

if "apple" in thislist:
  print("Yes, 'apple' is in thislist") # Check if Item Exists


"""
When we say that lists are ordered, 
it means that the items have a defined order and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

The list is changeable, 
meaning that we can change, add and remove items in a list after it has been created.
"""