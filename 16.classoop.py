class Person():
    pass


person = Person()

# we can danamically add attributes /methods to objects
# method 1
# person.first = "louis"
# person.last = "wu"

# print(person.first)
# print(person.last)

# method 2 what if the attributes we want to set is the value of another variables
# setattr is able to use the value of a variable

firstname_key = 'firstname'
firstname_val = 'louis'

# we set the value of a variable as an attribute
setattr(person, firstname_key, firstname_val)

print(person.firstname)

print(getattr(person, firstname_key))
