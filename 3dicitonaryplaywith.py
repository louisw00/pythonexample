# not ordered
# 0. Create list by SQUARE bracket
#    Create tuple by PARANTHESE
#    Create dictionary by curly bracket/braces
mydict = {"name": "Louis", "age": 28, "city": "Beijing"}  # not equal sign
print(mydict)
mydict2 = dict(name="Louis", age=28, city="Beijing")  # equal sign
print(mydict2)

# 1. add items in dictionary
mydict["email"] = "aug@com"
# 这种形式会跟list[index]搞混 要特别注意dictionary是add 而list是modify
# 2. delete items
del mydict["email"]  # 1
mydict.pop("age")  # 2
mydict.popitem()  # 3
print(mydict)


# 3 iteration
for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)

# unpack
packdic = {"a": 1, "b": 2}
a, b = packdic.values()
print(a, b)
a, b = packdic.keys()
print(a, b)
a, b = packdic.items()
print(a, b)

# 1. items
print(mydict.items())

# 2. key and value
value = mydict["name"]
# In Python, you can't directly find a key by its value using the syntax mydict["Louis"] because dictionaries are designed to be accessed by keys, not values. However, you can achieve this by iterating through the items of the dictionary and checking if the given value matches any of the values in the dictionary. Here's one way to do it:
mydict = {"name": "Louis", "age": 28, "city": "Beijing"}


def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found


result = find_key_by_value(mydict, "Louis")
print(result)


# comphensions
sentence = "hello my name is tim"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)
