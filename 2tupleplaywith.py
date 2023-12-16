import sys
# 1. Create list by SQUARE bracket
#    Create tuple by PARANTHESE
#    Create dictionary by curly bracket/braces
mytuple = 5, 1, 2, 3, 4  # paranthese is optional
print(mytuple)

# 2.index - ordered
print(mytuple[1])
print(mytuple.index(5))

# 3. tuple is immutable
# mytuple[1] = 5
mytuple1 = list(mytuple)
print(mytuple1)
mytuple1[0] = 8
print(mytuple1)

# 4. fully unpack tuple
mytuple2 = "louis", 28, "Beijing"
name, age, city = mytuple2
print(mytuple2)

# 5. partially unpack
i1, *i2, i3 = mytuple
print(i2)  # become a list

# 6.tuple is smaller than list and more efficient than list
mylist = [5, 1, 2, 3, 4]
print(sys.getsizeof(mytuple), "bytes")
print(sys.getsizeof(mylist), "bytes")
